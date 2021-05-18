PROGRAM UniUni;

VAR quote: char = '''';
    n: longword = 1;

BEGIN
    {В PascalABCNet ипользуется Unicode                                        }
    WriteLn(quote);
    quote.code.println;      {данный код выводит код символа                   }
    WriteLn(ordansi(quote)); {10-й код символа в 1-байтной кодировке шинды     }
    WriteLn('-'*80, NewLine);

    {А теперь попробуем два вывода:                                            }
    range('А', 'я').select(c -> c.code).println();
    WriteLn('-'*80, NewLine);

    for var c:= 'А' to 'я' do
        write(ord(c), ' ');
    WriteLn('-'*80, NewLine);

    {Короче, Pascal ABC Net может ещё и так:                                   }
    println((2 * ('m' + 'a') + ' ') * 5);
    
    ('rub ' + 134).println; {При конкатенации строки и числа, второе будет     }
                            {сконвертировано в строку                          }
    WriteLn('-'*80, NewLine);

    {Статическая обработка символа                                             }
    char.IsLetter('3').println;
    {Обработка через расширение                                                }
    'J'.IsLetter.println;
    WriteLn('-'*80, NewLine);

    {Количество поддерживаемых букв в PascalABC.Net}
    Range(0, word.MaxValue).Where(n -> Chr(n).IsLetter).Count.Println;
    { word.MaxValue возвращает максимально возможное число данного типа, range }
    { строит последовательность от 0 до макисмального числа, что позволяет по- }
    { лучить все коды. Затем, последовательность фильтруется расширением where,}
    { использующим лямбда-выражением, которое проверяет то, что это буква. А   }
    { потом, .Count возвращает итоговое количество элементов получившейся пос- }
    { ледовательности.                                                         }
    WriteLn('-'*80, NewLine);

    '0'.IsDigit.PrintLn;               { <-- проверка на число                 }
    char.IsLetterOrDigit('@').PrintLn; { <-- c.isalpha()                       }
    char.IsWhiteSpace('1').PrintLn;    { <-- является ли он пробельным символом}
    char.IsWhiteSpace(#13).PrintLn;
    WriteLn('-'*80, NewLine);

    { Чекаем пробельные символы                                                }
    WriteLn('Коды White Space символов:');
    Range(0, word.MaxValue).Where(n -> char.IsWhiteSpace(chr(n))).PrintLn;
    WriteLn('-'*80, NewLine);

    { Является ли символ знаком пунктуации                                     }
    char.IsPunctuation(',').PrintLn;
    
    { Все знаки препинания по мнению PascalABC.Net                             }
    Range(0, word.MaxValue).Select(n -> Chr(n)).
        Where(c -> char.IsPunctuation(c)).PrintLn;
    WriteLn('-'*80, NewLine);

    { Проверка на верхний/нижний регистр                                       }
    'C'.IsUpper.PrintLn;
    'c'.IsLower.PrintLn;
    char.IsUpper('C').Println;
    char.IsLower('c').Println;
    WriteLn('-'*80, NewLine);

    { Располагается ли символ в указаном интервале                             }
    'A'.InRange(#0, 'z').PrintLn;
    WriteLn('-'*80, NewLine);

    { Приведение буквенного символа к верхнему/нижнему регистру                }
    '@'.ToUpper.PrintLn;
    char.ToUpper('g').PrintLn;
    UpCase('z').PrintLn;
    UpperCase('l').PrintLn; { синоним UpCase                                   }
    
    '@'.ToLower.PrintLn;
    char.ToLower('g').PrintLn;
    LowCase('z').PrintLn;
    LowerCase('l').PrintLn; { синоним LowCase                                  }
    WriteLn('-'*80, NewLine);

    { Преобразование символа в число                                           }
    WriteLn('2'.ToDigit + 8); { преобразует в неотрицательный, однозначный     }
                              { integer                                        }
    { если символ будет не числовым, то .ToDigit вернёт False, а при выполнении}
    { программы она рухнет                                                     }

    { символ, предшествующий/следующий указанному                              }
    'z'.Pred.PrintLn;
    Pred('я').PrintLn;

    'z'.Succ.PrintLn;
    Succ('я').PrintLn;
    WriteLn('-'*80, NewLine);

    { Смещение по кодовой таблице                                              }
    var c:= 'я';
    Dec(c, 9);
    c.PrintLn;
    Inc(c, 30);
    c.PrintLn;
    WriteLn('-'*80, NewLine);

END.
