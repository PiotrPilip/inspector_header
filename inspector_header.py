import argparse
import os

import header_parser
import tree


if __name__ == "__main__":
    aparser = argparse.ArgumentParser()
    aparser.add_argument("path_to_file")
    aparser.add_argument("-I", nargs="*", dest="additional_includes")

    args = aparser.parse_args()

    project_root = os.path.dirname(args.path_to_file)
    filename = os.path.basename(args.path_to_file)
    parsed_tree = header_parser.parsefile(project_root, filename, args.additional_includes)
    tree.print_tree(parsed_tree)
