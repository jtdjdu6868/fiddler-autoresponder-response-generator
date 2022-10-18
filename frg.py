import os
import sys
import configparser

inputfilename = sys.argv[1].strip('"')
outputfilename = sys.argv[2].strip('"')

body = open(inputfilename, 'rb')
output = open(outputfilename, 'wb')
header = open('basic_header.txt')
config = configparser.ConfigParser()
config.read('mimetype.ini')


ext = os.path.splitext(inputfilename)[1]
mimetype = config['DEFAULT'].get(ext, 'text/plain') if len(sys.argv) <= 3 else sys.argv[3]
output.write(bytes(header.read() % (mimetype, os.stat(inputfilename).st_size), 'utf-8'))
output.write(body.read())
