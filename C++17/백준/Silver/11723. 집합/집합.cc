#include <iostream>
#include <string>


using namespace std;

class SetManager {
public:
    bool S[21] = {false}; 

    void add(int x) {
        if (S[x] == false){
            S[x] = true;
        }
    }

    void remove(int x) {
        if (S[x] == true){
            S[x] = false;
        }
    }

    int check(int x) {
        if (S[x] == true){
            return 1;
        }
        else {
            return 0;
        }
    }

    void toggle(int x) {
        if (S[x] == true){
            S[x] = false;
        }
        else if (S[x] == false){
            S[x] = true;
        }
    }

    void all() {
        for (int i=1; i<=20; i++){
            S[i] = true;
        }
    }

    void empty() {
        for (int i=1; i<=20; i++){
            S[i] = false;
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    SetManager sm;

    for (int i = 0; i < n; i++) {
        string command;
        int num;

        cin >> command;

        if (command == "add") {
            cin >> num; 
            sm.add(num);
        } 
        else if (command == "check") {
            cin >> num;
            cout << sm.check(num) << "\n";
        }
        else if (command == "remove") {
            cin >> num;
            sm.remove(num);
        }
        else if (command == "toggle") {
            cin >> num;
            sm.toggle(num);
        }
        else if (command == "all") {
            sm.all();
        }
        else if (command == "empty") {
            sm.empty();
        }
    }

    return 0;
}