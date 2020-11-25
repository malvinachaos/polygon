#! /bin/bash

name="main.pas"

while [ -n "$1" ]
do
    case $1 in
        "-h"|"--help")
            echo -e "building pascal program
Usage build.sh [-h] [-n] [-c N [name]] [-b] [-v] [-r]

-h --help \t \t output this text
-b --build \t \t compile to program, named 'program'
-v --verbose \t \t compilt with additional information
-r --remove \t \t remove 'program'
"
        shift
        ;;

        "-b"|"--build")
            fpc $name -oprogram.exe && rm -f *.o
        shift
        ;;

        "-v"|"--verbose")
            fpc -ved $name -oprogram.exe && rm -f *.o
        shift
        ;;

        "-r"|"--remove")
            rm -fv program.exe
        ;;
    esac
shift
done
