PROGRAM by_Marina;

VAR x, S, E, a, X4, F: real;
    K, one: integer;

BEGIN
    {E = 10e-2, 10e-4, 10e-6, 10-8}
    write('Введите точность E (10 в степени): ');
    readln(E);
    writeln(#10#13, E, #10#13);

    write('Введите значение x: ');
    readln(x);
    
    {вывод тёплой шапки}
    writeln('|   X   | S(X) сум ряда | K |  F(X) | S(x) - F(X) |');

    S:= 0; 
    K:= 1;
    a:= 0;
    one:= 1;
    X4:= x*x*x*x;
    F:= (2 - sin(x) - cos(x) - exp(-x)) / (2*x*x);

    while a < E do
    begin
        K:= K + 1;
        a:= X4 * (4.0*K - x);
        X4:= (4.0*(K-1) - x);
        a:= a/X4;
        S:= S + (a * one);
        one:= one * (-1);
    end;

    writeln('| ', X:4:2, ' |   ', S:3:6, '    | ', K, ' | ', F:2:3, ' |  ', (S-F):2:6, '  |')
END.
