PROGRAM by_Marina;

USES sysutils;

TYPE onedim = array of integer;

VAR Af, Cf, out: text;
    A, C: onedim;
    n: integer;
    fexists: boolean;
    allargs: boolean;

PROCEDURE arr_i(var f: text; var x: onedim; n: integer);
Var i: integer;
Begin
    reset(f);
    setlength(x, n-1);

    for i:= 0 to n-1 do
        read(f, x[i]);

    close(f);
End;

PROCEDURE arr_o(var f: text; x: onedim; n: integer);
Var i: integer;
Begin
    for i:= 0 to n-1 do
        write(f, x[i], ' ');
End;

FUNCTION  find_num(x: onedim; y: onedim; n: integer):integer;
Var i, num: integer; mini: integer; chibi: integer;
Begin
    mini:= x[1] - y[1];
    for i:= 1 to n-2 do
    begin
        chibi:= x[i] - y[i];
        if (chibi < (x[i-1] - y[i-1])) and (chibi < (x[i+1] - x[i+1])) and (chibi < mini) then
        begin
            mini:= chibi;
            num:= i+1;
        end;
    end;
    find_num:= num;
End;

BEGIN
    fexists:= FileExists(argv[1]) and FileExists(argv[2]);
    allargs:= (argv[1] <> '') and (argv[2] <> '') and (argv[3] <> '');

    if allargs and fexists then
    begin
        assign(Af, argv[1]);
        assign(Cf, argv[2]);
        assign(out, argv[3]);
        rewrite(out);

        repeat
            write('Введите количество элементов(больше 2, но меньше 30): ');
            readln(n);
        until((2 < n) and (n < 50));

        arr_i(Af, A, n);
        write(out, 'Значения массива A:', #13#10);
        arr_o(out, A, n);

        arr_i(Cf, C, n);
        write(out, #13#10, #13#10, 'Значения массива C:', #13#10);
        arr_o(out, C, n);

        write(out, #13#10, #13#10, 'Номер наименьшего из значений A^2 - C^2:', #13#10);
        write(out, find_num(A, C, n));

        close(out);
    end
    else if (not allargs) then writeln(#13#10, 'Использование:', #13#10,
        './main file1.txt file2.txt [out_file.txt]')
    else if (not fexists) then writeln(#13#10, 'Один или оба файла не существуют')
END.
