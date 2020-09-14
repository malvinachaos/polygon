#include <iostream>

using namespace std;

void output_array(int a[], unsigned size)
{
    for (int i = 0; i < size; i++)
        cout << a[i] << ' ';
    cout << endl;
}

void rotate(int a[], unsigned size, int shift)
{
    // --- отладка
    cout << "Было:" << endl;
    output_array(a, size);
    cout << endl;
    // ---

    if (shift != 0 && shift%size != 0) // Проверка на случай, если будет "нулевое смещение"
    {    
        shift = shift%size; // Чтобы смещение не было больше размера массива
        int tmp_fst = 0, tmp_snd = 0;
        for (int j = 0; j < shift; j++)
        {
            tmp_fst = a[j], tmp_snd = a[j+shift];
            for (int i = shift + j; i <= size - shift; i+=shift)
            {
                a[i] = tmp_fst;
                tmp_fst = tmp_snd;
                tmp_snd = a[i+shift];
            }
        }
    }

    // --- отладка
    cout << endl << "Стало:" << endl;
    output_array(a, size);
    cout << "----" << endl << endl;
    // ---
}


int main()
{
    int a[5] = {0, 1, 2, 3, 4};
    rotate(a, 5, 1);
    rotate(a, 5, 2);

    int b[25] = {};
    for (int *p = b; p < b+25; p++) *p = 25 - (p-b);

    rotate(b, 25, 5);
    rotate(b, 25, 67);
    rotate(a, 5, 5);
    rotate(a, 5, 0);
    rotate(a, 5, 25);

    int c[10] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    rotate(c, 10, 5);
    rotate(c, 10, 2);
    rotate(c, 10, 10);
    return 0;
}
