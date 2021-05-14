FUNCTION B(i: integer): integer; forward;

FUNCTION A(j: integer): integer;
begin
    result:= j + B(j);
end;

FUNCTION B(i: integer): integer;
begin
    result:= i*i;
end;

BEGIN
    writeln(A(5));
END.
