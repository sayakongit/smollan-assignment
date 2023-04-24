# Smollan-assignment (Task-2)
==============================

This document will help you to setup the environment to execute the script.


## Table of Contents
- [Project Organization](#project-organization)
- [Getting Started](#getting-started)

## Project Organization
------------

    ├── README.md          <- The README for using/validating this task.
    │
    ├── main.py           <- Main python file to run the selenium script.
    │
    └── requirements.txt   <- The requirements file for reproducing the analysis environment.


## Getting Started
------------

### On your Windows machine
1. To get this repository, run the following command inside your git enabled terminal

```bash
$ git clone https://github.com/sayakongit/smollan-assignment.git
```

2. Change the name of folder that contains this whole repo: `smollan-assignment` -> `{your project name}` and navigate to that folder.

3. Install Python version >=3.10.5

4. Install virtual environment by running 

```
pip install virtualenv
```

5. Create a virtual environment named `smollan` by running,

```
virtualenv smollan
```

6. Activate the environment by running the following on Windows PowerShell.
```
.\smollan\Scripts\activate.ps1 
```
on Windows PowerShell.
(If you get `UnauthorizedAccess` error, enter this command `Set-ExecutionPolicy Unrestricted -Scope Process` followed by `Y` before activating the environment.)

7. Install the package's dependencies in `requirements.txt` with pip by running 

```
pip install -r requirements.txt
```

8. Download and copy the folder-path of `chromedriver.exe` (as per you Chrome version) and modify the line no. 6 in `main.py` as follow
```
DRIVER_PATH=r"<folder-path>\chromedriver.exe"
```

9. Deactivate the virtual environment by running 
```
deactivate
```

    
--------
