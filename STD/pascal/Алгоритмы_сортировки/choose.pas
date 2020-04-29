VAR a: array[1..10] of integer;
    i, n, m, j: integer;

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
        begin
            if a[i] < a[m] then
            begin
                m:= j;
                a[i]:= a[i]+a[m];
                a[m]:= a[i]-a[m];
                a[i]:= a[i]-a[m];
            end
        end
    end;

    writeln('Вывод упорядочного массива');
    for i:= 1 to n do
        write(a[i], ' ');
END.
