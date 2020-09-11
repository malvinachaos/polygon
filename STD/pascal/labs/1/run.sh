#! /bin/sh

fpc half-circle_n_square.pas > log && ./half-circle_n_square || less log ; rm half-circle_n_square half-circle_n_square.o

rm log
