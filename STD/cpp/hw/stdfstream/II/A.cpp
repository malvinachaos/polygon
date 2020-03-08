#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int convert();

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int fst = convert(), snd = convert();
	int sum = fst + snd;

	cin.seekg(sum, ios::beg);
	cout << convert();

	fclose(stdin);
	fclose(stdout);
	return 0;
}

int convert()
{
	char number[10] = {}, sym;
	bool FLG = 0;
	int i = 0;
	while(42)
	{
		cin.get(sym);
		if (isdigit(sym)) FLG = 42;
		if ((!isdigit(sym) && sym != '-') && FLG) break;
		if (isdigit(sym) || sym == '-')
		{
			number[i] = sym;
			++i;
		}
	}

	return atoi(number);
}
