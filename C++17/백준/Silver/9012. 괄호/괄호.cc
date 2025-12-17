#include <iostream>
#include <string>
#include <stack>

using namespace std;

bool isBal(string str){
    stack<char> st;
    
    for(char ch:str){
        // str 만큼 각각 ch로 반복 여는거면 넣고
        if (ch == '(' || ch == '{' || ch == '['){
            st.push(ch);
        }
        // 닫는거면 확인
        else if (ch ==')' || ch =='}' || ch ==']'){
            if (st.empty()){
                return false;
            }
            //
            char top = st.top();
            if (ch ==')' && top !='(' || ch =='}' && top !='{' || ch ==']' && top != '['){
                return false;
            }
            else {
                st.pop();
            }
        }
    }
    return st.empty();
}

/**/
int main(){
    int t;
    string str;
    //cout<<"Start"<<endl;
    cin >> t;
    for(int i = 0; i<t; i++){
        cin >> str;
        if (isBal(str)){ //isBal, isbalanced
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}