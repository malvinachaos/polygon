PROGRAM by_Marina;

TYPE
    onedim = array[1..30] of integer;

VAR n, i: integer;
    sum: longint = 0;
    k: integer = 0;
    Xtxt, Ytxt: text;
    otxt: text;
    X, Y: onedim;

BEGIN
    assign(Xtxt, 'inX.txt');
    assign(Ytxt, 'inY.txt');
    assign(otxt, 'out.txt');
    reset(Xtxt);
    reset(Ytxt);
    rewrite(otxt);

    repeat
        write('Введите количество элементов(не больше 30): ');
        readln(n);
    until (n >= 2) and (n <= 30);


    for i:= 1 to n do
    begin
        read(Xtxt, X[i]);
        read(Ytxt, Y[i]);
        
        if (X[i] > 0) and (X[i] > Y[i]) then
        begin
            sum:= sum + X[i];
            k:= k + 1;
        end;
    end;

    write(otxt, sum);
    write(otxt, ' ');
    write(otxt, k);

    close(Xtxt);
    close(Ytxt);
    close(otxt);
END.
