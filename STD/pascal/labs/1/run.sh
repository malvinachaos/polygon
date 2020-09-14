#! /bin/sh

fpc half-circle_n_square.pas > log && ./test.py|| less log ; rm half-circle_n_square half-circle_n_square.o

rm log
