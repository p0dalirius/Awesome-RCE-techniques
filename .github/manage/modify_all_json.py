#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : modify_all_json.py
# Author             : Podalirius (@podalirius_)
# Date created       : 6 Aug 2022

import json
import glob
import os


def find_techniques_and_apply_modifiers(modifiers):
    for path_to_json_file in glob.glob("../../*/*/techniques/*/technique.json"):
        f = open(path_to_json_file, 'r')
        data = json.loads(f.read())
        f.close()

        f = open(os.path.dirname(path_to_json_file) + os.path.sep + 'README.md', 'r')
        readme = f.read()
        f.close()

        # Do stuff
        for fct_modifier in modifiers:
            data = fct_modifier(data, readme)

        # Write
        f = open(path_to_json_file, 'w')
        f.write(json.dumps(data, indent=4))
        f.close()


def add_references(data, readme):
    readme = readme.strip()
    if "## References" in readme:
        data["references"] = []
        references = readme.split("## References")[-1].split('\n')
        for ref_line in references:
            if "http" in ref_line:
                ref_line = 'http' + ref_line.split('http', 1)[1].strip()
                data["references"].append(ref_line)
    return data


def add_work_in_progress(data, readme):
    data["work_in_progress"] = False
    return data


if __name__ == '__main__':

    modifiers = [add_work_in_progress, add_references]

    find_techniques_and_apply_modifiers(modifiers)
