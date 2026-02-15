#include <iostream>
#include <string>

using namespace std;

bool vol(char c) {
    return (c == 'a' || c == 'o' || c == 'e' || c == 'i' || c == 'u');
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string w;
    while (cin >> w && w != "end") {
        int s = w.length();
        bool tmp1 = false; 
        bool tmp2 = true;  
        bool tmp3 = true;  
        // condition1
        for (char c : w) {
            if (vol(c)) {
                tmp1 = true;
                break;
            }
        }

        // condition2
        if (s >= 3) {
            for (int j = 2; j < s; j++) {
                bool v1 = vol(w[j - 2]);
                bool v2 = vol(w[j - 1]);
                bool v3 = vol(w[j]);
                if (v1 == v2 && v2 == v3) {
                    tmp2 = false;
                    break;
                }
            }
        }

        // condition3
        for (int i = 1; i < s; i++) {
            if (w[i - 1] == w[i]) {
                if (w[i] != 'e' && w[i] != 'o') {
                    tmp3 = false;
                    break;
                }
            }
        }

        string text = (tmp1 && tmp2 && tmp3) ? " is acceptable." : " is not acceptable.";
        cout << "<" << w << ">" << text << "\n";
    }
    return 0;
}