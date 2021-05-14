FUNCTION fact(n: integer): biginteger;
begin
    if n = 0 then
        result:= 1
    else
        result:= n * fact(n-1);
end;

VAR x: integer = 0;

BEGIN
    write('Введите число x: ');
    readln(x);
    writeln('Факториал ', x, ' равен ', fact(x));
END.
