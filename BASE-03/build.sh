#! /bin/bash

name="main.pas"

while [ -n "$1" ]
do
    case $1 in
        "-h"|"--help")
            echo -e "building pascal program
Usage build.sh [-h|--help] [-b|--build] [-v|--verbose] [--run] [--remove]

-h --help \t \t output this text
-b --build \t \t compile to program
--run \t \t start compiled program
-v --verbose \t \t compilt with additional information
-r --remove \t \t remove program
"
        ;;

        "-b"|"--build")
            fpc $name -oprogram.exe  && rm -f *.o
        ;;

        "--run")
            ./program.exe
        ;;

        "-v"|"--verbose")
            fpc -ved $name -oprogram.exe  && rm -f *.o
        ;;

        "-r"|"--remove")
            rm -fv program.exe
        ;;
    esac
shift
done
