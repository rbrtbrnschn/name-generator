#!/usr/bin/env bash

PATH="/usr/local/bin"
/usr/bin/sudo rm -rf $PATH/name-gen $PATH/name-generator
/usr/bin/sudo /usr/bin/cp -a $PWD $PATH/name-generator
/usr/bin/sudo cp -a $PWD/name-gen $PATH/name-gen
