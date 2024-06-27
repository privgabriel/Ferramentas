#!/bin/bash
runs=6
while [ $runs -gt 0 ]
do
    echo "Run down at number $runs"
    let runs=runs-1
done
until [ $runs -gt 6 ]
do
    echo "Run up at number $runs"
    let runs=runs+1
done
