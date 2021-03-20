#! /bin/bash
read -p "Input number of tests = " n
for i in $(seq 1 $n)
do
    echo $i | python3 12.py >> logfile.log
    echo -ne "$i\r"
done
