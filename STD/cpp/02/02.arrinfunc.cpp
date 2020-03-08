#include <iostream>

using namespace std;

int sum_arr(int a[], int size);

int main()
{
	int d[10] = {};
	cout << sum_arr(d, 10);
	return 0;
}
int sum_arr(int a[], int size)
{
	int sum = 0;
	for(int i = 0; i < size; i++)
	{
		a[i] = i;
		sum += a[i];
	}
	return sum;
}
