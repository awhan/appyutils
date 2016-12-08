from bs4 import BeautifulSoup as bs
import lxml.html
import json
import yaml
import sys


def showhtml(e):
    '''pretty print html fragment'''
    print(bs(lxml.html.tostring(e), 'lxml').prettify())


def dumpj(adict):
    print(json.dumps(adict, indent=1))


def dumpy(adict):
    d = json.loads(json.dumps(adict))
    yaml.dump(d, sys.stdout, default_flow_style=False, allow_unicode=True)
