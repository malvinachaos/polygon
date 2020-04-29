VAR a: array[1..10] of integer;
    i, n, m, j, buf: integer;

BEGIN
    write('Введите размерность массива(минимум 2, максимум 10):');
    readln(n);

    writeln('Введите значения массива');
    for i:= 1 to n do
    begin
        write('a[', i, ']:=' );
        readln(a[i]);
    end;

    for i:= n downto 2 do
    begin
        m:= i;
        
        for j:= 1 to i-1 do
            if a[j] > a[m] then
                m:= j;
        buf:= a[i];
        a[i]:= a[m];
        a[m]:= buf;
        
    end;

    writeln('Вывод упорядочного массива');
    for i:= 1 to n do
        write(a[i], ' ');
END.
