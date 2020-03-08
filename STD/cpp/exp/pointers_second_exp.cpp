#include <iostream>

using namespace std;

int main()
{
	char inst = '*';
	char * ptr = (char *)&inst;
	int * ptr2 = (int *)&inst;
	cout << ptr << endl << *ptr << endl;
	cout << ptr2 << endl << *ptr2 << endl << endl;

	int array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
	int * point = array;
	cout << array[5] << " = " << *(point+5) << endl << "Адрес элемента, приведённого выше: " << point+5 << endl << endl;
	for(int i = 0; i < 10; i++)
		cout << "Адрес " << i << "-го элемента: " << point+i << endl; //Альтернатива &array[i]

	return 0;
}
