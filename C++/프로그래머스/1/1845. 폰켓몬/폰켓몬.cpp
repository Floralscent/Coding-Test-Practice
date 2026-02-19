#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_set>

using namespace std;

int solution(vector<int> nums){
    unordered_set<int> s(nums.begin(),nums.end());
    
    int mx;
    mx = nums.size()/2;
    
    int answer = min((int)s.size(),mx);
    return answer;
    
    
}