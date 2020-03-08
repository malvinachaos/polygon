#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main()
{
	fstream in, out;
	int count = 0;
	char watch = ' ';
	in.open("in.txt", ios::in);
	out.open("out.txt", ios::out);
	while(!in.eof())
	{
		in.get(watch);
		if(watch == 'e')
		{
			in.get(watch);
			++count;
			if(watch == 'n')
			{
				in.get(watch);
				++count;
				if(watch == 'd')
				++count;
				break;
			}
		}
		++count;
	}
	in.close();
	in.open("in.txt", ios::in);
	out << count << endl;
	for(int i = 0; i < count; i++)
	{
		in.get(watch);
		out << watch << ' ';
	}
	in.close();
	out.close();
	return 0;
}
