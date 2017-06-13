#!/bin/python
# Clone each repository in the list file
import subprocess as sp
import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('list', help='path to repository list')
args = parser.parse_args()

with open(args.list, 'r') as f:
    for line in f:
        line = line.strip()

        # ignore lines commented with #
        if re.search('^\s*#', line) != None:
            continue

        # ignore empty lines
        if re.search('^\s*$', line) != None:
            continue

        # ignore lines that don't end with .git
        reponame = re.search('([^/]+)\.git$', line).group(1)
        if reponame == None:
            print('{} does not define a valid repo path\n'.format(line))
            continue

        print('{}: {}'.format(reponame, line))
        sp.run(['git', 'clone', line])
        print('')
