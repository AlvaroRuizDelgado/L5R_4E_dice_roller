# L5R 4E dice roller

Script to roll dice for the 4th edition of the Legend of the 5 Rings roleplaying game (python 3).

## How to use

Make the script executable:
```shell
chmod u+x roll
```

Pass number of dice to roll-keep (e.g. 6k3), followed by a bonus/penalty if applicable.
```shell
./roll 6k3 [12] [-u]
./roll 6k3 [-5] [--unskilled]
```

Possible parameters:
```
    -u, --unskilled, dice explosion is disabled.
    -e, --explosion, threshold value for dice explosion (10 by default).
```

## Container use

```shell
docker build -t l5r_dice .
docker run -it --rm l5r_dice
```
