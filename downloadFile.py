#!/usr/bin/env python3
import requests
from requests import ConnectionError
from textColour import OUTPUT_CLR

def GET(session, url, video_title):
    downloaded_bytes_amount = 0
    try:
        with session.get(url, stream=True) as r:
            try:
                file_size = r.headers['Content-Length']
            except KeyError:
                return False
            r.raise_for_status()
            with open(video_title + ".mp4", 'wb') as f:
                for chunk in r.iter_content(chunk_size=(8 * 1024)):
                    f.write(chunk)
                    downloaded_bytes_amount += len(chunk)
                    print('\033[A{0}[*] {1}{2:.2f}/{3:.2f}kb {4}downloaded...'.format(OUTPUT_CLR.green_bold, OUTPUT_CLR.blue, float(downloaded_bytes_amount)/1024, float(file_size)/1024, OUTPUT_CLR.green))
            del downloaded_bytes_amount, f, chunk, file_size
            return True
    except ConnectionError:
        print("{0}[!] {1}Error during connection.".format(OUTPUT_CLR.red_bold, OUTPUT_CLR.red))
