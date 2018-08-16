# L5R 4E dice roller

[![Build Status](https://travis-ci.org/AlvaroRuizDelgado/L5R_4E_dice_roller.svg?branch=master)](https://travis-ci.org/AlvaroRuizDelgado/L5R_4E_dice_roller)

Script to roll dice for the 4th edition of the Legend of the 5 Rings roleplaying game (python 3).

## How to use

Make the script executable:
```shell
chmod u+x roll.py
```

Pass number of dice to roll-keep (e.g. 6k3), followed by a bonus/penalty if applicable.
```shell
./roll.py 6k3 [12] [-u] [-e value]
./roll.py 6k3 [-5] [--unskilled] [--explosion value]
```

Possible parameters:
```shell
    -u, --unskilled, dice explosion is disabled.
    -e, --explosion, threshold value for dice explosion (10 by default).
```

Examples:
```shell
./roll.py 5k2
./roll.py 5k3 -u
./roll.py 6k2 -e 9
```

## Container use

```shell
docker build -t l5r_dice .
docker run -it --rm l5r_dice
```

Or if you install [coverage.py](https://coverage.readthedocs.io/en/latest/):
```shell
coverage run test_roll.py
coverage report -m
coverage html
open htmlcov/index.html
```

You can also pull the container from dockerhub:
https://hub.docker.com/r/alpacarider/l5r_dice
