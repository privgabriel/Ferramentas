#!/bin/bash

names=('Peter' 'Paul' 'Mary' 'David' 'Joe')
x=${#names[@]}

for ((i=0; i<$x; i++))
do
    echo ${names[$i]}
done
