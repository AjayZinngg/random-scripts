#!/bin/sh
d=$1

awk '{for(i=0;i<=NF;i++) if (tolower($i)=="thy") print $(i+1)}' $d | tr '[,.?;:@#$%^&*()\t\r\f]' '[\n*]'| grep -v "^\s*$" | sort |uniq -c | sort -bnr

