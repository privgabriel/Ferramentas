#!/bin/bash
if [ -d $1 ]
then
    echo "$1 exists"
    ls $1
else
    echo "$1 does not exist"
fi