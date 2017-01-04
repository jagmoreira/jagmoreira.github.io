# jagmoreira.github.io

My personal website built with [Pelican](https://blog.getpelican.com/) using my own custom version of the [pelican-hyde](https://github.com/jagmoreira/pelican-hyde) theme, originally by [jvanz](https://github.com/jvanz).


## Why User instead of Project Pages

I like the simple, yet cool ring of `<user>.github.io` (even though I am now using a custom domain name :smile:), so I decided to build my website as a GitHub User Pages. This means the live website code can only live in the **master** branch of the repo. I didn't want to put the source code into a separate repo so after some searching I decided to split the repo into 2 branches:

* [**develop**](https://github.com/jagmoreira/jagmoreira.github.io/tree/develop): Contains all pelican settings, posts/pages source files, and theme submodule. This is the repo's default branch and where I do all the work.
* [**master**](https://github.com/jagmoreira/jagmoreira.github.io/tree/master): Contains the built website html and css code. All content here is derivative so I never work directly on this branch.


## Using `ghp-import` to publish to GitHub Pages

I use the [ghp-import](https://github.com/davisp/ghp-import) package to easily publish to GitHub Pages any website updates. It pushes the **output** dir to the **master** branch. **Note that, if the master branch already exists on your GitHub repo it will be destroyed**:

    $ pelican content -o output -s publishconf.py
    $ ghp-import output

Then, just make sure to add the **output** folder to the `.gitignore` to prevent from accidentally commiting it to the **develop** branch.

The `pelican-quickstart` script will ask you once for all necessary parameters and then will create a `gh-pages` Fabric task that automates the process even more: `$ fab gh_pages`.

By default, `ghp-import` will commit your new build with the message *"Update Documentation"*, which is not very useful. I modified the default `gh_pages` Fabric task to add the current date on commit:

```python
import datetime

# Github Pages configuration
env.github_pages_branch = 'master'
env.commit_message = "'Publish site on {}'".format(datetime.date.today().isoformat())

(...)

def gh_pages():
    """Publish to GitHub Pages"""
    rebuild()
    local('ghp-import -b {github_pages_branch} '
          '-m {commit_message} '
          '{deploy_path} -p'.format(**env))
```


## Development workflow

1. Checkout **develop** branch: `$ git checkout develop`

1. Write or update a post/page, or make any changes to the theme.

1. Commit and push all changes on **develop** branch: `$ git commit -am "..."; git push`

1. Re-build website and push **output** directory to **master** branch: `$ fab gh_pages`
