# Config

## Create venv

```bash
python3 -m venv venv
source .venv/bin/activate
```

## Generate your `requirements.txt`

`requirements.txt` is a txt file that contains the project dependancies

```bash
pip freeze > requirements.txt
```

If the project has `requirements.txt` then install the the dependancies

```bash
pip install -r requirements.txt
```
