#include <iostream>

using namespace std;

int main()
{
	//Обьявление и задание значений указателям
	int m = 2345;
	int *pointer = &m;
	int f = *pointer;
	cout << m << " Изначальное значение" << endl;
	cout << &m << " Адресс переменной" << endl;
	cout << pointer << " Адресс переменной" << endl;
	cout << f << " Изначальное значение" << endl;
	
	//Арифм операции с указателями
	int *snd_pointer = pointer;
	cout << snd_pointer << " = " << pointer << endl << endl;
	--snd_pointer;
	
	cout << snd_pointer << ' ' << *snd_pointer << endl << endl;
	pointer -= 456;
	cout << pointer << ' ' << *pointer << endl << endl;
	pointer += 1278;
	cout << pointer << ' ' << *pointer << endl << endl;
	//pointer *= 2; -- эта операция вызовет ошибку
	cout << pointer << ' ' << *pointer << endl << endl;
	pointer -= 0;
	cout << pointer << ' ' << *pointer << endl << endl;
	//pointer -= 50.234; -- вызовет ошибку
	pointer -= m;
	cout << pointer << ' ' << *pointer << endl << endl;
	//*pointer -= &m; -- ошибка
	
	/* Это вызовет ошибку, т.к. можно ссылаться на соотв-й указа
	 * телю тип
	 * double symbol = 234.13113;
	 * int *point = &symbol;
	 * cout << point << ' ' << *point << endl;
	*/


	return 0;
}
