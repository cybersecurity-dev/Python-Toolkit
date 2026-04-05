<div align="center">
    <p align="center">
        <a href="https://github.com/cybersecurity-dev/awesome-python-programming-language">
          <img width="13%" src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/python.svg" />
        </a>
    </p>

# [Python](https://www.python.org/) Development [Toolkit](https://github.com/cybersecurity-dev/awesome-python-programming-language)
</div>

[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://github.com/cybersecurity-dev/Bash-Toolkit?tab=readme-ov-file#programming-language) 
[![Windows](https://custom-icon-badges.demolab.com/badge/Windows-0078D6?style=for-the-badge&logo=windows11&logoColor=white)](https://github.com/cybersecurity-dev/PowerShell-Toolkit?tab=readme-ov-file#programming-language)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)]()
[![Reddit](https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/Python/)

<p align="center">
    <a href="https://github.com/cybersecurity-dev/"><img height="25" src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/github.svg" alt="GitHub"></a>
    &nbsp;
    <a href="https://www.youtube.com/@CyberThreatDefence"><img height="25" src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/youtube.svg" alt="YouTube"></a>
    &nbsp;
    <a href="https://cyberthreatdefence.com/my_awesome_lists"><img height="20" src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/blog.svg" alt="My Awesome Lists"></a>
    <img src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/bar.gif">
</p>


## Python Package Manager

### PIP

* Linux

    ```bash
    python3 -m pip --version && \
    python3 -m venv .venv_poc && \
    source .venv_poc/bin/activate && \
    python3 -m pip install --upgrade pip && \
    XDG_CACHE_HOME=./cache_pip/ pip install -r requirements.txt
    ```

* Windows 
    
    ```powershell
    py -m pip --version
    py -m venv .venv_poc
    .venv_poc\Scripts\activate
    py -m pip install --upgrade pip
    XDG_CACHE_HOME=./cache_pip/ pip install -r requirements.txt
    ```

### UV

* Linux
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh  && \
    uv venv .venv_poc --python 3.15 --cache-dir ./.uv_cache && \
    source .venv_poc/bin/activate && \
    python --version && \
    uv pip install -r requirements.txt --cache-dir ./.uv_cache
    ```
* Windows
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

### CONDA

* Linux
    ```bash
    
    ```
* Windows
    ```powershell

    ```

##

### Interacting with the OS
* os
* sys

### Interacting with Files
* os.path
* pathlib
* shutil
* fileinput
* tempfile

### Command line arguments & Configuration Files
* argparse
* configparser

### Compressing & Decompressing Files
* gzip

### Running & Communicating with other Processes
* subprocess

### Running Remote Commands

* [Paramiko](https://github.com/paramiko/paramiko) - [Paramiko](https://www.paramiko.org/) is a pure-Python implementation of the SSHv2 protocol, providing both client and server functionality.
    ```python
    pip install paramiko
    ```

##

### My Awesome Lists
You can access the my awesome lists [here](https://cyberthreatdefence.com/my_awesome_lists)

### Contributing

[Contributions of any kind welcome, just follow the guidelines](contributing.md)!

### Contributors

[Thanks goes to these contributors](https://github.com/cybersecurity-dev/Python-Toolkit/graphs/contributors)!

[🔼 Back to top](#python-development-toolkit)
