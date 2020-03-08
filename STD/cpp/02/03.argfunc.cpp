#include <iostream>

using namespace std;
void sum(int a)
{
	a = 50;
}

void inter(int *a)
{
	*a *= 50;
}
int main()
{
	//Передача по значению
	int f = 20;
	sum(f);
	cout << f << endl;
	inter(&f);
	cout << f << endl;
	return 0;
}
