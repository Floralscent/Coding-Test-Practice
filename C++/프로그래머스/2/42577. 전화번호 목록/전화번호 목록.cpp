#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(), phone_book.end());
    for (int i = 1; i<phone_book.size(); i++){
            if (phone_book[i].find(phone_book[i-1]) ==0){
                answer = false;
                return answer;
            }
    }
    //pyton의 startswith > find() ==0 endswith >> rfind() == str.length() - tar.length() 
    return answer;
}