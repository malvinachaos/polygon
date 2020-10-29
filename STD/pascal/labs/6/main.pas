PROGRAM by_Marina;

USES sysutils;

TYPE one = array of integer;

VAR xf, otxt: text;
    i, n: integer;
    fexist: boolean;


PROCEDURE arr_i(var f: text; var x: one; n: integer);
Var i: integer;
Begin 
    reset(f);
    setlength(x, n);

    for i:= 0 to n do
        read(f, x);

    close(f);
End;


PROCEDURE arr_o(var f: text; var x: one; n: integer);
Var ;
Begin 

End;


BEGIN
	fexist:= FileExists(argv[1]);

    if fexist and (argv[1] <> '') and (argv[2] <> '') then
    begin
        repeat
            write('Введите количетво элементов массива от 2 до 50: ');
            readln(n);
        until (n > 2) and (n < 50);
        n:= n - 1;

    end
    else if (not fexist) then writeln('Файла ', argv[1], ' не существует')
    else writeln('Использование:', #13#10, './main file_1.txt out.txt');

END.
