#!/usr/bin/env python3
import sys

class Utils:
    def __init__(self):
        return None

    def ParseArgumentLine(self, bitchute_url):
        index = ""
        for argument in sys.argv:
            if index == bitchute_url:
                del bitchute_url, index
                return argument
            index = argument
        return None

    def ParseBitChuteURL(self, bitchute_base_url, www):
        if (type(www) != str):
            www = str(www)
        index = www.find(bitchute_base_url[12:])
        if index == -1:
            return None
        www = bitchute_base_url[:12] + www[index:]
        del index
        return www
