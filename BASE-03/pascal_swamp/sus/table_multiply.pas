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
    a.Rows.Println;
    a.Row(3).Println;        {выводит строку в виде массива                    }
    a.RowSeq(3).Println;     {выводит строку в виде последовательности         }
    a.ElementsByRow.Println; {выводит элементы строки в виде последовательности}
    writeln();

    a.ElementsWithIndices.Println; {Возвращает последовательность трёхэлементных }
                                   {кортежей, в которой каджый формируется в виде}
                                   {(значение, индекс i, индекс j)               }
    writeln();

    {begin row--v        v--- end column}
    a.MatrSlice(1, 4, 2, 5).println;
    {   end row ---^  ^---start column  }
    {Возвращает срез матрицы            }
    writeln();

    {a.ConvertAll(T, T1) преобразует элеметны одного массива в другой согласно }
    {                    lambda-выражению                                      }
    {a.Fill((i, j), -> T) заполняет массив по шаблону lambda-выражения.        }
    var rc: array[0..9] of integer = (1, 5, 5, 3, 2, 5, 5, 5, 5, 5);
    var rs: array[0..9] of integer = (0, 0, 0, 0, 0, -1, 0, 0, 0, 0);

    a.SetCol(2, rc); {устанавливает значения элементов из массива rc в третий столбец}

    a.SetRow(0, rs);
    a.println();
    writeln();

    a.SwapCols(2, 6);
    a.SwapRows(0, 9);
    a.println();
    writeln();

    {a.Transform(T -> T1) преобразует каждый элемент?}
    Transpose(a).println(); {Транспонирование матрицы}
    writeln();


END.
