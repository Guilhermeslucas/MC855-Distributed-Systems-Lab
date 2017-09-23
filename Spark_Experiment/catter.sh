#!/bin/sh

if [ $1 = "test" ] 
then
    output="$(~/Documentos/Unicamp/MC855/hadoop-2.7.4/bin/hdfs dfs -cat /data/year-prediction-msd-test.txt)"
elif [ $1 = "train" ]
then
    output="$(~/Documentos/Unicamp/MC855/hadoop-2.7.4/bin/hdfs dfs -cat /data/year-prediction-msd-train.txt)"
else
    echo "Not a valid option. Run ./catter.sh test or /catter.sh train"
    exit
fi

for line in $output
do
    echo $line
done
