import os
import re

import parsed_file
import tree


GLOBAL_INCLUDE_PATTERN = re.compile(r"#include\s*\<(?P<path>.*)\>")
LOCAL_INCLUDE_PATTERN = re.compile(r'#include\s*\"(?P<path>.*)\"')


def determine_global_path(filepath, globals):
    for gp in globals:
        if os.path.exists(os.path.join(gp, filepath)):
            return gp


def parsefile(root_dir, filename, globals=[]):
    node = tree.Node(parsed_file.ParsedFile(root_dir, filename))
    fullpath = os.path.join(root_dir, filename)
    if os.path.exists(fullpath):
        #TODO add some info if file coudn't be opened
        with open(fullpath) as fp:
            for line in fp:
                match = GLOBAL_INCLUDE_PATTERN.match(line)
                if match:
                    global_path = determine_global_path(match.group("path"), globals)
                    if global_path:
                        new_filepath = os.path.join(global_path, match.group("path"))
                        new_root = os.path.dirname(new_filepath)
                        new_filename = os.path.basename(new_filepath)
                    else:
                        new_root = "UNDETERMINED_ROOT"
                        new_filename = match.group("path")
                    node.add_child(parsefile(new_root, new_filename, globals))

                match = LOCAL_INCLUDE_PATTERN.match(line)
                if match:
                    new_filepath = os.path.join(root_dir, match.group("path"))
                    new_root = os.path.dirname(new_filepath)
                    new_filename = os.path.basename(new_filepath)

                    node.add_child(parsefile(new_root, new_filename, globals))
    return node

