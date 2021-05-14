TYPE func = function(const i: integer): integer;

FUNCTION p(const i: integer):= 4 + i*4 - 90 + i;

FUNCTION some_sum(const a, b, c: integer; f: func): integer;
begin
    result:= f(a) + f(b) + f(c);
end;

BEGIN
    writeln(some_sum(5, 4, 3, p));
END.
