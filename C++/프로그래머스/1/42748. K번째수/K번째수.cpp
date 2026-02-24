#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    
    vector<int> answer;
    int ans;
    for (int h  = 0; h< commands.size(); h++){
        int i,j,k;
        i = commands[h][0];
        j = commands[h][1];
        k = commands[h][2];
        vector<int> tmp(array.begin() + i - 1, array.begin() + j);
        sort(tmp.begin(), tmp.end());
        ans = tmp[k-1];
        answer.push_back(ans);
    }
    
    return answer;
}