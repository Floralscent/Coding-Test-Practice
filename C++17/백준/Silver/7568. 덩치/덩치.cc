#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// 순위를 매길 수 없는 경우가 있으니 브루트 포스로 

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    vector<vector<int>> v(n, vector<int>(2));

    for (int i = 0; i < n; i++) {
        cin >> v[i][0] >> v[i][1]; 
    }

    //
    for (int i = 0; i < n; i++) {
        int rank = 1; 
        
        for (int j = 0; j < n; j++) {
            if (i == j) continue; //

            // 다른애가 키와 몸무게 둘다 클 경우에만 
            if (v[j][0] > v[i][0] && v[j][1] > v[i][1]) {
                rank++;// 딴애 나보다 크다면 등수가 커짐(뒤로 밀려)
            }
        }
        cout << rank << " ";
    }

    return 0;
}