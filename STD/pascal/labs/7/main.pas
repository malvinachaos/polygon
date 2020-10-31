PROGRAM by_Marina;

USES sysutils;

TYPE twodim = array of array of integer;

VAR a: twodim;
    matfile, otxt: text;
    m, n:integer;
    aexist, fexist: boolean;

PROCEDURE matrix_i(var f: text; var x: twodim; m, n: integer);
Var i, j, c: integer;
{log} k: integer;
Begin 
    reset(f);
{log} writeln('check input');
{log} k:= 1;
    for i:= 0 to m do
    begin
        for j:= 0 to n do
        begin
            read(f, x[i, j]);
{log} write('[', i, 'x', j, ']', ' ', x[i, j], '    ');
{log} if (k mod 10 = 0) then writeln();
{log} k:= k + 1;
        end;

        while not seekeoln(f) do read(f, c);
    end;

    close(f);
End;

PROCEDURE fnd(var f: text; var x: twodim; m, n: integer);
Var i, j, sum: integer;
    k: byte;
    flg: boolean;
Begin
    flg:= false;
{log} writeln('check output');
    writeln(f, 'Номера строк матрицы:');
    for i:= 0 to m do
    begin
        sum:= 1;
        k:= 0;

        for j:= 0 to n do
            sum:= sum + x[i, j];
        
        if sum < 0 then
        begin
            flg:= true;
            write(f, i, '      ');
            if (k mod 4 = 0) then writeln(f);
            k:= k + 1;
        end;
{log} writeln('Good');
    end;

    if not flg then writeln(f, 'Не найдено');
End;

BEGIN
    fexist:= FileExists(argv[1]);
    aexist:= (argv[1] <> '') and (argv[2] <> '');

    if fexist and aexist then
    begin
        assign(matfile, argv[1]);
        assign(otxt, argv[2]);
        rewrite(otxt);

        repeat
            write('Введите размерность матрицы A(сначала кол-во строк, потом столбцов, от 2 до 100): ');
            readln(m, n);
        until (m >= 2) and (m <= 100) and (n >= 2) and (n <= 100);
        n:= n - 1;
        m:= m - 1;
        setlength(a, m, n);

        matrix_i(matfile, a, m, n);
        fnd(otxt, a, m, n);
    end
    else if not fexist then writeln('Файла ', argv[1], ' не существует')
    else if not aexist then writeln('Использование:', #13#10, './main file.txt out.txt');

    close(otxt);

END.
