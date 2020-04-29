VAR a: array[1..10, 1..10] of integer;
    n, m, i, j, k:integer;

BEGIN
    {ввод}
    writeln('Введите размеры матрицы(n, m от 1 до 10)');
    read(n, m);

    writeln('Введите значения для массива: ');
    for i:= 1 to n do
    begin
        for j:= 1 to m do
        begin
            write('a[', i, ', ', j, ']:= ');
            read(a[i, j]);
        end;
        writeln();
    end;

    {Сама сортировка}
    for i:= 1 to n do
        for k:= 1 to m do
            for j:= 1 to m-1 do
                if a[i, j] > a[i, j+1] then
                begin
                    a[i, j]:= a[i, j] + a[i, j+1];
                    a[i, j+1]:= a[i, j] - a[i, j+1];
                    a[i, j]:= a[i, j] - a[i, j+1];
                end;

    {Вывод массива}
    for i:= 1 to n do
    begin
        for j:= 1 to m do
            write(a[i, j], ' ');
        writeln();
    end;
END.
