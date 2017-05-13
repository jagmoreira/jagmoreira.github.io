Title: Updating the micro python version of virtual environments
Date: 2017-05-13
Category: Development
Tags: python, bash, pyenv
Summary: How to systematically update the micro version of python for all virtual environments in your system using pyenv.

**TL;DR**: I wrote a [gist](https://gist.github.com/jagmoreira/b922d0524a5b7bc9500ea4b8c372e66b) to systematically update the micro version of python for all virtual environments in your system using pyenv!

Python projects should be implemented inside virtual environments (virtualenvs). If you are not doing it yet, then please start. Right now! Virtualenvs are essential to ensure reproducibility and to keep different projects sand-boxed from each other. You specify a `requirements.pip` file and a python **A.B** (major and minor) version and anyone else, including future you, should be able to re-create your project results.

Yet, there is some flexibility in virtualenvs *because of the micro version*. Python releases follow a A.B.C versioning system, where **C** represents a micro update to a given **A.B** version. These micro updates are reserved for security and bug fixes. As I write this post, the latest [active](https://docs.python.org/devguide/index.html#status-of-python-branches) releases from python's [official page](https://www.python.org/downloads/) are 3.6.1, 3.5.3, and 2.7.13.

Since virtualenvs are typically only tied to a **A.B** version, we can improve the security and stability of a project by updating the virtualenv's micro version of python without affecting anything project results.


## Updating the micro version of a single virtualenv

I use pyenv (link) to manage all my version of python, so if I wanted to update the micro version of one of my 3.5.1 projects:

    $ pyenv versions
      system
      3.5.1
      3.5.1/envs/proj

First I install the latest 3.5.x version:

    $ pyenv install 3.5.3
    (...)

Then I save the packages list of the virtualenvs packages:

    $ pyenv shell proj
    (proj)$ pip freeze > proj_requirements.pip
    (proj)$ pyenv shell --unset

Now I can safely remove the old 3.5.1 `proj`, and create a new `proj` based on 3.5.3:

    $ pyenv uninstall proj
    (...)
    $ pyenv virtualenv 3.5.3 proj
    (...)


Finally I install the packages again to the new venv:

    $ pyenv shell proj
    (proj)$ pip install -r proj_requirements.pip

    $ pyenv versions
      system
      3.5.1
      3.5.3
      3.5.3/envs/proj

And voilá.

If you don't use the base 3.5.1 you can now safely uninstall it:

    $ pyenv uninstall 3.5.1



## What if I have a lot of virtualenvs?

I hear you. I have 15 different environments spread across both python 2.7 and 3.5 in my lab workstation myself! It would be a pain to go through the above process manually for each one of those virtualenvs, that's why I decided to write a script that does all the work for me!

The first step is to find all main python versions currently installed:

    :::shell
    $ pyenv versions
      system
      2.7.10
      2.7.10/envs/foo
      2.7.10/envs/bar
      2.7.12/envs/baz
      3.5.3
      3.5.3/envs/proj
      foo
      bar
      baz
      proj

      $ pyenv versions --bare | grep / | cut -f 1 -d / | uniq
      2.7.10
      2.7.12
      3.5.3

Next, for each **A.B** version we search for the latest micro version:

    :::shell
    #!/usr/bin/env bash

    # First update pyenv to get any new python versions
    pyenv update

    # Get currently installed main pythons with derived virtualenvs
    MAIN_PYTHONS="$(pyenv versions --skip-aliases --bare | grep / | cut -f 1 -d / | uniq)"

    for VERSION in $MAIN_PYTHONS; do
        # Get the latest micro version for each A.B python
        MAJOR_MINOR="$(echo $VERSION | cut -f 1,2 -d .)"
        LATEST_MICRO=$(pyenv install -l | grep -E "(^| )$MAJOR_MINOR" | sort -b -V | tail -n 1 | sed -e 's/^[ \t]*//')

        # If there are no new micro versions
        # we move on to the next main Python
        if [[ "$VERSION" = "$LATEST_MICRO" ]]; then
            echo -n "Version $VERSION is already the latest version in the $MAJOR_MINOR.x series."
            continue
        fi

        echo "Found a new micro version for python $VERSION!"
        echo "$VERSION -> $LATEST_MICRO"
    done

    $ ./update_envs_micro_python.sh
    (...pyenv update...)
    Checking for micro version updates for python 2.7.10.
    Found a new micro version for python 2.7.10!
    2.7.10 -> 2.7.13
    Checking for micro version updates for python 2.7.12.
    Found a new micro version for python 2.7.12!
    2.7.12 -> 2.7.13
    Checking for micro version updates for python 3.5.3.
    Version 3.5.3 is already the latest version in the 3.5.x series.

I only use virtualenvs derived from the *vanilla* python versions but it should be easy to adapt the code above for other distributions (anaconda, jython, pypy, etc.).

Then, for each new micro version, we need to install it, making sure that pip is up-to-date as well (pip 9+ ensures python2-only packages are not installed in python3 environments, and vice-versa):

    :::shell
    # Install the latest micro and upgrade pip
    pyenv install -s "$LATEST_MICRO"
    pyenv rehash
    export PYENV_VERSION="$LATEST_MICRO"
    pip install --upgrade pip


Now all we have to do is find all virtualenvs for each major.minor, so we can apply the procedure I first described at the top of the post:

    :::shell
    # Get all virtual environments for this minor version
    VENVS="$(pyenv versions --skip-aliases --bare | grep $VERSION/ | cut -f 3 -d /)"
    N_VENVS=$(echo $VENVS| wc -w)
    echo "Found $N_VENVS virtual environments built with python $VERSION."

    for ENV in $VENVS; do
        echo "Upgrading micro python version of '$ENV' virtualenv: $VERSION-> $LATEST_MICRO"

        ENV_PIP_REQS="__tmp_${ENV}_requirements.pip"

        export PYENV_VERSION="$ENV"     # "Activate" the virtualenv
        pip freeze > $ENV_PIP_REQS
        pyenv uninstall -f "$ENV"
        pyenv virtualenv "$LATEST_MICRO" "$ENV"
        pyenv rehash

        echo "Re-installing $ENV with all its packages."

        # PYENV_VERSION is still set. No need to update it since
        # it's just a string with the virtualenv name,
        # which did not change.
        pip install --upgrade pip
        pip install -r $ENV_PIP_REQS

    done


### Regarding pandas and statsmodels

While I was testing my script, I re-learned that installation of older versions of these packages via requirements file will fail unless their required packages are already installed. Dependency management in python projects was a [bit of a pain](https://blog.miguelgrinberg.com/post/the-package-dependency-blues) [until recently](https://glyph.twistedmatrix.com/2016/08/python-packaging.html). My solution for virtualenvs that use old versions of these packages is to install them separately before installing the full requirements:

    :::shell
    # If numpy is present install it manually, otherwise some
    # package installations might fail due to mall-formed
    # installation requirements
    NUMPY="$(grep numpy= $ENV_PIP_REQS)"
    if [[ -n $NUMPY ]]; then
        pip install $NUMPY
    fi

    # Installation of old versions of statsmodels may fail due to mall-formed
    # installation requirements. To prevent this, we install all other
    # packages first then try the full requirements file again
    if [[ -n "$(grep statsmodels $ENV_PIP_REQS)" ]]; then
        sed -e '/statsmodels/d' $ENV_PIP_REQS | pip install -r /dev/stdin
    fi
    pip install -r $ENV_PIP_REQS

The reason statsmodels is done differently is because it has several requirements (numpy, scipy, pandas, patsy) that can all be installed in one go via requirements file, if numpy is already installed. There are probably other packages out there that suffer from the same issues. Adapt as necessary to your purposes.


## Putting it all together

I uploaded the full script, with some additional tweaks as a [public gist](https://gist.github.com/jagmoreira/b922d0524a5b7bc9500ea4b8c372e66b).

Hope it's useful to someone else!
