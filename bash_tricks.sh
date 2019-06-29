#!/usr/bin/env bash

# vi tricks

## add leading commas for each line

::%s/^/,/g

## add trailing commas for each line

:%s/$/,/g

## make N lines into 1 line with commas delimited

:%s/\n/,/g

#1
#2
#3

#into

#1,2,3,

#reference: https://stackoverflow.com/questions/6577508/how-to-merge-multiple-lines-into-one-line-in-vim
