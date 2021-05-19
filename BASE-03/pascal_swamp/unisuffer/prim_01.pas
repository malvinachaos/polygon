BEGIN
    Var k:= ReadInteger('Введите целое число: ');
    WriteLn('Введено ', k);
    
    Write('Попробуем ещё раз ');
    Read(k);

    Var c: Char;
    Write('Введите символ: ');
    ReadLn(c); { Откуда в буфере NewLine? он оттуда ^                          }
    WriteLn('Введено ', c, NewLine, '-'*80);

    Write('Вновь введите символ: ');
    Read(c); { Сюда из буфера достался NewLine                                 }
    Read(c); { А вот тут уже вводиится символ                                  }
    WriteLn('Введено ', c, NewLine, '-'*80);


END.
