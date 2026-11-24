/*
Problema 1001 BeeCrowd
2026.11.03
Gustado Ribeiro
*/

#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    double r, area;

    cin >> r;
    area = 3.14159 * r * r;
    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;

    return 0;
}