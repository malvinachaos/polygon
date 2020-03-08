#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
	//Вывод рандомных чисел
	cout << rand();

	cout << "Вывод случайного числа в диапазоне от 0 до 10" << endl <<
		rand() % 10 << endl;

	//Вывод действительно случайных чисел
	srand(42);

	for(int i = 0; i < 10; i++)
		cout << rand() % 34 << endl << endl;

	//Используем time, возвращающий кол-во секунд в системрых часах устр-ва
	srand(time(0));
	for(int i = 0; i < 10; i++)
		cout << 3 + rand()%50 << endl << endl;

	// от 3 до 50
	return 0;
}
