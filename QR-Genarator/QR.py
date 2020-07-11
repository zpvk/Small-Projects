# -*- coding: utf-8 -*-
"""
Created on: 11/07/2020
@author: Rohan Kumara

QR code Genrator app
"""


# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
qr_text = input("Enter Text what you want to make as QR code : ")
# Generate QR code
url = pyqrcode.create(qr_text)
selection = int(input("PNG(1) or SVG(2) :"))

# Create and save the svg file naming

if selection == 2:
    name = input("Enter name for .svg : ")
    url.svg(name, scale=8)
else:
# Create and save the png file naming
    name = input("Enter name for .png : ")
    url.png(name, scale=6)
