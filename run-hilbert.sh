#!/bin/bash

echo "Running rivet on files, wish you patience!"


for file in *.txt; do

	echo "rivet for " $file " .."
	rivet_console $file --betti -H 1 -x 50 -y 50 > hil_$file
	echo "--"
done 

echo "done!"

