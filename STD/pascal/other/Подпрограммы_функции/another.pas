VAR a,b,c: real;
    k: shortint;

FUNCTION fun(x, y: real; var k: shortint): real;
    Begin
        k:= 0;
        if x > 0 then
            fun:= exp(y*ln(x));
        
        if x = 0 then
            fun:= 0;

    End;

BEGIN
    while true do
    begin
        write('Введите а: ');
        read(a);
        if a > 0 then
            break;
        writeln('Число может быть только положительным');
    end;

    write('Введите b: ');
    read(b);

    c:= fun(a, b, k);
    writeln('c = ', c:10:3);
END.
