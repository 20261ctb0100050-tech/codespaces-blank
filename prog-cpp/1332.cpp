/*
Problema 1332 BeeCrowd
2026.11.03
Gustado Ribeiro
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, i;
    string s;

    cin >> n;
    for (i == 0; i < n; i++) {
        cin >> s;
        if (s.length() == 5) {
            cout <<    << endl;
        } else if ((s[0] == 'o' && s[1] 'n') || (s[0] == 'o' && s[2] == 'e') || (s[1] == 'n' && s[2] == 'e')) {
            cout << 1 << endl;
        } else {
            cout << 2 << endl;
        }
    }

    return 0;
}
