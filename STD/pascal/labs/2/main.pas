PROGRAM by_Marina;

VAR x, S, E, a, X4, F: real;
    K, one, iE: integer;

BEGIN
    repeat
        write('Введите точность E, (0;1]: ');
        readln(E);
        write('Введите значение x, (-1;1): ');
        readln(x);
    until ((0 < E) and (E < 1)) and ((x > -1) and (x < 1));

    iE:= trunc(ln(round(1/E))/ln(10)); {данный код вычисляет степень для 1/E}

    a:= (x * (4 - x)) / 24;
    S:= a; 
    K:= 2;
    X4:= x*x*x*x;
    F:= (2 - sin(x) - cos(x) - exp(-x)) / (2*x*x);

    while (abs(a) > E) do
    begin
        K:= K + 1;
        a:= a * ((-1) * ((X4 * (4*K - x)) / (4*K * (4*(K - 1) - x))));
        S:= S + a;
        writeln
        (
            '======[', K:2, ']======', #10#13, 
            'S = ', S:(3+iE):iE, #10#13,
            'a = ', a:(3+iE):iE, #10#13,
            '================', #10#13
        );
    end;

    writeln(
            'X = ', X:4:iE, #10#13,
            'Cумма ряда S(X) = ', S:(3+iE):iE, #10#13,
            'Количество потребовавшихся итераций K = ', K, #10#13,
            'Результат вычисления контрольной формулы F(x) = ', F:(2+iE):iE, #10#13,
            'S(X) - F(X) = ', (S-F):(2+iE):iE
          );
END.
