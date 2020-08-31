#include <iostream>

using namespace std;

void foo(int a[5])
{
    for (int i = 0; i < 5; i++)
        cout << a[i] + 3 << ' ';

    cout << endl;
}

/*   |   Такая конструкция вызовет ошибку
     |
    \./
int [5] bar(int a[5])
{
    for (int i = 0; i < 5; i++)
        a[i] = (a[i] + i) * (i + 5);
    return a;
}
 */

void bar(int * a)
{
    for(int * i = a; i < a + 5; i++)
        *i = (*i) + 3;
}

void foobar(int *a)
{
    for(int i = 0; i < 5; i++)
        a[i] = a[i] + 5;
}

int main()
{
    int a[5] = {10, 20, 30, 40, 50};
    foo(a);
    bar(a);
    foo(a);
    cout << "Вывод: функции foo() и bar() обращаются к одну и тому же указателю, не смотря на то, что\
в bar мы это делаем отчётливо." << endl << endl;
    foobar(a);
    foo(a);
    cout << "То же самое относится и к функции foobar. То есть мы в любом случае редактируем\
переданный в функцию массив и чтобы этого избежать нам придётся делать цикл, чтобы скопировать в\
локальный массив значения." << endl;

    return 0;
}
