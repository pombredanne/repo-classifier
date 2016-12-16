# Repo Classifier

## Requirements
- python 3.5
- pip


## Setup
- Create a virtual environment with `pyvenv .venv`
- Activate the venv with `source .venv/bin/activate` or install `autoenv` and create a `.env` file as described below
- Install the dependencies with `pip install -r requirements.txt`
- Setup the python SDK to `.venv/bin/python` to also access the dependencies in the venv

### New Dependencies
- Install a dependency in the venv with `pip install DEPENDENCY`
- Save a snapshot of the dependencies with `pip freeze > requirements.txt`

### Configure autoenv
Simply create a file called `.env` in the root directory of the repository and paste this in it for Linux.
```
source .venv/bin/activate
echo "repo-classifier - NICE! (venv on)"
```


## Reference
- autoenv: https://github.com/kennethreitz/autoenv
- packaging: https://packaging.python.org/installing/
- venv: https://docs.python.org/3/library/venv.html