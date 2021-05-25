PROGRAM ghost;


BEGIN
    {                               Удаление строк                             }
    var STANDART:= 'Я конечно добрый но могу уебать';
    var st:= STANDART;
    
    st.PrintLn;
    { нумерация позиций ведётся с нуля } {Я не добрый но могу уебать}
    Delete(st, 3, 2);
    Delete(st, 5, 3);
    Delete(st, 12, 15);
    st.PrintLn;

    st:= STANDART;
{    Delete(st, );
    Delete(st, );
    Delete(st, );
    Delete(st, );
}
END.
