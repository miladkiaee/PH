#!/bin/bash

echo "Running rivet on files, wish you patience!"


for file in *; do

	echo "rivet for " $file " .."
	../rivet_console $file $file".mif" -x 50 -y 50 -H1
	echo "--"
done 

echo "done!"

