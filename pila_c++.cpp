#include <iostream>
#include <vector>
using namespace std;

const int capacidad = 10;

int main() {
    vector<int> elementos;

    cout << "Teclea elemento de la pila (termina con -1)\n";

    while (elementos.size() < capacidad) {
        int x;
        cin >> x;

        if (x != -1) {
            elementos.push_back(x);
        }
        else {
            break;
        }
    }

    cout << "Elementos de la Pila: ";
    for (int i = elementos.size() - 1; i >= 0; --i) {
        cout << elementos[i] << " ";
    }

    return 0; // Espacio normal entre "return" y "0"
}
