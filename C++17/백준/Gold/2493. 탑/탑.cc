#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;


    vector<pair<int, int>> v(n);
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        v[i].first = val;    
        v[i].second = i + 1; 
    }

    vector<int> ans(n);
    stack<pair<int, int>> st;
    int idx = 0;


    while (idx < n) {
        
        while (!st.empty() && st.top().first < v[idx].first) {
            st.pop();
        }

        //
        if (st.empty()) {
            ans[idx] = 0;
        } else {
            ans[idx] = st.top().second; 
        }

        //
        st.push(v[idx]); 
        idx++;
    }

    //
    for (int i = 0; i < n; i++) {
        cout << ans[i] << " ";
    }

    return 0;
}