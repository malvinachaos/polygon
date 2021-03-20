#! /bin/bash
read -p "Input count of test = " n

log="Shine_On_You_Crazy_Diamond.log"
echo -ne > $log

for i in $(seq 1 $n)
do
    echo $i | python3 15.py >> $log
    echo -ne "\n\n" >> $log
done
