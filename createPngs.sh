#!/bin/bash

# quit if anything fails
set -e

echo "Checking for required tools: Java and Graphviz's dot"
java --version
echo
dot -V
echo

createPngs(){
   echo "Processing dot files ..."
   find . -name "*.dot"  | while read F; do dot -O -Tpng $F; done
   echo "Processing uml files ... (this may take a while depending on the number of files)"
   java -jar plantuml.jar docs-*/uml/*.uml
}
createPngs

rmExtraFiles(){
  echo "Removing dot and uml files" 
  rm -f docs-*/dot/*.dot
  rm -f docs-*/uml/*.uml
}
rmExtraFiles

