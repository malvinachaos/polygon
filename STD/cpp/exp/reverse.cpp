#include <iostream>

using namespace std;

void reverse(int a)
{
    cin >> a;
    if (a == 0) return;
    reverse(a);
    cout << a << " ";
}

int main()
{
    reverse(0);
    return 0;
}
