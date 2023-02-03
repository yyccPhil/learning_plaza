// Fibonacci Sequence

#include <iostream>
using namespace std;

void test(int range)
{
    cout << 0;

    int fibonacci = 1;
    int temp = 0;

    for (int i = 1; i < range; i++) {
        cout << " " << fibonacci;
        fibonacci += temp;
        temp = fibonacci - temp;
    }
        
}


