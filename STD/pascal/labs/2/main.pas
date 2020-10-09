PROGRAM by_Marina;

CONST F = 4.58342634; {при X = 0.5 контрольная формула будет равна 4.58342634}

VAR X: array[0..4] of real = (-0.98, -0.5, 0.1, 0.5, 0.95);
    S, E, a, X4: real;
    K, i, one: integer;

BEGIN
    {E = 10e-2, 10e-4, 10e-6, 10-8}
    writeln('Введите точность E (10 в степени)');
    readln(E);
    writeln(#10#13, E, #10#13);
    
    {вывод тёплой шапки}
    writeln('| № |   X   | S(X) сум ряда | K |  F(X) | S(x) - F(X) |');

    for i:= 0 to 4 do
    begin
        S:= 0; 
        K:= 1;
        a:= 0;
        one:= 1;
        X4:= X[i]*X[i]*X[i]*X[i];

        while a < E do
        begin
            K:= K + 1;
            a:= X4 * (4.0*K - X[i]);
            X4:= (4.0*(K-1)-X[i]);
            a:= a/X4;
            S:= S + (a * one);
            one:= one * (-1);
        end;
        if i >= 2 then
            writeln('| ', (i+1), ' |  ', X[i]:3:2, ' |   ', S:3:6, '    | ', K, ' | ', F:2:3, ' |  ', (S-F):2:6, '  |')
        else
            writeln('| ', (i+1), ' | ', X[i]:3:2, ' |   ', S:3:6, '    | ', K, ' | ', F:2:3, ' |  ', (S-F):2:6, '  |');
    end;
END.
