#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LEOZA
#
# Created:     29/06/2021
# Copyright:   (c) LEOZA 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random


def gen_mdp(n_mini,n_maj,n_num,n_ponct):
    mdp=''
    if n_mini > 0:
        for loop in range(n_mini):
            mdp=mdp+chr(random.randint(65,90))
    if n_maj > 0:
        for loop in range(n_maj):
            mdp=mdp+chr(random.randint(97,122))
    if n_num > 0:
        for loop in range(n_num):
            mdp=mdp+chr(random.randint(48,57))
    if n_ponct > 0:
        for loop in range(n_ponct):
            mdp=mdp+chr(random.randint(33,47))
    mdp = list(mdp)
    random.shuffle(mdp)
    mdp_melange=''
    for char in mdp:
        mdp_melange=mdp_melange+char
    return mdp_melange






