from bs4 import BeautifulSoup as bs
import lxml.html
import json
import yaml
import sys
from colorama import Fore, Style
import re
from itertools import cycle


def hl(substrings, text):
    '''highlight substrings in text'''
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.MAGENTA]
    if not isinstance(substrings, list):
        substrings = [substrings]
    for ss, clr in zip(substrings, cycle(colors)):
        text = re.sub(
            r'({})'.format(ss),
            Style.BRIGHT + clr + r'\1' + Style.RESET_ALL,
            text, flags=re.I)
    return text


def showhtml(e):
    '''pretty print html fragment'''
    print(bs(lxml.html.tostring(e), 'lxml').prettify())


def dumpj(adict):
    print(json.dumps(adict, indent=1))


def dumpy(adict):
    d = json.loads(json.dumps(adict))
    yaml.dump(d, sys.stdout, default_flow_style=False, allow_unicode=True)
