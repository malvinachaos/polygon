#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	//ofstream debug("debug.log");
	int count = 0, everything = 0;
	char syms[101] = {};

	while(!in.eof())
	{
		in.getline(syms, 101);
		++everything;
	}
	//debug << "everything is " << everything << endl;
	everything -= 1; //why? except everything -= 2;
	//debug << "everything is " << everything << endl;
	in.close();
	in.open("in.txt", ios::in);
	
	while(!in.eof())
	{
		if(count < everything - 1)
		{
			in.getline(syms, 101);
			out << syms << endl;
			++count;
		}
		else if(count == everything - 1)
		{
			in.getline(syms, 101);
			out << syms;
			++count;

		}
		else if(count == everything)
		{
			in.getline(syms, 101);
			//cout << syms;
			//debug << syms << endl;
		}
		//debug << endl << "count is " << count;
	}

	in.close();
	out.close();
	//debug.close();
	return 0;
}
