#!/usr/bin/python
# coding: UTF-8

import os
import urllib.request
import json
import codecs
import datetime
import pathlib

import xmltodict


# - - - - - - - - - - - - - - - - - - - -
# Const, Enum
# - - - - - - - - - - - - - - - - - - - -
_XML_URL = 'http://www.data.jma.go.jp/developer/xml/feed/regular_l.xml'
_JSON_DIR = 'json'
_FILE_NUM_MAX = 12



# - - - - - - - - - - - - - - - - - - - -
# Functions - XML / JSON
# - - - - - - - - - - - - - - - - - - - -
def open_xml(url):
    res = None
    req = urllib.request.Request(url)

    try:
        resp = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read()) 
    else:
        res = resp.read()

    return res


def xml2json_file(xml, path):
    dict = xmltodict.parse(xml)

    file = codecs.open(path, 'w', 'utf-8')
    json.dump(dict, file, ensure_ascii=False, indent=4,)

    return



# - - - - - - - - - - - - - - - - - - - -
# Functions - File
# - - - - - - - - - - - - - - - - - - - -
def create_dir():
    dir = os.path.join(os.getcwd(), _JSON_DIR)

    if not os.path.isdir(dir):
        os.makedirs(dir)

    return dir


def create_file(dir, xml):
    """
    date_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = '{0}-{1}.{2}'.format(os.path.basename(_XML_URL).split('.', 1)[0],
                                                date_str,
                                                'json')
    """
    filename = '{0}.{1}'.format(os.path.basename(_XML_URL).split('.', 1)[0], 'json')
    file_path = os.path.join(dir, filename)
    xml2json_file(xml, file_path)


"""
def rotation_file(dir):
    path = pathlib.Path(dir)
    files = path.glob('*.json')

    sorted_files = sorted(files, reverse=True)
    file_cnt = 0

    for file in sorted_files:
        file_cnt += 1

        if file_cnt > _FILE_NUM_MAX:
            file.unlink()
            continue

    return
"""


# - - - - - - - - - - - - - - - - - - - -
# Functions - Main
# - - - - - - - - - - - - - - - - - - - -
def main():
    xml = open_xml(_XML_URL)

    if xml is None:
        print("error xml open.")
        return


    dir = create_dir()

    create_file(dir, xml) 

    # rotation_file(dir)

    
if __name__ == '__main__':
    main()
