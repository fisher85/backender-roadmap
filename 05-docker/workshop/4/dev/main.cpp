#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {

    map<string, int> test_map = {
        {"hello", 1},
        {"this feature std17", 2}
    };
    for (const auto& [name, number]: test_map) {
        cout << name << " " << number << '\n';
    }
    return 0;
}