#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : manage.py
# Author             : Podalirius (@podalirius_)
# Date created       : 6 Aug 2022

import argparse
import json
import glob

import jinja2


def find_and_parse():
    awesome_rce_techniques = {}
    for path_to_json_file in glob.glob("../../*/*/techniques/*/technique.json"):
        f = open(path_to_json_file, 'r')
        data = json.loads(f.read())
        f.close()
        path = path_to_json_file.lstrip('./').split('/')
        if path[0] not in awesome_rce_techniques.keys():
            awesome_rce_techniques[path[0]] = {}
        if path[1] not in awesome_rce_techniques[path[0]].keys():
            awesome_rce_techniques[path[0]][path[1]] = {}
        if path[3] not in awesome_rce_techniques[path[0]][path[1]].keys():
            awesome_rce_techniques[path[0]][path[1]][path[3]] = data
    return awesome_rce_techniques


def generate_readme(awesome_rce_techniques: dict):
    f = open("./templates/main_README.md.jinja2", 'r')
    main_template = jinja2.Template(f.read())
    f.close()

    f = open("./templates/category_README.md.jinja2", 'r')
    category_template = jinja2.Template(f.read())
    f.close()

    # Counting total number of techniques
    nb_rce_techniques = 0
    for category in awesome_rce_techniques.keys():
        for software in awesome_rce_techniques[category].keys():
            for technique in awesome_rce_techniques[category][software].keys():
                nb_rce_techniques += 1

    # Generating readme
    print("[>] Generating 'README.md'")
    f = open('../../README.md', 'w')
    f.write(main_template.render(
        nb_rce_techniques=nb_rce_techniques,
        awesome_rce_techniques=awesome_rce_techniques,
        fct_sorted=sorted,
        fct_len=len
    ))
    f.close()

    # Generating category readmes
    for category in awesome_rce_techniques.keys():
        print("[>] Generating '%s/README.md'" % category)
        f = open('../../%s/README.md' % category, 'w')
        f.write(category_template.render(
            category=category,
            awesome_rce_techniques=awesome_rce_techniques,
            fct_sorted=sorted,
            fct_len=len
        ))
        f.close()
    print("[+] All done!")


def parseArgs():
    parser = argparse.ArgumentParser(description="Description message")
    parser.add_argument("-a", "--arg", default=None, help='arg1 help message')
    parser.add_argument("-v", "--verbose", default=False, action="store_true", help='Verbose mode. (default: False)')
    return parser.parse_args()


if __name__ == '__main__':
    options = parseArgs()

    awesome_rce_techniques_data = find_and_parse()
    generate_readme(awesome_rce_techniques_data)

