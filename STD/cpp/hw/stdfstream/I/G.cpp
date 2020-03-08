#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main()
{
	ifstream numbers("numbers.txt");
	int counting_stars = 0;
	char Magic = '0';
	bool flazhochek = 0;

	while(!numbers.eof())
	{
		numbers.get(Magic);
		if(isdigit(Magic) && !flazhochek)
		{
			flazhochek = 42;
			++counting_stars;
		}
		else if (!isdigit(Magic) && flazhochek)
			flazhochek = 0;
	}

	cout << counting_stars;
	return 0;
}
