#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    int i2;
    double d2;
    string s2;
    // Declare second integer, double, and String variables.
    
    cin >> i2;
    cin >> d2;
    cin.ignore();
    getline(cin, s2);
    // Read and save an integer, double, and String to your variables.
    // Note: If you have trouble reading the entire string, please go back and review the Tutorial closely.
    
    cout << i + i2 << endl;
    // Print the sum of both integer variables on a new line.
    
    cout << fixed << setprecision(1) << d + d2 << endl;
    // Print the sum of the double variables on a new line.
    
    cout << s + s2 << endl;
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.

    return 0;
}