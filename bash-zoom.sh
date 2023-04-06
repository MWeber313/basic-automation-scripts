#! /opt/devkitpro/msys2/usr/bin/bash
read -p "Write the path to the file you wish to execute " a

var=`py $a`
echo $var