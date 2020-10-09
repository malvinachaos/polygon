PROGRAM by_Marina;

VAR X: array[0..4] of real = (-0.98, -0.5, 0.1, 0.5, 0.95);
    S, E, F, a, X4: real;
    K, i, one: integer;

BEGIN
    F:= 4.58342634; {при X = 0.5 контрольная формула будет равна 4.58342634}
    {E = 10e-2, 10e-4, 10e-6, 10-8}
    writeln('Введите точность E (10 в степени)');
    readln(E);
    
    {вывод тёплой шапки}
    writeln('| № |', '   X   |', ' S(X) сумма ряда |', ' K |', ' F(X) к.ф. |', ' S(x) - F(X) |');
    {3, 4, 18, 4, 12, 14}

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
            one:= -one;
            a:= (X4 * (4.0*K - X[i]) ) / (4.0*(K-1)-X[i]) * one;
            S:= S + a;
        end;
        
        writeln('| ', (i+1), ' | ', X[i]:3:2, ' |   ', S:8:3, '   | ', K, ' | ', F:2:3, '   | ', (S-F):2:3, ' |');
    end;
END.
