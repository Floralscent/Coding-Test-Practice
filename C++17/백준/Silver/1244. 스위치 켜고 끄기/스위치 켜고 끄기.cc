#include <iostream>
#include <vector>

using namespace std;

void Man(vector<bool> &l, int i,int num){
    for(int k=1; k<num+1;k++){
        if (k%i==0) l[k] = !l[k];
    }
    return ;
}

void Girl(vector<bool> &l, int i, int num) {
    l[i] = !l[i]; 
    int k = 1;
    while (i - k >= 1 && i + k <= num && l[i - k] == l[i + k]) { //경계조건 주의
        l[i - k] = !l[i - k];
        l[i + k] = !l[i + k];
        k++;
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num;
    int num_st;
    cin>>num;
    vector<bool> s(num+1);
    for(int i=1; i<num+1;i++){
        bool tmp;
        cin>>tmp;
        s[i] = tmp;
    }
    cin>>num_st; 
    for (int j = 0; j<num_st; j++){
        int mode;
        int idx;
        cin >>mode>>idx;
        if (mode == 1){
            Man(s,idx,num);
        }
        else Girl(s,idx,num);
    }
    
    for (int i = 1; i <= num; i++) {
    cout << s[i];
    if (i % 20 == 0 || i == num) {
        cout << "\n";
    } else {
        cout << " ";
    }
    }
    // system("pause");
    return 0;
}