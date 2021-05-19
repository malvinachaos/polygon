PROGRAM RUSSIAN_ALPHABET;

VAR sym: char;
    alphabet:= Range('А', 'Е') + 'Ё' + Range('Ж', 'З');

BEGIN
    WriteLn('Вводите подряд буквы русского алфавита');

    foreach var c in alphabet do
    begin
        Write(#13);
        sym:= ReadChar('>>').ToUpper;
        if sym <> c then
        begin
            WriteLn(#13, 'Вы ошиблись!');
            exit;
        end;
    end;
    WriteLn('Молодец');

END.
