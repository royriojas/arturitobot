#!/usr/bin/env python

# -*- coding: utf-8 -*-

from search_geotagget_tuits import fetch_tuits
from generate_pages import generate_pages
import codecs
import sys
import lib
import argparse
from argparse import RawTextHelpFormatter



description = """Retrieve geotagget tuits based on location"""
parser = argparse.ArgumentParser(description=description,formatter_class=RawTextHelpFormatter)
parser.add_argument('-p', '--page', action='store_true', 
        help='Generate Google Map page',
        required=False, dest='page')

args = parser.parse_args()

if args.page == True:
    print "Generating page"
    generate_pages()
    sys.exit()

# open file with coordinates
f = codecs.open("carceles.txt", "r", "utf-8")
carceles = f.readlines()
f.close()

for carcel in carceles:
    carcel = carcel.strip().split(",")
    latitude = carcel[1].split(" ")[0]
    longitude = carcel[1].split(" ")[1]
    carcel = carcel[0]
    print "\n ###\t" + carcel
    radius = "1km"

    geocode = latitude + "," + longitude + "," + radius
    fetch_tuits(geocode, carcel)

generate_pages()
lib.delete_tuits_no_coords()
