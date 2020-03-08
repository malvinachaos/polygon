#include <iostream>

using namespace std;

int main()
{
	int *p = new int;
	*p = 2;
	cout << p << ' ' << *p << endl;
	delete p;
	return 0;
}
