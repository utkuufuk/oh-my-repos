# oh-my-repos
## Setting Up
 1. [Install myrepos](https://myrepos.branchable.com/install/)
 2. Run the installation script, optionally passing your Git root as an argument:
    ``` sh
    ./install.sh /path/to/your/repos
    ```
 3. You can always change your Git root directory in `~/.config/.oh-my-repos.json`
    ``` json
    {
        "dir": "/path/to/your/repos"
    }
    ```

## Usage
If you specified a default path in [`~/.config/.oh-my-repos.json`](config.json), you can run the script without an argument:
```
pull
```

You can also run it for arbitrary directories: 
``` sh
pull --dir="/path/to/other/repos/"
```