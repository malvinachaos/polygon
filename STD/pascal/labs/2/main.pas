PROGRAM by_Marina;

VAR x, S, E, a, X4, F: real;
    K, one, iE: integer;

BEGIN
    repeat
        write('Введите точность E, (-1;0) U (0;1]: ');
        readln(E);
    until ( (-1 < E) and (E < 0) or (0 < E) and (E <= 1));

    iE:= trunc(ln(round(1/E))/ln(10)); {данный код вычисляет степень для 1/E}

    write('Введите значение x: ');
    readln(x);
    
    S:= 0; 
    K:= 0;
    a:= x * (4 - x) / 24;
    X4:= x*x*x*x;
    F:= (2 - sin(x) - cos(x) - exp(-x)) / (2*x*x);

    while (a < E) and (K < 100) do
    begin
        S:= S + a;
        K:= K + 1;
        a:= - a * (X4 * (4.0*K - x)) / (4.0*(K-1) - x);
    end;

    writeln(
            'X = ', X:4:iE, #10#13,
            'Cумма ряда S(X) = ', S:(3+iE):iE, #10#13,
            'Количество потребовавшихся итераций K = ', K, #10#13,
            'Результат вычисления контрольной формулы F(x) = ', F:(2+iE):iE, #10#13,
            'S(X) - F(X) = ', (S-F):(2+iE):iE
          );
END.
