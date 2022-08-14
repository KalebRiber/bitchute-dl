#!/usr/bin/env python3
import requests
import sys
from time import time
import downloadFile
import console
from textColour import OUTPUT_CLR

base_url = "https://www.bitchute.com"
search_for = "<source src=\"https://seed"
argument_bcurl = "--bcurl"

browse = requests.Session()

help_mesg = '''
Usage: {0}{1} {2}{3} {4}bitchute.com/video/...
'''.format(OUTPUT_CLR.blue_bold, sys.argv[0], OUTPUT_CLR.green, argument_bcurl, OUTPUT_CLR.white)

parser = console.Utils()
video_url = parser.ParseBitChuteURL(base_url, parser.ParseArgumentLine(argument_bcurl))
if(video_url == None):
    print('{0}[!] {1}no valid URL found'.format(OUTPUT_CLR.red, OUTPUT_CLR.red_bold))
    print(help_mesg)
    sys.exit()

print('{0}[*] {1}BitChute video URL: {2}{3}'.format(OUTPUT_CLR.blue, OUTPUT_CLR.green, OUTPUT_CLR.white, video_url))
print('{0}[*] {1}Downloading and reading web page...'.format(OUTPUT_CLR.blue, OUTPUT_CLR.green))

page_req = browse.get(video_url)
page = page_req.text

if page_req.status_code != 200:
    print('{0}[!] {1}Error downloading the page'.format(OUTPUT_CLR.red, OUTPUT_CLR.red_bold))
    sys.exit()

del page_req
video_to_download = (page[(page.find(search_for) + 0xD):]).split("\"")[0]
video_title = page[(page.find("<ti") + 7):].split("</t")[0].replace("\r\n", ' ')
del page, search_for

print('{0}[*] {1}Downloading {2}\"{3}\" {4}from: {5}{6}'.format(OUTPUT_CLR.blue, OUTPUT_CLR.green, OUTPUT_CLR.blue_bold, video_title, OUTPUT_CLR.green, OUTPUT_CLR.white, video_to_download))

now = time()
if not downloadFile.GET(browse, video_to_download, video_title):
    print("{0}[!] {1}Invalid response from server".format(OUTPUT_CLR.red_bold, OUTPUT_CLR.red))
    browse.close()
    del browse, now, argument_bcurl, parser
    sys.exit()

finish = int(time() - now)

print('{0}[*] {1}Finished downloading in {2} seconds'.format(OUTPUT_CLR.blue, OUTPUT_CLR.green, finish))

browse.close()
del browse, now, finish, argument_bcurl, parser
