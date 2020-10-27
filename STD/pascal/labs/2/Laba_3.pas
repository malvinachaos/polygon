program laba_3v18;
var x, y, a, b, c, s, n, ch, eps: real;
begin

ch:=1;
repeat
  repeat
  writeln('Введите число х (от -1 до 1):');
  readln(x);
  until (x>-1) and (1>x);
  repeat
  writeln('Введите значение точности (от 0 до 1):');
  readln(eps);
  until (eps>0) and (1>eps);
  
  
  
  a:=x;
  b:=2;
  c:=a*b;
  s:=c;
  n:=2;
  
 while (abs(c)>=eps) and (n<100) do
 begin
   a:= a*(-1)*x/n;
   b:=b+1;
   c:=a*b;
   s:=s+c;
   n:=n+1;
  end;
  y:=x*exp(-x)-exp(-x)+1;
  
  writeln('s: ', Round(s/eps)*eps);
  writeln('y: ',Round(y/eps)*eps);
  
  writeln('Если хотите повторить, напишите 1');
  readln(ch)
  until ch<>1;
  end.