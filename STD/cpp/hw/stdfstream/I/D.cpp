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
	--everything;
	in.close();
	in.open("in.txt", ios::in);
	
	while(!in.eof())
	{
		if(count != 2 && count < everything)
		{
			in.getline(syms, 101);
			out << syms << endl;
			++count;

		}
		else  if(count != 2 && count == everything)
		{
			in.getline(syms, 101);
			out << syms;
		}
		else if(count == 2)
		{
			in.getline(syms, 101);
			//debug << syms << endl;
			++count;
		}
		//debug << endl << "count is " << count;
	}

	in.close();
	out.close();
	//debug.close();
	return 0;
}
