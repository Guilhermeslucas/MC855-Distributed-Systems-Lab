#!/usr/bin/env python3
import subprocess
import pyspark

train_input = subprocess.Popen(['./catter.sh', 'train'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')

for line in train_input.split('\n'):
    print(line)
