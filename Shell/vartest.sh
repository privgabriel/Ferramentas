#!/bin/bash

num1=$1
num2=17

if [ $num1 -ge $num2 ]
then
  echo "$num1 is greater than or equal to $num2"
else
  echo "$num1 is less than $num2"
fi

echo "Sum is $((num1 + num2))"
