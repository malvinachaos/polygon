PROGRAM MARINA_02;
(* Данная программа ищет максимальный(max), минимальный(min) положительный элемент.
 * Если модуль man и min меньше заданного числа r, изменить отрицательные элементы на
 * их модули. Ввод/вывод через файлы. Отрицательные и положительные числа должны быть
 * в матрице.
 *)

TYPE two_dim = array[0..4, 0..3] of real;

VAR a:two_dim;
    i, j:integer;
    max, min, r:real;
    ini, out:text;       {ini -- входной файл, out -- выходной}

{-----------------------------~~~~ PROCEDURE and FUNCTIONS ~~~~-----------------------------------}
(* ~~ Список процедур и функций ~~
 *
 *   maximum_negative 
 *   minimum_positive
 *   change_to_abs
 *)
PROCEDURE maximum_negative(a:two_dim; var max:real);        { .--------.        }
{Находит максимально отрицательное число(?) в матрице}      { |         \       }
VAR i, j:integer;                                           { |          \      }
    FLG: boolean;                                           { |           *     }
BEGIN                                                       { |           |     }
    FLG:= true;                                             { |           |     }
    for i:= 0 to 4 do                                       { |           |     }
        for j:= 0 to 3 do                                   { |           .     }
        begin                                               { |          /      }
            if a[i, j] < 0 then                             { |         /       }
                if FLG then                                 { *--------*        }
                begin
                    FLG:= false;
                    max:= a[i, j];                          {    ___     ___    }
                end                                         {   /   \   /   \   }
                else                                        {  /     \_/     \  }
                    if a[i, j] > max then                   { |               | }
                        max:= a[i, j];                      { |               | }
        end;                                                {  \             /  }
END;                                                        {   \           /   }
                                                            {    \___   ___/    }
PROCEDURE minimum_positive(a:two_dim; var min:real);        {        *-*        }
{Находит минимально положительное число в матрице}
VAR i, j:integer;
    FLG: boolean;
BEGIN
    FLG:= true;
    for i:= 0 to 4 do
        for j:= 0 to 3 do
        begin
            if a[i, j] > 0 then
                if FLG then
                begin
                    FLG:= false;
                    min:= a[i, j];
                end
            else
                if a[i, j] < min then
                    min:= a[i, j];
        end;
END;

PROCEDURE change_to_abs(var a:two_dim);
{меняет отрицательные числа на положительные}
VAR i, j:integer;
BEGIN
    for i:= 0 to 4 do
        for j:= 0 to 3 do
            if a[i, j] < 0 then
                a[i, j]:= abs(a[i, j]);
END;

{---------------------------------------~~~~ END ~~~~---------------------------------------------}

{----------------------------------~~~~ MAIN PROGRAMM ~~~~----------------------------------------}
BEGIN
    assign(ini, 'in.txt');   {~~~~~~~~~~~~~~~~~~~~}
    assign(out, 'out.txt');  { Открываем на ввод- } 
    reset(ini);              { вывод данные       }
    rewrite(out);            {~~~~~~~~~~~~~~~~~~~~}
    
    readln(ini, r);

    for i:= 0 to 4 do            {~~~~~~~~~~~~~~~~~~~~~~}
    begin                        { Вводим в матрицу 'a' }
        for j:= 0 to 3 do        { значения из файла    }
            read(ini, a[i, j]);  { 'in.txt'             }
        readln(ini);             {~~~~~~~~~~~~~~~~~~~~~~}
    end;

    maximum_negative(a, max);
    writeln('Наибольший отрицательный элемент матрицы -- ', max:6:2);

    minimum_positive(a, min);
    writeln('Наименьший положительный элемент матрицы -- ', min:6:2);

    if abs(max-min) < r then
    begin
        change_to_abs(a);
        writeln('#13 Смотрите, что получилось :#13');
        for i:= 0 to 4 do
        begin
            for j:= 0 to 3 do
                write(a[i, j]:6:2, ' ');
            writeln;
        end;
    end
    else 
        writeln(out, '|max-min|>=r');

    for i:= 0 to 4 do                {~~~~~~~~~~~~~~~~~~~~~~~~~~}
    begin                            { Выводим в файл 'out.txt' }
        for j:= 0 to 3 do            { все значения из матрицы  }
            write(out, a[i, j]:6:2); { 'a'                      }
        writeln(out);                {~~~~~~~~~~~~~~~~~~~~~~~~~~}
    end;

    close(ini);  { Не забывем закрывать }
    close(out);  {         !!!!         }
END.
