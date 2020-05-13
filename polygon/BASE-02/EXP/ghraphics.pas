PROGRAM Strange;
Uses ptcGraph;

VAR
    drv, mode, x, y, i, Color: integer;

BEGIN
    DetectGraph(drv, mode);
    InitGraph(drv, mode, '');
    Color:= 0;
    y:= 0;
    for i:= 0 to 63 do
    begin
        for x:= 0 to 1023 do
        begin
            SetColor(Color);
            Line(x, y, x, y+10);
            Inc(Color);
            write(Color, ' ');
        end;
        writeln;
        y:= y+12;
    end;
    Readln;
    CloseGraph;
END.
