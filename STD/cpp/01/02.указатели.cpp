#include <iostream>

using namespace std;

int main()
{
	int a = 5;
	cout << &a << " это адрес переменной a\n";

	//Объявление и использование указателей
	int *pa;
	pa = &a;
	cout << pa;
	cout << endl;
	cout << "pa -- указатель на переменную a" << endl;
	//int fo = &a; ошибка
	//int *fo = a; ошибка
	cout << pa << " -- pa == &a" << endl;
	cout << *pa << " -- *pa == a" << endl;

	if (*pa == a) cout << 42 << endl;
	return 0;
}
