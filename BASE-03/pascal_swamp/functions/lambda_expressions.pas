VAR f: integer -> integer:= x -> 3 * x + 4;

BEGIN
    {(x, y) -> x + y}
    {эквивалентно function foo(x: integer):= x * x + 4}
    writeln(f(511), #13#10, f(62), #13#10);

    f:= p -> p div 10;

    writeln(f(511), #13#10, f(62), #13#10);
    {lambda-выражение без параметров}

    var n: () -> integer := () -> random(1, 100);
    writeln(n, #13#10, n, #13#10, n, #13#10, n, #13#10, n, #13#10);
    
    var c: integer -> integer := x -> x * 500;

    writeln(c(500));

END.
