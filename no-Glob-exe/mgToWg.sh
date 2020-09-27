#!/usr/bin/env bash

#Transfer multi grapgh too weighted graph 
NewName=$(echo "$1" | sed 's/.*\.\(.*\)/\1.test/g')
 awk '$1 > $2 { print $2,  $1 ; next } {print $1, $2}' $1 |
 sort |
uniq -c |
awk '{print $2, $3, $1}' > "$NewName"
