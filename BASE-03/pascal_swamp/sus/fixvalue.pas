BEGIN
    var a:= MatrFill(32, 64, '*');
    
    for var i:= 0 to 31 do
    begin
        for var j:= 0 to 63 do
            write(a[i, j]);
        writeln()
    end;

END.
