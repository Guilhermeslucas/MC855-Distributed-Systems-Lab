#!/bin/sh

output="$(~/Documentos/Unicamp/MC855/hadoop-2.7.4/bin/hdfs dfs -cat /data/year-prediction-msd-test.txt)"

for line in $output
do
    echo $line
done

