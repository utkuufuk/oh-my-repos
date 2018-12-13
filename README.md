# oh-my-repos
## Installation
 1. [Install myrepos](https://myrepos.branchable.com/install/)
 2. Optionally edit [config.json](config.json) to specify a default parent directory.
 3. Run the installation script:
    ``` sh
    sudo ./install.py
    ```

## Usage
Pull all git repositories in a parent directory in parallel:
``` sh
pull --dir="/path/to/your/repos/"
```

If you specified a default path in [`~/.config/oh-my-repos/config.json`](config.json) file, you can run the script without an argument:
```
pull
```