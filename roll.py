#!/usr/local/bin/python3
# Last edited: 18/08/15

import sys
from random import randint

def roll(argv):
    if (len(argv) == 0 or "--help" in argv or "-h" in argv):
        print_help()
        sys.exit(0)

    # Die characteristics
    die_range = 10

    # Explode mechanic
    unskilled_flag = False
    explosion_threshold = 10

    # Get the arguments (flag for unskilled, accept exploding result in case it's 9 --> same conditional?).
    roll_keep = argv.pop(0)
    roll = int(roll_keep[0:roll_keep.find('k')])
    keep = int(roll_keep[roll_keep.find('k')+1:])
    bonus = 0
    while len(argv) > 0:
        if (argv[0] == "--unskilled" or argv[0] == "-u"):
            argv.pop(0)
            unskilled_flag = True
        elif (argv[0] == "--explosion" or argv[0] == "-e"):
            argv.pop(0)
            explosion_threshold = argv.pop(0)
        else:
            bonus = int(argv.pop(0))

    # 10 dice mechanic
    max_dice = 10
    if roll > max_dice:
        difference = roll - max_dice
        while keep < 10:
            if difference > 1:
                keep += 1
                difference -= 2
            else:
                break
        bonus += 2 * difference
        roll = max_dice
    if keep > max_dice:
        bonus += 2 * (keep - max_dice)
        keep = max_dice
    if keep > roll:
        keep = roll
    
    # Show the actual values
    print("Roll:",roll, "Keep:",keep, "Bonus:",bonus, "Explosion value:", explosion_threshold, "Unskilled:",unskilled_flag)

    # Roll and save to a list.
    results = []
    for i in range (0, roll):
        die_roll = randint(1,die_range)
        results.append(die_roll)
        if unskilled_flag == False:
            while die_roll >= explosion_threshold:
                die_roll = randint(1,die_range)
                results[i] += die_roll

    # Order the array and get the optimum result. Consider that there could be less dies rolled than kept.
    results.sort() # reverse=True)
    optimum = sum(results[roll-keep:]) + bonus

    # Show the optimum result in green (or perhaps a rotating color), with the other results in a row. The selected ones in white, the others in grey or something.
    class bcolors:
        PURPLE = '\033[95m'
        GREY = '\033[92m'
        ORANGE = '\033[91m'
        LIGHT_RED = '\033[35m'

    print(bcolors.GREY, results[0:roll-keep], bcolors.PURPLE, results[roll-keep:], bcolors.LIGHT_RED, "+", bonus, bcolors.GREY, "-->", bcolors.ORANGE, optimum, bcolors.GREY)
    return({'roll': roll, 'keep': keep, 'bonus': bonus, 'optimum_value': optimum})

def print_help():
    print("    Pass number of dice to roll-keep (e.g. 6k3), followed by a bonus/penalty if applicable.")
    print("        ./roll 6k3 [12] [-u] [-e value]")
    print("        ./roll 6k3 [-5] [--unskilled] [--explosion value]")
    print("    Optional parameters:")
    print("        -u, --unskilled, dice explosion is disabled.")
    print("        -e, --explosion, threshold value for dice explosion (10 by default).")
    print("    When using a container, substitute './roll' for 'docker run -it --rm l5r_dice' in the examples above.")
    print("        docker run -it --rm l5r_dice 6k3 [12] [-u] [-e value]")

if __name__ == "__main__":
   roll(sys.argv[1:])
