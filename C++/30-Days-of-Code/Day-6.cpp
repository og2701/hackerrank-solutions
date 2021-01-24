#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin >> n;
    
    for(int i=0; i<n; i++){
        string s;
        cin >> s;
        
        for(int j=0; j<s.length(); j+=2){
            cout << s[j];
        }
        cout << ' ';
        for(int j=1; j<s.length(); j+=2){
            cout << s[j];
        }
        cout << endl;
    }
      
    return 0;
}
