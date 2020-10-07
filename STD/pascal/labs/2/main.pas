PROGRAM by_Marina;

VAR X: array[0..4] of real = (-0.98, -0.5, 0.1, 0.5, 0.95);
    S, E, F: real;
    K, i: integer;

FUNCTION fact(x: integer): integer;
Var k: integer;
Begin
    k:= x - 1;
    while k > 1 do
    begin
        x:= x * k;
        k:= k - 1;
    end;
    fact:= x;
End;

FUNCTION pow(x: real; y: integer): real;
Begin
    {Что-то надо сделать...}
End;

BEGIN
    F:= 4.58342634; {при X = 0.5 контрольная формула будет равна 4.58342634}
    {E = 10e-2, 10e-4, 10e-6, 10-8}
    writeln('Введите точность E (10 в степени)');
    readln(E);
    
    {вывод тёплой шапки}
    writeln('| № |', ' X |', ' S(X) сумма ряда |', ' K |', ' F(X) к.ф. |', ' S(x) - F(X) |');
    {3, 4, 18, 4, 12, 14}

    for i:= 0 to 4 do
    begin
        S:= 0; 
        K:= 1;
        while S <= E do
        begin
            S:= S + ( (pow(X[i], (4*K-3)) * (4*K-X[i])) / (fact(4*K)) ) * pow(-1, K);
            K:= K + 1;
        end;
        writeln(' ', (i+1), ' ', X[i]:2:2, ' ', S:2:8, '     ', K:4, ' ', F, ' ', ' ', (S-F):2:8, ' ');
    end;
END.
