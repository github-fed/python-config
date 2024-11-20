# Python Development Environment Setup Guide

## Prerequisites
- macOS
- Terminal (tested with Z shell)
- Homebrew

## Install pyenv

### macOS
```bash
brew install pyenv
```

### Update Terminal Configuration Zsh (`.zshrc`)

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

### Install Python Versions
```bash
pyenv install 3.12.0
pyenv install 3.6.15
pyenv versions
```

### Remove Potential Conflicts With System Python
```bash
alias python=$(which python)
alias python3=$(which python3)
```

### Set Global Python Version
```bash
pyenv global 3.12.0
pyenv which python
python --version
```

## Install Poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Create New Project
```bash
mkdir my-python-project
cd my-python-project
poetry init
poetry local 3.12.0
poetry env use 3.12.0
poetry add pytest
poetry shell
```

### Verify Installation
```bash
python --version
poetry --version
```

