#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main()
{
	freopen("middle.txt", "r", stdin);
	cin.seekg(1, ios::end);
	int counts = cin.tellg();
	char sym = '0';
	if (counts % 2 == 0)
	{
		cin.seekg(counts/2-2, ios::beg);
		cin.get(sym);
		cout << sym << ' ';
		cin.get(sym);
		cout << sym;
	}
	if (counts % 2 != 0)
	{
		cin.seekg(counts/2-1, ios::beg);
		cin.get(sym);
		cout << sym;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
