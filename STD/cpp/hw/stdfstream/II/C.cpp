#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin.seekg(-2, ios::end);
	const int i = cin.tellg();
	cin.seekg(0, ios::end);
	int fullpos = cin.tellg(), posb = 0, pose = -2;
	char chbeg[i] = {}, chend[i] = {}, sym, mom;

	while(posb <= i/2 && pose >= -i)
	{
		cin.seekg(posb, ios::beg);
		cin.get(sym);
		cout << sym;
	
		cin.seekg(pose, ios::end);
		cin.get(sym);
		cout << sym;

		++posb;
		--pose;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}

