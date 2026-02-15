#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    vector<vector<int>> graph(t + 1, vector<int>(t + 1));
    char c;
    for (int i = 1; i <= t; i++) {
        for (int j = 1; j <= t; j++) {
            cin >> c;
            graph[i][j] = (c == '*') ? 1 : 0;
        }
    }

    int head_i = 0, head_j = 0;
    bool found = false;
    for (int i = 1; i <= t; i++) {
        for (int j = 1; j <= t; j++) {
            if (graph[i][j] == 1) {
                head_i = i;
                head_j = j;
                found = true;
                break;
            }
        }
        if (found) break;
    }

    int heart_i = head_i + 1;
    int heart_j = head_j;

    int left_arm = 0;
    for (int j = heart_j - 1; j >= 1; j--) {
        if (graph[heart_i][j] == 1) left_arm++;
        else break;
    }

    int right_arm = 0;
    for (int j = heart_j + 1; j <= t; j++) {
        if (graph[heart_i][j] == 1) right_arm++;
        else break;
    }

    int sp = 0;
    int sp_end_i = heart_i;
    for (int i = heart_i + 1; i <= t; i++) {
        if (graph[i][heart_j] == 1) {
            sp++;
            sp_end_i = i;
        }
        else break;
    }

    int l_leg = 0;
    for (int i = sp_end_i + 1; i <= t; i++) {
        if (graph[i][heart_j - 1] == 1) l_leg++;
        else break;
    }

    int r_leg = 0;
    for (int i = sp_end_i + 1; i <= t; i++) {
        if (graph[i][heart_j + 1] == 1) r_leg++;
        else break;
    }

    cout << heart_i << " " << heart_j << "\n";
    cout << left_arm << " " << right_arm << " " << sp << " " << l_leg << " " << r_leg << "\n";

    return 0;
}