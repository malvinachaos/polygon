PROGRAM UniUni;

VAR quote: char = '''';
    n: longword = 1;

BEGIN
    {В PascalABCNet ипользуется Unicode}
    writeln(quote);
    quote.code.println;      {данный код выводит код символа                        }
    writeln(ordansi(quote)); {десятичный код символа в однобайтной кодировке Windows}

    write('Введите количество символов Unicode, которые вы хотите вывести(макс 65535) ');
    readln(n);

    for var i:= 0 to n do
        chr(i).print;
    writeln();

    {А теперь попробуем два вывода:}
    range('А', 'я').select(c -> c.code).println();
    writeln();

    for var c:= 'А' to 'я' do
        write(ord(c), ' ');
    writeln();
    
END.
