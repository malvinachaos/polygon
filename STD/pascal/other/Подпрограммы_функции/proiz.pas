TYPE ind = 0..9;
     matr = array[ind, ind] of real;

VAR a: matr;
    k, n, i, j: integer;

PROCEDURE Proiz(r, l: integer; b: matr);
    var pr: real;
        i: integer;
    Begin
        pr:= 1;
        for i:= 0 to r do
            pr:= pr*a[i, l];
        writeln(pr:3:3);
    End;

BEGIN
    write('Введите размерность матрицы: ');
    read(n);
    write('Введите номер столбца: ');
    read(k);

    writeln('Введите элементы');
    for i:= 0 to n do
        for j:= 0 to n do
            read(a[i, j]);

    write('Произведение равно: ');
    proiz(k, n, a);
END.
