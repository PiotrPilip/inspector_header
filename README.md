# Inspector Header
Command line tool written in python for printing out the tree of files
 included with `#include` preprocessor directives in C and C++
 
 Work in progress - project still needs some refinement and additional features
 
## Usage
 `python inspector_header path_to_file [-I additional_include_directory1, additional_include_directory2...]`
 
 `path_to_file` is full path to file you want to inspect
 `-I` lets you specify global/additional include directories where you search for include files in your project
