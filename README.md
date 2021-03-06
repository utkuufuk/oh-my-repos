# Oh My Repos
A wrapper for the awesome [myrepos](https://myrepos.branchable.com/) tool that makes pulling your Git repositories even easier.

## Features
 * **Works from any directory.** You don't have to `cd` to your `$HOME` directory to use it.
 * **Usage is simple and easy.** You don't have to `mr register` your repositories one by one, just type `pull.`
 * **Parallel by default.** You don't have to explicitly tell it to use multiprocessing.
## Setting Up
 1. [Install myrepos](https://myrepos.branchable.com/install/)
 2. Run
    ``` sh 
    # normal installation
    pip3 install .
    ```
    ``` sh
    # development mode installation
    pip install -e .
    ```
 
#### Uninstall 
```
./uninstall.sh
```

## Usage
``` sh
# Pulls all git repos in all dirs specified in ~/.ohmyrepos.json
pull

# Pulls all git repos in input dir in addition to all dirs specified in ~/.ohmyrepos.json
pull -d /path/to/other/repos/

# Same as above, except now it also adds input dir to saved dirs in ~/.ohmyrepos.json
pull -d /path/to/other/repos/ -s
```

## Configuration
Just after the first execution of a command with `-s` (or `--save`) flag, the configuration file `.ohmyrepos.json` will be created inside your `$HOME` directory. 
You can always manually edit your saved directories from there:
``` json
    {
        "dirs": [
            "/path/to/your/repos",
            "/path/to/your/other/repos"
        ]
    }
```


