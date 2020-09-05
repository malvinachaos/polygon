#include <iostream>

using namespace std;

void reverse(int a = 0)
{
    cin >> a;
    if (a == 0) return;
    reverse(a);
    cout << a << " ";
}

int main()
{
    reverse();
    return 0;
}
