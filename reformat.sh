#!/bin/bash

PWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
FILE="$HOME/.names.txt"
CATFISH=$(cat $FILE | tr -d '[],')
ARR=( )
for NAME in $CATFISH
do
	NAME=${NAME:1:-1}
	ARR+="$NAME " 
done
echo ${ARR[@]}
