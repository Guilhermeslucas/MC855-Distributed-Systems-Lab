#!/usr/bin/env python3
import subprocess
import pyspark
from pyspark import SparkConf, SparkContext

conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app")
         .set("spark.executor.memory", "1g"))

sc = SparkContext(conf = conf)

train_input = subprocess.Popen(['./catter.sh', 'train'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')

data = sc.textFile(train_input).map(lambda line: line.split(",")).collect()

for line in data:
    print(line)
    break    
