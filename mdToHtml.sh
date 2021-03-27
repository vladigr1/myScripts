#!/usr/bin/env bash

#mark-down to html better way to export it
htmlName=$(echo "$1" | sed 's/\(.*\)\..*/\1.html/g')
markdown-it.cmd "$1" -o "temp.html" 
cat /c/Users/do2vl/source/myScripts/share/mdToHtml/code/header.txt "temp.html" /c/Users/do2vl/source/myScripts/share/mdToHtml/code/footer.txt > "$htmlName"
cp /c/Users/do2vl/source/myScripts/share/mdToHtml/main.css ./
rm "temp.html"
