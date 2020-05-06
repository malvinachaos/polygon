TYPE ind = 0..9;
     matr = array[ind, ind] of real;

VAR a: matr;
    k, n, i, j: integer;
    p:real;

FUNCTION proiz(n, k:ind; var a:matr):real;
    VAR pr: real;
        i: ind;
    Begin
        pr:= 1;
        for i:= 0 to n do
            pr:= pr*a[i, k];

        proiz:= pr;
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

    p:= proiz(n, k, a);
    write(p:3:3);
END.
