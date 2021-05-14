VAR i, j: integer;

BEGIN
    var a:= MatrRandom(5, 3, 1, 100);

    for i:= 0 to 4 do
    begin
        for j:= 0 to 2 do
            write(a[i, j]:4, ' ');
        writeln();
    end;

END.
