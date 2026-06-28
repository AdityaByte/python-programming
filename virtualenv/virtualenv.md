# virtualenv: Virtual Environment in python.
> **virtualenv** is a way by which you can seperate different python environments.

### Why do we need virtual environment?
> Umm let's assume you're working on different project on the same local machine and those project requirement are like they are working on the different version of a flask in that case you'll face conflict if you install the different version of a package to the local site package in that case the virtualenv is useful.

#### Without the virtualenv library.
```bash
# Command for creating a virtualenv
python -m venv .venv # .venv is the virtualenv name. 

# Command for installing the libraries to the virtualenv.
pip install -r requirements.txt
```



### Command for installing the virtualenv
```bash
pip install virtualenv
```

### Creating a virtual environment
```bash
virtualenv <environment-name> # Replace the it with your project/environment-name.
```
In order to activiate the new virtual environment that we have been create we have to run the `activate.bat` (windows specific) file.
```bash
cd project1_env/Scripts
# This command is for cmd.
activate.bat

# Ths command is for powershell.
./activate.ps1
```

If you want to re-check this python and pip we are using currently.
```bash
where python
where pip
```
As do we are in the virtual environment any package that we install is locally to this folder.
Example - You can try by installing one for them like numpy
```bash
pip install numpy
# Then check the list of installed pkgs.
pip list
```
If we want to export the packages to some other folder then you can do this.
```bash
# --local : It only takes the local entities.
pip freeze --local
```

### Going back to the global environment
```bash
# Just type
deactivate
```

### Creating a virtual environment with a specified python version.
```bash
# Linux/Mac specific
virtualenv -p \usr\bin\python3.7.7 <project-name>
# Windows
virtualenv -p <path-to-python-interpreter> <project-name>
```

> These virtualenv are meant to be only for dependency only they are not for project files.

# Creating a virtual env using a new package manager - uv
```
# Command for creating a new virtualenv.
uv venv .venv | uv venv

# Command for adding a library
uv add matplotlib

# Command for syncing with the pyproject.toml file.
uv sync
```