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

# Gitlab mirroring repo

## Create gitlab repo and clone it, and clone also this one

```bash
git git@gitlabvigan.iem:m2projettutore2024-2025-groupe1/donnees-meteo.git

git clone git@github.com:Mah224Moud/weather-data.git
```

## Add Gitlab as remote in weather-data

```bash
cd weather-data
git remote add gitlab git@gitlabvigan.iem:m2projettutore2024-2025-groupe1/donnees-meteo.git
```

## Check the remotes

```bash
git remote -v
```

You shoud see two remotes:  
`origin` for github  
`gitlab` for gitlab

## Push all github commit histories to gitlab

```bash
git push gitlab --mirror
```

From now on, evrytime you push your `origin`, you should do the same for `gitlab`

```bash
git push origin
git push gitlab
```

In case of new update, just pull `origin` and/or add your features, commit then push it. And push also `gitlab`
