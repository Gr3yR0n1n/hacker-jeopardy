#!/usr/bin/python

# Copyright Skullspace, 2014
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved. This file is offered as-is,
# without any warranty.
# http://www.gnu.org/prep/maintain/html_node/License-Notices-for-Other-Files.html
# @author Mark Jenkins <mark@markjenkins.ca>

from pickle import dump, load
from os.path import exists

PERSIST_FILE = 'board.pickle'

if not exists(PERSIST_FILE):
    board = { (i,j): False
              for i in range(2)
              for j in range(2)
            }
else:
    with open(PERSIST_FILE) as f:
        board = load(f)

print 'before', board


x = int(raw_input("flip x> "))
y = int(raw_input("flip y> "))

board[ (x, y) ] = not board[ (x, y) ]

print 'after', board

with open(PERSIST_FILE, 'w') as f:
    dump(board, f)


