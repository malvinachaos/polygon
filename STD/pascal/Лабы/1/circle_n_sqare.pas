PROGRAM by_Marina;

VAR xc, xs, a, r: real;

{ввести проверку на вложенность фигур}

BEGIN
    writeln('Введите следующие значения:');
    write('центр окружности по координате абсциссы: ');
    readln(xc);

    write('радиус окружности: '); 
    readln(r);

    write('центр квадрата по координате абсциссы: ');
    readln(xs);

    write('сторона квадрата: ');
    readln(a);
    
    if ((r > 0) and (a > 0)) then
    begin
        r:= r + a/2;

        if (xs < xc) then xc:= xc - xs
        else xc:= xs - xc;

        if (xc > r) then
            writeln('Фигуры не пересекаются.');
        if (xc = r) then
            writeln('Фигуры касаются.');
        
        if (xc < r) then
        begin
            write('Фигуры пересекаются');
            if (xc = 0) then
                writeln('Фигуры концетричны.'); 
        end;
    end
    else writeln(
        #13#10, 
        'Вы ввели неверные данные!', 
        #13#10, 
        'Радиус окружности и сторона квадрата не могут быть отрицательными или равны нулю!'
        );
END.
