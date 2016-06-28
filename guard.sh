#!/usr/bin/bash
#
# run make whenever something (anything, really) changes in the directory
# needs inotifywait which is in
# $ apt-get install inotify-tools
while [ 1 ] ;  do
  inotifywait -e close_write,moved_to,create  . |
  while read -r directory events filename; do
    echo ">> GUARD: running make"
    make
  done
done
