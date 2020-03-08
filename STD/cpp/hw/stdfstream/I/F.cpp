#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	fstream in, out, help;
	in.open("in.txt", ios::in);
	out.open("out.txt", ios::out);
	help.open("help.txt", ios::out);
	char sym = '0';
	int lines = 0, symbols = 0;

	while(!in.eof())
	{
		in.get(sym);
		if(sym == '\n') ++lines;
		else ++symbols;
		if(lines == 2 && sym != '\n') help << sym;
	}
	--lines;	
	out << lines << endl << symbols << endl;
	help.close();
	if (lines >= 3)
	{
		help.open("help.txt", ios::in);
		while(!help.eof())
		{
			help.get(sym);
			out << sym;
		}
	}
	else out << 0;
	in.close();
	out.close();
	help.close();
	return 0;
}
