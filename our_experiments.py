"""
Understanding the template code and the assignment by doing small manageable pieces


"""

import arcade
import arcade.gui as gui
import json
import sys
import secrets
from copy import copy

from constants import DrawMode
from mountain import Mountain
from mountain_manager import MountainManager
from trail import Trail, TrailSeries, TrailSplit
from draw_trails import TrailDraw
from mountain_organiser import MountainOrganiser
from double_key_table import DoubleKeyTable
from serialize import serialize, deserialize


"""
Create a simple trail with a moutain and serialize it.
"""

def basic_trail ():
    trail = Trail(TrailSeries (Mountain("only",2,2), Trail(None)))
    print(serialize(trail))





def main():
    """ Main function """
    basic_trail ()
if __name__ == "__main__":
    main()
