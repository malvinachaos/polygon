PROGRAM beauty_output;

VAR field  : array of array of char;
    n, i, j: byte;

BEGIN
    repeat
        write('Введите нечётное число n для матрицы размерности nxn меньше 255: ');
        readln(n);
    until (n mod 2 <> 0);

    setlength(field, n);
    for i:= 0 to n-1 do
        setlength(field[i], n);

    {Я не понимаю, как работают лямбда-выражения}
    field.transform((t, i, j) -> (i = j) ? '*' : t);
    field.println;

END.
