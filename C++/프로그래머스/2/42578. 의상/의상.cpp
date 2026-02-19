#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<vector<string>> clothes) {
    unordered_map<string , int> m;
    
    for (auto c : clothes){
        m[c[1]]++;
    }
    int ans = 1;
    for (auto pair : m){
        ans = (ans*(pair.second+1));
    }
    return ans-1;
}