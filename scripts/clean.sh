#!/bin/sh

day2=$(date  --date="2 days ago" +"%Y-%m-%d")

find . -name "${day2}_*.log" -exec rm -rf {} \;