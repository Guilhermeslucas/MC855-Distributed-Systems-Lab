#!/usr/bin/env python3

import sys

repo_link = 'https://github.com'
for line in sys.stdin:
    final = repo_link + line
    print(final, end='')
