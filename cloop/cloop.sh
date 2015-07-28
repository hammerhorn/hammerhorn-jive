echo -n "%"
while read $SCRIPT_SOURCE_LINE
  do [[ $(echo "$SCRIPT_SOURCE_LINE"|cut -d' ') == "#include" ]]\
     && 
