#include <iostream>
#include <string>
#include <set>   

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int c;
    char type;
    cin >> c >> type;

    int sz;
    if (type == 'Y') sz = 1;      
    else if (type == 'F') sz = 2; 
    else sz = 3;                  

    set<string> s;
    for (int i = 0; i < c; i++) {
        string word;
        cin >> word;
        s.insert(word);
    }

    
    cout << s.size() / sz << "\n";

    return 0;
}