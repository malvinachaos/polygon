begin // p08008
    var a := MatrRandom(7, 7, -50, 50);
    Println('-' * 7 * 4);
    writeln('Исходная матрица');
    a.Println;
    Println('-' * 7 * 4);

    var rs: () -> integer := () -> Random(1, 2) = 1 ? -1 : 1;
    a.Transform((t, i, j) -> Abs(t) > 20 ? rs * (i + j) : t);
    writeln('Какое-то преобразование(вообще хз)');
    a.Println;
    Println('-' * 7 * 4);

    var b := a.Rows.Select(row -> row.Where(t -> t > 0).Count).ToArray;
    var nCols := a.ColCount;
    var c := ArrFill(nCols, 0);

    for var i := 0 to a.RowCount - 1 do
        if 2 * b[i] > nCols then
            a.SetRow(i, c);
    a.Println;
end.
