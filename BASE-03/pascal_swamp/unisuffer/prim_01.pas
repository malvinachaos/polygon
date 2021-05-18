BEGIN
    Var k:= ReadInteger('Введите целое число: ');
    WriteLn('Введено ', k);

    Var c: Char;
    Write('Введите символ: ');
    ReadLn(c);
    WriteLn('Введено ', c, NewLine, '-'*80);

    Write('Вновь введите символ: ');
    ReadLn(c);
    WriteLn('Введено ', c, NewLine, '-'*80);


END.
