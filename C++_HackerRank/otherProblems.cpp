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
