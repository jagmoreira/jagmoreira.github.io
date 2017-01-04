Title: Pyenv Tutorial
Date: 2014-07-07
Category: Development
Tags: pyenv, python, tutorial
Summary: Meet pyenv: a simple Python version management tool.

Meet [pyenv](https://github.com/yyuu/pyenv): a simple Python version management tool. Previously known as Pythonbrew, pyenv lets you change the global Python version, install multiple Python versions, set directory (project)-specific Python versions, and yes create/manage virtual python environments ("virtualenv's"). All this is done on *NIX-style machines (Linux and OS X) without depending on Python itself and it works at the user-level–no need for any `sudo` commands. So let's start!

## Installation
Follow the [installation instructions](https://github.com/yyuu/pyenv#installation) or use the [automatic installer](https://github.com/yyuu/pyenv-installer). If you're using a Mac, I highly recommend installing pyenv with [Homebrew](https://github.com/yyuu/pyenv#homebrew-on-mac-os-x) (none of that MacPorts shenanigans). Whichever way you decide to go, after checking out the repository, be sure to add a couple of lines to your `.bashrc` (`.bash_profile` on Mac) to enable pyenv's auto-complete functionality.

### Linux/OS X Copy-Paste Install
On a Mac replace `.bashrc` with `.bash_profile` below.

    :::shell
    ~$ git clone git://github.com/yyuu/pyenv.git .pyenv
    ~$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    ~$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    ~$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    ~$ source ~/.bashrc


### pyenv Suite Installer
This is the one-liner provided by the [automatic installer](https://github.com/yyuu/pyenv-installer).

    curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash


## Walkthrough

    ~$ pyenv global
    system
    ~$ pyenv versions
    * system (set by /home/staff/jmoreira/.pyenv/version)

Usually you will only have one version of python installed, the system-wide version. That's what's shown in the above command. pyenv now allows you to expand upon this version. Let's start by installing another python version. For instance, let's go now to the cutting edge of python:

    ~$ pyenv install 3.4.0
    Installing readline-6.3...
    Installed readline-6.3 to /home/staff/jmoreira/.pyenv/versions/3.4.0

    Installing Python-3.4.0...
    Installed Python-3.4.0 to /home/staff/jmoreira/.pyenv/versions/3.4.0

(By the way, there is no need to memorize these. `pyenv install -list` will show all available Python versions to install).

    ~$ pyenv versions
    * system (set by /home/staff/jmoreira/.pyenv/version)
      3.4.0

pyenv now lists two python versions. To use python 3.4 as the global one we do:

    pyenv global 3.4.0

You can also use pyenv to define a project-specific, or local, version of Python:

    ~$ pyenv global system

    ~$ mkdir cuting_edge
    ~$ cd cuting_edge/
    ~/cutting_edge$ pyenv local 3.4.0
    ~/cutting_edge$ python -V
    Python 3.4.0
    ~/cutting_edge$ cd ..
    ~$ python -V
    Python 2.7.6

It's as simple as that.


## Virtual Environments

To other virtualenv users, the idea of a local Python might seem familiar. Indeed, a local Python created from pyenv is almost like a Python virtual environment. The main difference is that pyenv actually copies an entire Python installation every time you create a new pyenv version. In contrast, virtualenv makes use of symbolic links to decrease the size of the virtualenv's.
If you can't function without your virtual environments anymore then fear not, for there is a plugin for that: `pyenv-virtualenv`. This plugin adds complete virtualenv functionality to pyenv:

    git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
    source ~/.bashrc

    ~$ mkdir virtual_env
    ~$ cd virtual_env/
    ~/virtual_env$ pyenv virtualenv 3.4.0 venv
    Ignoring indexes: https://pypi.python.org/simple/
    Requirement already satisfied (use --upgrade to upgrade): setuptools in /home/staff/jmoreira/.pyenv/versions/venv/lib/python3.4/site-packages
    Requirement already satisfied (use --upgrade to upgrade): pip in /home/staff/jmoreira/.pyenv/versions/venv/lib/python3.4/site-packages
    Cleaning up...

    ~/virtual_env$ pyenv versions
    * system (set by /home/staff/jmoreira/.pyenv/version)
      3.4.0
      lab_web
      venv

Here I used Python 3.4 to create the virtualenv (Note that if you want to create a virtualenv from the system Python, then virtualenv needs to be installed at the system level as well).

    ~/virtual_env$ pyenv activate venv
    (venv) ~/virtual_env$ python -V
    Python 3.4.0
    (venv) ~/virtual_env$ pip list
    pip (1.5.4)
    setuptools (2.1)
    (venv) ~/virtual_env$ pyenv deactivate
    ~/virtual_env

This last command is the recommended way to deactivate the virtualenv. This ensures that pyenv remains working as normal after you leave the virtualenv.

pyenv's magic works because it actually redefines your Python command:

    ~$ which python
    /home/staff/jmoreira/.pyenv/shims/python

When you try to run Python, it first looks for a `.python-version` in the current directory to decide which version of python to run. If it doesn't find this file, then it looks for the user-level file `~/.pyenv/version`.

And this is essentially all there is to it. Have fun developing Python code in a safe, environment-friendly way.

Special thanks to [Adam Pah](https://amaral.northwestern.edu/people/pah/) for the tips.
