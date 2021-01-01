'''
====================================================
LIBRARIES USED:
pyqrocde - Module to automate the building process 
			of the QRCode
png - To save the QRCode output as a png file, does
	  not have to include .png when naming

QRCode - To generate the building process

validators - Used to validate the URL of the website

sys - Used to handle the arguments in the terminal
==================================================== 
'''
import pyqrcode 
import png
from pyqrcode import QRCode
import validators
import sys


def qr_gen(user_url):
	url = pyqrcode.create(user_url)
	url.png('QRCode.png', scale = 8)


if __name__ == '__main__':
	print('===============================')
	valid=validators.url(sys.argv[1])
	if valid==True:
	    qr_gen(sys.argv[1])
	    print('\tSUCCESS')
	    # print(1)
	else:
	    print("Invalid url")
	    print(valid)
	print('===============================')


