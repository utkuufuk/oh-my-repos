# oh-my-repos
## Installation
 1. [Install myrepos](https://myrepos.branchable.com/install/)
 2. Run the installation script:
    ``` sh
    sudo ./install.py
    ```

## Usage
Pull all git repositories in a parent directory in parallel:
``` sh
pull --dir="/path/to/your/repos/"
```

You can edit the [`~/.config/oh-my-repos/config.json`](config.json) file to specify a default path in order to run the script without any argument:
```
pull
```