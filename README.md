# oh-my-repos
A wrapper for the awesome [myrepos](https://myrepos.branchable.com/) tool that makes pulling your Git repositories even easier.

## Features
 * **Works from everywhere;** you don't have to `cd` to your `$HOME` directory to use it.
 * **Configuration is simple and easy;** you don't have to `mr register` your repositories one by one.
 * **Implicitly parallel;** launches as many processes as the number of repositories to pull.
## Setting Up
 1. [Install myrepos](https://myrepos.branchable.com/install/)
 2. Run the installation script, passing the directory of your Git repositories as an (optional) argument:
    ``` sh
    ./install.sh /path/to/your/repos
    ```
 3. You can always change your Git root directory in `~/.oh-my-repos.json`
    ``` json
    {
        "dir": "/path/to/your/repos"
    }
    ```

## Usage
If you specified a default path in [`~/.oh-my-repos.json`](config.json), you can run the script without an argument:
```
pull
```

You can also run it for arbitrary directories: 
``` sh
pull --dir="/path/to/other/repos/"
```