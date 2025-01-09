# Dev environment

### Python version
Recommended to use asdf to keep the same python version

Python version used in `.tool-versions` file

### Install dependencies
```
pip install -r requirements-dev.txt
```
### Run tests
```
PYTHONPATH=./app pytest -v
```
### Run app
```
python app/main.py
```