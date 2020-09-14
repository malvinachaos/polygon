VAR n: byte;

FUNCTION factorial(n: byte): extended;
Begin
    if n = 0 then factorial:= 1
    else factorial:= n*factorial(n-1);
End;

BEGIN
    write('Введите число ');
    readln(n);

    writeln('Факториал равен ', factorial(n));
END.
