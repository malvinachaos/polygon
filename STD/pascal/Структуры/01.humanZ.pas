PROGRAM MARINA_01;
(*
 * Данная программа создаёт записи студентов и сохраняет в файл
 *)
TYPE 
student = RECORD
    group, surname, gender:string;
    year, math:integer;
    scholarship:real;
END;
    one_dim = array[1..30] of student;

VAR a: one_dim;
    n:integer;
    name:string;
    out: text;

{------------------------------------~~~~ PROCEDURES ~~~~-----------------------------------------}
(*                       *
 * ~~ Список процедур ~~ *
 *                       *
 *      inarrary         *
 *      outarray         *
 *                       *)

PROCEDURE inarray(n:integer; var a:one_dim);    {~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}
VAR i:integer;                                  { Ввод данных в массив типа student }
BEGIN                                           {~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}
    for i:= 1 to n do
    begin
        with a[i] do
        begin
            writeln(#10#13, 'Введите данные о ', i,'-м студенте: ', #10#13);
            
            write('Номер группы(двузначное число): ');
            readln(group);
            
            write('Фамилия: '); 
            readln(surname);

            write('Год рождения: ');
            readln(year);
            
            write('Гендер(ж -- женский, м -- мужской, н -- не бинарный): ');
            readln(gender);

            write('Оценка по математике: ');
            readln(math);

            write('Стипендия: ');
            readln(scholarship);
        end;
    end;
END;

PROCEDURE outarray(n:integer; var a:one_dim; var out:text);   {~~~~~~~~~~~~~~~~~~~~~~~~~}
VAR i:integer;                                                { Вывод данных из массива }
BEGIN                                                         {~~~~~~~~~~~~~~~~~~~~~~~~~}
    writeln(out, '№  ', 'Группа  ', 'Фамилия  ', 'Год  ', 'Гендер  ', 'Оценка   ', 'Стипендия   ');
    for i:= 1 to n do
        with a[i] do
        begin
            writeln(out, i:2, ' ', group, ' ', surname, ' ', year, ' ', gender, ' ', math, scholarship:6:2);
        end;
END;
{---------------------------------------~~~~ END ~~~~---------------------------------------------}

{---------------------------------------~~~~ MAIN ~~~~--------------------------------------------}
BEGIN
    write('Введите количество записей(максимум 30): ');
    readln(n);
    write('Введите имя файла, куда записать данные(не забудьте потом поставить .txt): ');
    readln(name);
    
    assign(out, name);
    rewrite(out);

    inarray(n, a);
    outarray(n, a, out);

    close(out);
END.
