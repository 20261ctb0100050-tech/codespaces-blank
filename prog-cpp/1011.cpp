/*
Problema 1011 BeeCrowd
2026.11.03
Gustado Ribeiro
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double r, volume;

    cin >> r;
    volume= (4.0/3.0) *3.14159*r*r* r;
    cout << fixed << setprecision(3);
    cout << "VOLUME = " << volume << endl;

    return 0;
}