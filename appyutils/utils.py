from bs4 import BeautifulSoup as bs
import lxml.html
import json
import yaml
import sys
from colorama import Fore, Style
import re
from itertools import cycle
import pandas as pd
import numpy as np

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


def dumpj(d: dict):
    print(json.dumps(d, indent=1))


def dumpy(d: dict):
    yaml.dump(d, sys.stdout, default_flow_style=False, allow_unicode=True)


def random_df():
    return pd.DataFrame(np.random.randint(1, 10, (10, 4)),
                        columns=list('abcd'))
