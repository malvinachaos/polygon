#include <fstream>
#include <cstring>
using namespace std;
/*
	Предисловие
	В OS Windows в файлах конец стоки это '\r\n'
	В UNIX-like -- '\n'
	Поэтому есть ошибки
*/


int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	char data[255][255] = {};
	int str = 0, syms = 0;
	
	//Чтение файла
	while(!in.eof())
	{
		char s[255] = {};
		in.getline(s, 255);
		int len = strlen(s);

		//Избавление от символа возврата кoретки love from Windows
		if(s[len - 1] == '\r')
		{
			s[len - 1] = '\0';
			--len;
		}

		strncpy(data[str], s, len);
		//увеличиваем коол-во прочтённых символов
		syms += len;
		//увеличиваем кол-во прочтенных строк
		++str;
	}

	out << str << endl;
	out << syms << endl;

	if (str > 2)
		out << data[2];
	else out << 0;

	return 0;
}
