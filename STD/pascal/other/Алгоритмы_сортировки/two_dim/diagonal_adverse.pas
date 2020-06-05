VAR a:array[0..9, 0..9] of integer;
    i, k, j, n: integer;

BEGIN
    {Ввод данных}
    writeln('Введите размеры матрицы от 1 до 9(n)');
    read(n);

    writeln('Введите целочисленные значения');
    for i:= 0 to n do
        for j:= 0 to n do
        begin
            write('a[', i, ', ', j, ']= ');
            readln(a[i, j]);
        end;

    {Сортировка по побочной диагонали}
    for k:= 0 to n do
        for i:= 0 to n-1 do
            if a[i, n-i+1] < a[i+1, n-i] then
            begin
                a[i, n-i+1]:= a[i, n-i+1] + a[i+1, n-i];
                a[i+1, n-i]:= a[i, n-i+1] - a[i+1, n-i];
                a[i, n-i+1]:= a[i, n-i+1] - a[i+1, n-i];
            end;

    {Вывод}
    for i:= 0 to n do
    begin
        for j:= 0 to n do
            write(a[i, j], ' ');
        writeln();
    end;
END.

