VAR A: array[0..2, 0..2] of real;
    C, D, ARIFM, S: real;
    i, j: integer;

BEGIN
    {Ввод данных}
    Writeln('Введите девять чисел');
    for i:= 0 to 2 do
		for j:= 0 to 2 do
			Read(A[i, j]);

    Writeln('Введите концы отрезка: ');
    Read(C, D);

	{Вычисление}
	ARIFM:= 0;
	for i:= 0 to 2 do
	begin
		for j:= 0 to 2 do
		begin
			if (A[i, j] >= C) and (A[i, j] <= D) then
			begin	
				ARIFM:= ARIFM + A[i, j];
				S:= S+1;
			end;
		end;
	end;

	{Вывод}
	Writeln('Среднее арифмитическое равно ', ARIFM/S);
END.
