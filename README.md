# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

Bookbot that counts characters and words on a book

# Instructions for use

Usage: python3 main.py <path_to_book> [flag]
Unflagged use analyses alphabetical characters
Valid flags: '--non-alpha', '--nalpha', '--na': analyses non alphabetical 
'path_to_book' is a path to a text file, relative to the folder where main.py and stats.py are located, and typicaly books/bookname.txt

# Project folder and file strutcure
The files main.py and stats.py contain the executed code

The folder code_blocks_for_reference contains non executed files with code snippets that I wrote to figure out the needed functionality

# Dependencies

Python 3.13.5

# An addendum

While making the project, I didn't know you could analyse strings directly and didn't know I could turn strings into lists with list(), so I coded a very ineficient way to turn the string into a list so I could analyze it

