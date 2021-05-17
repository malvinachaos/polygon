BEGIN
    var a:= MatrGen(10, 10, (i, j) -> (i + 1) * (j + 1));
    a.println;

    writeln();
    writeln('Количество колонок: ', a.ColCount);
    writeln('Количество   строк: ', a.RowCount);

    writeln('Расширения для колонок:');
    a.Cols.Println;
    a.Col(3).Println;        {выводит колонку в виде массива                    }
    a.ColSeq(3).Println;     {выводит колонку в виде последовательности         }
    a.ElementsByCol.Println; {выводит элементы колонки в виде последовательности}
    writeln();

    writeln('Расширения для строк:');
    writeln();

    a.ElementsWithIndices.Println; {Возвращает последовательность трёхэлементных }
                                   {кортежей, в которой каджый формируется в виде}
                                   {(значение, индекс i, индекс j)               }

    a.MatrSlice();
END.
