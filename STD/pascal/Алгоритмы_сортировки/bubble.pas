VAR a:array[-10..9] of integer;
    i, j, n:integer;

{Данная программа сортирует элементы методом пузырька в порядке возрастания}
BEGIN
    writeln('Введите размер массива(максимум 9, минимум -9)');
    read(n);

    {Ввод данных}
    writeln('Введите целочисленные значения массива:');
    for i:= -10 to n do
        read(a[i]);

    {Сортировка}
    for i:= -10 to n do
    begin
        for j:= -10 to n-1 do
        begin
            if a[j] > a[j+1] then
            begin
                a[j]:= a[j] + a[j+1];
                a[j+1]:= a[j] - a[j+1];
                a[j]:= a[j] - a[j+1];
            end;
        end;
    end;

    {Вывод отсортированного массива}
    writeln('Вывод отсортированного массива');
    for i:= -10 to n do
        write(a[i], ' ');
END.
