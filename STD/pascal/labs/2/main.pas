PROGRAM by_Marina;

VAR x, S, E, a, X4, F: real;
    K, one, iE: integer;

BEGIN
    write('Введите точность E (10 в степени): ');
    readln(E);
    iE:= trunc(ln(round(1/E))/ln(10)); {данный код вычисляет степень для 1/E}

    write('Введите значение x: ');
    readln(x);
    
    {вывод шапки}
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

    writeln('| ', X:4:2, ' |   ', S:(3+iE):iE, '    | ', K, ' | ', F:(2+iE):iE, ' |  ', (S-F):(2+iE):iE, '  |')
END.
