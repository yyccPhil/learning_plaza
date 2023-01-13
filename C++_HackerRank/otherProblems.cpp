// Input and Output
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int a, b, c;
    cin >> a >> b >> c;
    cout << a + b + c << endl;
    return 0;
}

// -----------------------------------------------------------------------------------------------

// Basic Data Types
#include <iostream>
#include <cstdio>
#include <iomanip>
using namespace std;

int main() {
    // Complete the code.
    int a;
    long b;
    char c;
    float d;
    double e;
    
    cin >> a >> b >> c >> d >>e;
    
    cout << a << endl
         << b << endl
         << c << endl
         << fixed << setprecision(3) << d << endl
         << setprecision(9) << e;
    
    return 0;
}

// -----------------------------------------------------------------------------------------------

// For Loop
int main() {
    // Complete the code.
    int first, last;
    string numbers[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    cin >> first >> last;
    for (int i = first; i <= last; i++) {
        if (i <= 9) cout << numbers[i - 1] << endl;
        else {
            if (i % 2 == 0) cout << "even" << endl;
            else cout << "odd" << endl;
        }
    }
    return 0;
}

// -----------------------------------------------------------------------------------------------

// Functions
int max_of_four(int a, int b, int c, int d) {
    if (a > b) b = a;
    if (b > c) c = b;
    if (c > d) d = c;
    return d;
}
