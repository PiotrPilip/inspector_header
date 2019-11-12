import os
import re

import parsed_file
import tree


BRACKET_INCLUDE_PATTERN = re.compile(r"#include\s*\<(?P<path>.*)\>")
QUOTES_INCLUDE_PATTERN = re.compile(r'#include\s*\"(?P<path>.*)\"')


def process_global_include(filepath, globals):
    global_path = next((gp for gp in globals if os.path.exists(os.path.join(gp, filepath))), None)
    if global_path is not None:
        return os.path.join(global_path, filepath)
    else:
        return None


def process_local_include(filepath, local_path):
    result = os.path.join(local_path, filepath)
    if os.path.exists(result):
        return result


def parsefile(root_dir, filename, globals=[]):
    node = tree.Node(parsed_file.ParsedFile(root_dir, filename))
    fullpath = os.path.join(root_dir, filename)
    if os.path.exists(fullpath):
        #TODO add some info if file coudn't be opened
        #TODO handle circular includes
        with open(fullpath) as fp:
            for line in fp:
                match = BRACKET_INCLUDE_PATTERN.match(line)
                if match:
                    result = process_global_include(match.group("path"), globals)
                    if result is None:
                        result = process_local_include(match.group("path"), root_dir)
                    if result is None:
                        result=os.path.join("UNDETERMINED_PATH", match.group("path"))
                match = QUOTES_INCLUDE_PATTERN.match(line)
                if match:
                    result = process_local_include(match.group("path"), root_dir)
                    if result is None:
                        result = process_global_include(match.group("path"), globals)
                    if result is None:
                        result=os.path.join("UNDETERMINED_PATH", match.group("path"))
                if result is not None:
                    file_dir = os.path.dirname(result)
                    file_name = os.path.basename(result)
                    node.add_child(parsefile(file_dir, file_name, globals))

    return node

