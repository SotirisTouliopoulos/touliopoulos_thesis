#!/bin/bash

for file in *.pdb ; do

    solvate -bulk ${file:0:4} ${file}.water
    mv ${file}.water.pdb ${file}.water

done
