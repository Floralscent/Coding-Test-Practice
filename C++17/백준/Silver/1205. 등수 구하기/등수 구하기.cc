#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    int n;
    int score;
    int num_rank;
    int ans;
    
    ans = -1;
    cin>>n>>score>>num_rank;
    int min_score;

    vector<int> lst;
    // lst.push_back(score);
    for(int i=0; i<n;i++){
        int tmp;
        cin>>tmp;
        lst.push_back(tmp);
    }

    if (lst.size() < num_rank){
        lst.push_back(score);
        
    }
    else{
        min_score = *min_element(lst.begin(),lst.end());
        if (min_score >= score){
            ans = -1;
            cout<<ans<<"\n";
            return 0;
        }
        else lst.push_back(score);
    }
    //
    sort(lst.begin(),lst.end(),greater<int>());
    auto it = find(lst.begin(), lst.end(), score);
    int idx = distance(lst.begin(), it);
    cout << idx + 1;

    
    return 0;
}