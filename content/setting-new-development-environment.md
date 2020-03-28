Title: Setting up a new development environment
Date: 2017-01-03
Category: Development
Tags: dotfiles, bash
Summary: Learn how to set up your own personalized development environment on a new machine.

**NOTE**: This is an updated version of a [guide I wrote for the Amaral Lab](https://amaral.northwestern.edu/resources/guides/setting-new-development-environment). Since writing the original version, I updated Sublime Text to version 3, changed how version control software is configured, and added Homebrew configuration.

Setting up your development environment on a new computer can be a pain. You start by installing your favorite editor (sublime, vim, emacs, spacemacs, etc.). After that you need to install all your essential packages and plugins (the ones that make you go *"How can your live without XX? This is impossible to work."* every time a colleague asks you to check out something on their computer). Then, if you work with a scripting language like python or ruby, you also need to download an interpreter and configure it for your projects. In my work I use pyenv which makes this part super easy. Finally you go into the little details and configure the look and feel of the operating system (shell prompt, aliases, handy functions etc), and also set up all the environment variables that connect all the part... Like I said, setting up a dev environment on a new computer can be a pain.

Fortunately a lot of programmers have had this problem before, and since most of them hate having to do the same task more than once, they came up with ways to automate this painful and tedious process.

Nowadays a simple google search will give you access to plenty of scripts for setting up a new dev environment on your system of choice. However during my searches I couldn't find a script that I really liked. They either didn't automate enough parts or automated way more parts than I used. So I decided to write my own custom script, and instead of just sharing it and have it be useful for no one besides myself, I thought I would instead explain how you can make your own setup script.

This guide will help you set up a development environment on a new Unix system only. That means either Linux flavors or macOS. Sorry Windows!


### Organizing your dotfiles

First things first, in order to automate the setup of your environment you need to have one to begin with. On Unix systems most of the relevant settings for developers are stored in the so-called "dot files". These are are a set of files whose name starts with a “.” and sit in your home directory. Using dotfiles you can customize the look of the terminal, define handy functions aliases and keyboard shortcuts, and configure text-based editors, version control systems, plotting libraries, and much, much more. I'm going to assume you have your own set of dotfiles you are happy with. If you don't have one, just search the web for "sensible dotfiles" and you will find tons of examples.
Here's some tips to get you started:

**1 - You should always have both a `.bashrc` and a `.bash_profile`.**
Most Unix systems run a non-login shell which, by default, reads first the `.bash_profle` and then `.bashrc` (if they exist); on macOS the shell is a login shell, which *does not* read the `.bashrc` ([What's this about *login* and *non-login* shells?](http://apple.stackexchange.com/a/13019)). So, a good way to keep your configuration multi-system, is to have a `.bash_profile` that just reads from the `.bashrc`:

    :::shell
    $ cat ~/.bash_profile
    [ -n "$PS1" ] && [ -f ~/.bashrc ] && source ~/.bashrc


Then you can write all your configurations in the `.bashrc`.

**2 - Organize your `.bashrc` settings by sections.** The order is not very important. In my `.bashrc` I have: Bash options, exports, `PATH` variable, aliases, bash completions, prompt, and finally functions. Some terminal commands behave slightly differently on macOS than they do on Linux. This is because macOS is based on BSD (another type of Unix distribution), which defines its own version of popular commands such as `ls`, `ln`, `cat`, `head`, `tail`, and others. On macOS, if you use [Homebrew](http://brew.sh/) you can install the Linux versions, which are actually written by the GNU foundation:

    :::shell
    $ brew install coreutils.


Then modify your `PATH` like so:

    :::shell
    # Only modify path if both Homebrew and coreutils are installed
    if type brew > /dev/null 2>&1 && [ -d $(brew --prefix coreutils) ]; then
        # Add brew-installed GNU core utilities bin
        export PATH="$(brew --prefix coreutils)/libexec/gnubin:$PATH"
        # Add man pages for brew-installed GNU core utilities
        export MANPATH="$(brew --prefix coreutils)/libexec/gnuman:$MANPATH"
    fi

This ensures the GNU versions of those commands are the ones loaded in the shell. If you want to keep your configuration general, you need to add some checks in `.bashrc` to make sure your aliases work as expected in both systems. Here's how you can configure your `bash_profile` to make `ls` have colors in both macOS and other Unixes:

    :::shell
    # Detect which `ls` flavor is in use
    if ls --color >/dev/null 2>&1; then # GNU `ls`
        COLORFLAG='--color'
        GROUPDIRS='--group-directories-first'
        # GNU ls has much finer resolution so it's better to put it in its own file
        if type dircolors >/dev/null 2>&1; then
            [ -r ~/.dir_colors ] && eval "$(dircolors -b ~/.dir_colors)"
        fi
    else # OS X `ls`
        COLORFLAG='-G'
        # OS X `ls` does not have this option
        GROUPDIRS=''
        # ls color generator: http://geoff.greer.fm/lscolors/
        export LSCOLORS=ExGxFadxCxDaDaabagacad
    fi

    alias ls="ls  ${GROUPDIRS} ${COLORFLAG}"

**3 - If you `.bashrc` is getting too large, it might be good to move some sections to their own separate files and then source them from the `.bashrc`.** Here I have my prompt customization and my bash functions defined elsewhere:

    :::shell
    for FILE in ~/.{bash_prompt,bash_functions}; do
        [ -f "$FILE" ] && . "$FILE";
    done
    unset FILE

**4 - It's not that important, but to keep your shell environment clean, be sure to `unset` any variables in your bash files that are not exported nor defined as local.** Otherwise they will always be defined in your shell sessions.

So these are my dotfiles that I want to have in place in all my development environments:

* `~/.bash_functions`
* `~/.bash_prompt`
* `~/.bash_profile`
* `~/.bashrc`
* `~/.gitconfig`
* `~/.gitignore`
* `~/.hgrc`
* `~/.hgignore`
* `~/.vimrc`
* `~/.matplotib/matplotlibrc`

Because I use ssh a lot to connect between the lab computers I accumulated my own set of ssh configurations so I'm adding this file as well.

* `~/.ssh/config`


### Sublime Text configuration files

Some editors keep their configurations files in a dedicated location. If that's your case you need to find it and take note of the files/folders you need when starting again from scratch. Sublime Text, my editor of choice, keeps files in of these locations:

* Ubuntu: `~/.config/sublime-text3/`
* macOS: `~/Library/Application Support/Sublime Text 3/`

For Sublime you actually should only copy files from your User folder, namely settings, custom build systems, snippets, and theme files:

* `*.sublime-settings`
* `*.sublime-build`
* `*.sublime-snippet`
* `*.sublime-theme`
* `*.tmTheme`


### Writing the installer script

Now the real work begins! We want a script or series of scripts that we can run on any new system that copies all the files for us. We want this script to be available from anywhere so we should really place it somewhere online. GitHub and Bitbucket are some of the most popular platforms for this purpose. Pick whichever one you're most comfortable with, noting that by default GitHub repos are public while Bitbucket repos are private. Here I'm using GitHub.

    :::shell
    $ mkdir /path/to/your/project
    $ cd /path/to/your/project
    $ git init
    $ git remote add origin git@bitbucket.org:joao_moreira/dotfiles.git

Now we just copy our files inside the repo. Here's what mine looks like.

    :::shell
    $ ls -R -1 **
    Brewfile
    locate_sublime_config.sh
    setup_dev_env.sh

    dotfiles:
    bash_functions
    bash_profile
    bash_prompt
    bashrc
    dir_colors
    gitignore
    matplotlibrc
    screenrc
    ssh_config
    vimrc

    sublime_configs/Packages/User:
    (All my Sublime Text stuff)

    vc_files: (More on these later)
    gitconfig
    hgrc
    vc_settings.template

    $ git add .
    $ git commit -m “Add dotfiles and sublime config”
    $ git push

Alright. We have our files safely in our repo. Now we just need a script to install these files on demand.

#### Main dotfiles

    :::shell
    $ cat setup_dev_env.sh
    #!/bin/bash

    # Find full directory name where this script is located
    # http://stackoverflow.com/a/246128
    CWD=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

    echo -n "Sym-linking dotfiles..."
    ln -isv $CWD/dotfiles/bash_prompt ~/.bash_prompt
    ln -isv $CWD/dotfiles/bash_functions ~/.bash_functions
    ln -isv $CWD/dotfiles/bash_profile ~/.bash_profile
    ln -isv $CWD/dotfiles/screenrc ~/.screenrc
    ln -isv $CWD/dotfiles/dir_colors ~/.dir_colors
    ln -isv $CWD/dotfiles/gitignore ~/.gitignore
    ln -isv $CWD/dotfiles/vimrc ~/.vimrc

    # Matplotlib config lives in different places depending on the OS
    if [ "$(uname)" == "Darwin" ]; then
        ln -isv $CWD/dotfiles/matplotlibrc ~/.matplotlib/matplotlibrc
    elif [ "$(uname)" == "Linux" ]; then
        ln -isv $CWD/dotfiles/matplotlibrc ~/.config/matplotlib/matplotlibrc
    fi
    echo "done!"

As you can see, this script actually creates a symbolic link to the dotfiles in our home directory. This way every time you change your dotfiles you don't have to worry about copying your changes to the "gold standard" dotfiles, you already did it! Just remember to commit your changes to the repo, so they will apply the next time you need to start fresh.
**NOTE**: If you are already have some dotfiles in your home folder ths script will ask if you want to override them or not.


#### Git and Mercurial configuration files

Since these config files typically have your user name and email, you may want to keep them out of the repository, specially if your dotfiles repo is a public one. Yet it's still nice to be able to install them automatically. I solved this issue using a 3-step process:

1. All non-sensitive configurations (basically everything except username and email) I place in version-controlled files, which are put in place using rsync:

        :::shell
        rsync -abi $CWD/vc_files/hgrc ~/.hgrc
        rsync -abi $CWD/vc_files/gitconfig ~/.gitconfig


1. Then I have a separate sub-script `vc_files/vc_settings.local`, which is not in the repo, that adds username and email to those files:

        :::shell
        $ cat vc_files/vc_settings.template
        # Version control settings
        # Not in the repository, to prevent people from accidentally committing under my name

        # Git credentials
        git config --global user.name "John Doe"
        git config --global user.email "john.doe@mail.com"

        # Mercural credentials
        echo '' >> ~/.hgrc
        echo '[ui]' >> ~/.hgrc
        echo 'username = Jonh Doe <doe@mail.com>' >> ~/.hgrc
        echo '[trusted]' >> ~/.hgrc
        echo 'users = john_doe' >> ~/.hgrc
        echo 'groups = john_doe' >> ~/.hgrc

        (modify the template file with your own settings)

        $ cp vc_files/vc_settings.template vc_files/vc_settings.local

    Note that the `vc_files/vc_settings.template` is version-controlled. This way you don't have to rely too much on memory.

1. This sub-script is called during the installation script after the above rsync step:

        :::shell
        (... rest of setup_dev_env.sh)

        echo "Installing local configuration..."
        VC_LOCAL="$CWD/vc_files/vc_settings.local"
        VC_TEMPLATE="$CWD/vc_files/vc_settings.template"
        if [ -f $VC_LOCAL ]; then
            source $VC_LOCAL
        else
            echo "$VC_LOCAL not found. Did you create it from the template file?"
            echo
            echo -e "\t$ cp $VC_TEMPLATE $VC_LOCAL"
        echo


#### Homebrew installation (macOS only)

[Homebrew](http://brew.sh/) is the awesome package manager for macOS. It performs the same function as apt-get on Ubuntu. I use it to manage most of my non-system packages. Fortunately Homebrew is super easy to install programmatically, and using the `bundle` tap and a `Brewfile`, you can install all your packages in one fell swoop. The `Brewfile` lists all your installed packages:

    :::shell
    $ brew tap Homebrew/bundle
    $ brew bundle

These two commands create the `Brewfile` mentioned above. This is Homebrew's version of python's pip requirements file or ruby's Gemfile.

Now we can write the next section of your setup script:

    :::shell
    echo "Installing Homebrew and useful packages..."
    if [ "$(uname)" == "Darwin" ]; then

        # Install homebrew if it does not yet exist
        if ! type brew >/dev/null 2>&1; then
            /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        fi

        # Then install the packages using Homebrew-bundle
        brew tap Homebrew/bundle
        ln -isv $CWD/Brewfile ~/Brewfile
        brew bundle -v
    fi
    echo


#### Sublime Text configuration

Here I can't use symlinks because they won't capture any eventual files that will be created if I install any new sublime packages. To account for this I use rsync to keep the configuration synced to the repo.

    :::shell
    (... rest of setup_dev_env.sh)

    echo -n "Configuring Sublime Text..."
    SUBL=$($CWD/locate_sublime_config.sh)
    rsync -tprhm $CWD/sublime_configs/ "$SUBL"
    echo "done!"

This will sync the configuration files from the repo to the sublime installation location.
Then in my `.bash_functions.sh` I have a function that does the reverse:

    :::shell
    # Backup sublime text settings
    backup_sublime() {
        local REPO_LOCATION=$(locate_dev_repo)
        local SUBL=$($REPO_LOCATION/locate_sublime_config.sh)

        echo
        echo -n "Backing up Sublime Text configuration..."
        rsync -tprhm \
            --include="/Packages/User/*.sublime-settings" \
            --include="/Packages/User/*.sublime-snippet" \
            --include="/Packages/User/*.sublime-build" \
            --include="/Packages/User/*.sublime-theme" \
            --include="/Packages/User/*.tmTheme" \
            --include "*/" \
            --exclude="*" \
            --delete-excluded \
            "$SUBL/" "$REPO_LOCATION/sublime_configs"
        echo "done!"
    }

If I change any sublime settings all I need to do is:

    :::shell
    $ backup_sublime

and those settings will be backed up!

The line `local REPO_LOCATION=$(locate_dev_repo)` calls a [function](https://github.com/jagmoreira/dotfiles/blob/master/dotfiles/bash_functions) that does a more complicated version of "Find full directory name where this script is located". You can find it [here](http://stackoverflow.com/a/246128). The reason we can't use the one-liner from earlier (see definition of `$CWD`) is that when you call this function, `.bash_functions.sh` will be a symlink, and we need a recursive expression that can "dereference" the link.

Also, if you're scratching your head at the rsync `--include` syntax... I've been there too. It took me quite a while to get it to work properly. Basically the reason you have to be so verbose in the file specification is that rsync include/exclude rules are applied to each directory in a depth-first-search manner. If you don't do it this way you either sync all files in all directories or no files at all!

`locate_sublime_config.sh` is a handy little script that tries to guess which system you're running and returns the location to sublime settings location:

    :::shell
    $ cat locate_sublime_config.sh
    #!/bin/bash

    # Finds the location of Sublime Text configurations in several systems

    MACOS_DEFAULT="$HOME/Library/Application Support/Sublime Text 3"
    LINUX_DEFAULT="$HOME/.config/sublime-text-3"

    if [ -d "$MACOS_DEFAULT" ]; then
        SUBL="$MACOS_DEFAULT"
    elif [ -d "$LINUX_DEFAULT" ]; then
        SUBL="$LINUX_DEFAULT"
    else
        SUBL=""
    fi

    echo "$SUBL"
    unset SUBL
    unset MACOS_DEFAULT
    unset LINUX_DEFAULT


#### Installing pyenv

I work mainly with python so I include [pyenv](https://github.com/yyuu/pyenv) in my setup script. Instead of being dependent on whichever version ship with the OS, with `pyenv` I can have concurrent, self-contained, python installations. If you're interested in trying it out check out [my pyenv tutorial]({filename}./pyenv-tutorial.md)!

Fortunately pyenv has an automatic installer, so we just need one more line in our install script:

    :::shell
    (... rest of setup_dev_env.sh)
    if [ "$(uname)" == "Linux" ]; then
        echo "Installing pyenv..."
        curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
    fi

On a mac machine pyenv is installed as a Homebrew formula so this step is skipped.


And that's it! With this installer you can be sure to speed up the setup of your development environment.


### More suggestions

If you want to get fancier with your dev setup here are some suggestions:

* Add some command line flags to check for existing files, select what to install, etc.
* For Linux, add a section in `setup_dev_env.sh` that actually installs Sublime Text.
* For macOS, you can add a dotfile to configure pretty much anything in the OS. More info [here](https://github.com/mathiasbynens/dotfiles/blob/master/.osx).


### Acknowledgments

When writing this guide and my own dotfiles I relied heavily on these great github repos:

* [https://github.com/mathiasbynens/dotfiles](https://github.com/mathiasbynens/dotfiles)
* [https://github.com/necolas/dotfiles](https://github.com/necolas/dotfiles)
* [https://github.com/miohtama/sublime-helper](https://github.com/miohtama/sublime-helper)

Their authors deserve most of the credit for this guide!
