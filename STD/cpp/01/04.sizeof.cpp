#include <iostream>

using namespace std;

int main()
{
	//sizeof
	cout << "Размер char " << sizeof(char) << endl;
	cout << "Размер int " << sizeof(int) << endl;
	cout << "Размер double " << sizeof(double) << endl;
	cout << "Размер float " << sizeof(float) << endl;
	cout << "Размер long long int " << sizeof(long long int) << endl;

	int arr[9] = {};
	cout << "Размер массива arr: " << sizeof(arr) << endl;
	cout << "Количество элемнтов в массиве arr: " << sizeof(arr)/sizeof(arr[0]);

	return 0;
}
