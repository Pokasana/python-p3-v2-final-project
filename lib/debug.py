#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.art import Art
from helpers import *

def reset_db():
    Artist.drop_table()
    Art.drop_table()

reset_db()
