PROGRAM by_Marina;

USES sysutils;

TYPE one = array of integer;

VAR xf, otxt: text;
    i, n: integer;
    a: one;
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
Var i: integer;
Begin 
    append(f);
    for i:= 0 to n do
        write(f, ' ');
    writeln(f, #13#10);
End;


PROCEDURE find_num(var f: text, var x: one; n, t1, t2: integer);
Var i, j: integer;
    flg: boolean;
Begin
    writeln(f, 'Значения массива:', #13#10);
    arr_o(f, x, n);


    writeln(f, #13#10, #13#10);
    close(f);
End;

BEGIN
	fexist:= FileExists(argv[1]);

    if fexist and (argv[1] <> '') and (argv[2] <> '') then
    begin
        assign(xf, argv[1]);
        assign(otxt, argv[2]);

        repeat
            write('Введите количетво элементов массива от 2 до 50: ');
            readln(n);
        until (n > 2) and (n < 50);
        n:= n - 1;

        write('Введите значения для t1 и t2 соответственно: ');
        readln(t1, t2);

        arr_i(xf, a, n);
        find_num(otxt, a, n, t1, t2);

    end
    else if (not fexist) then writeln('Файла ', argv[1], ' не существует')
    else writeln('Использование:', #13#10, './main file_1.txt out.txt');

END.
