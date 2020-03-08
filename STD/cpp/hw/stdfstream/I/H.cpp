
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
	char *data[102401] = {};
	
	int i = 0;
	while(!in.eof())
	{
		char tmp[102400] = {};
		in.getline(tmp, 102401);

		int len = int(strlen(tmp)) + 1;
		data[i] = new char[len];
		//Очистка динамического массива
		for(int j = 0; j < len; j++) data[i][j] = 0;
		//Копируем прочтённую строку
		strncpy(data[i], tmp, len);
		++i;
	}
	
	//Вывод наоборот

	for (int j = i - 2; j >= 0; --j)
	{
		out << data[j] << endl;
	}

	//Чистим память

	for(int j = 0; j < i; j++)
	{
		delete [] data[j];
	}

	in.close();
	out.close();
	return 0;
}
