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

# Data

## Weather

### importants data and their types :

1. Indicatif OMM station : numéro de station `numer_sta` -> `int`
2. Date (UTC) : `date` -> `datetime`
3. Pression au niveau mer : `pmer` -> `int`
4. Variation de pression en 3 heures : `tend` -> `int`
5. Type de tendance barométrique : `cod_tend` -> `int`
6. Direction du vent moyen 10 mn : `dd` -> `int`
7. Vitesse du vent moyen 10 mn : `ff` -> `float`
8. Température : `t` -> `float`
9. Point de rosée : `td` -> `float`
10. Humidité : `u` -> `int`
11. Visibilité horizontale : `vv` -> `float`
12. Temps présent : `ww` -> `int`
13. Nébulosité totale : `n` -> `float`
14. Nébulosité des nuages de l'étage inférieur : `nbas` -> `int`
15. Hauteur de la base des nuages de l'étage inférieur : `hbas` -> `int`
16. Pression station : `pres` -> `int`
17. Variation de pression en 24 heures : `tend24` -> `int`
18. Température minimale sur N heures : `tn12` -> `float`
19. Température maximale sur N heures : `tx12` -> `float`
20. Température minimale du sol sur 12 heures : `tminsol` -> `float`
21. Rafales sur les 10 dernières minutes : `raf10` -> `float`
22. Rafales sur une période : `rafper` -> `float`
23. Période de mesure des rafales : `per` -> `float`
24. Précipitations dans les N dernières heures : `rr12` -> `float`

### Categories

1. Informations générales
   - Numéro de station : `numer_sta` -> int
   - Date (UTC) : `date` -> datetime
2. Pression
   - Pression au niveau mer : `pmer` -> int
   - Variation de pression en 3 heures : `tend` -> int
   - Type de tendance barométrique : `cod_tend` -> int
   - Pression station : `pres` -> int
   - Variation de pression en 24 heures : `tend24` -> int
3. Vent
   - Direction du vent moyen 10 mn : `dd` -> int
   - Vitesse du vent moyen 10 mn : `ff` -> float
   - Rafales sur les 10 dernières minutes : `raf10` -> float
   - Rafales sur une période : `rafper` -> float
   - Période de mesure des rafales : `per` -> float
4. Température
   - Température : `t` -> float
   - Point de rosée : `td` -> float
   - Température minimale sur N heures : `tn12` -> float
   - Température maximale sur N heures : `tx12` -> float
   - Température minimale du sol sur 12 heures : `tminsol` -> float
5. Humidité
   - Humidité : `u` -> int
6. Visibilité
   - Visibilité horizontale : `vv` -> float
7. Nébulosité et nuages
   - Nébulosité totale : `n` -> float
   - Nébulosité des nuages de l’étage inférieur : `nbas` -> int
   - Hauteur de la base des nuages de l’étage inférieur : `hbas` -> int
8. Précipitations
   - Précipitations dans les N dernières heures : `rr12` -> float
9. Temps présent
   - Temps présent : `ww` -> int

## Locations

1. Indicatif OMM station : numéro de station `no` -> `int`
1. Nom de la ville: `numer_sta` -> `int`
1. Latitude: `latitude` -> `float`
1. Longitude: `longitude` -> `float`
1. Altitude: `altitude` -> `int`
