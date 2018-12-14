# oh-my-repos
A wrapper for the awesome [myrepos](https://myrepos.branchable.com/) tool that makes pulling your Git repositories even easier.

## Features
 * **Works from any directory.** You don't have to `cd` to your `$HOME` directory to use it.
 * **Usage is simple and easy.** You don't have to `mr register` your repositories one by one, just type `pull.`
 * **Parallel by default.** You don't have to explicitly tell it to use multiprocessing.
## Setting Up
 1. [Install myrepos](https://myrepos.branchable.com/install/)
 2. Run the installation script:
    ``` sh
    ./install.sh
    ```
 3. You can always manually configure your Git root directories in `~/.oh-my-repos.json:`
    ``` json
    {
        "dirs": [
            "/path/to/your/repos",
            "/path/to/your/other/repos"
        ]
    }
    ```

## Usage
``` sh
# Pulls all git repos inside each path specified in ~/.oh-my-repos.json
pull

# Pulls all git repos in the given path in addition to each path specified in ~/.oh-my-repos.json
pull --dir="/path/to/other/repos/"

# Same as above, except now it also inserts the given path in ~/.oh-my-repos.json
pull --dir="/path/to/other/repos/" --save
```