
    // 인덱스 i는 i라는 노래의 장르정보 /  시행횟수
    // 정렬은 i라는 노래가 시행횟수가 장르별로 가장 많이 재생된 노래 두개 씩 모아 출시
    // 많이 재생된 장르 먼저, 장르 내에서 가장 많이 재생된 노래 두개

#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    unordered_map<string, int> genre; 
    unordered_map<string, vector<pair<int, int>>> songs_in_genre; // {재생수, 고유번호}

    for (int i = 0; i < genres.size(); i++) {
        genre[genres[i]] += plays[i];
        songs_in_genre[genres[i]].push_back({plays[i], i});
    }

    
    vector<pair<string, int>> genre_order(genre.begin(), genre.end());
    sort(genre_order.begin(), genre_order.end(), [](const pair<string, int>& a, const pair<string, int>& b) {
        return a.second > b.second; // python의 sort(key = lambda x: (x[1],x[0]))
    });

    vector<int> answer;

    //
    for (auto& g : genre_order) {
        string genre_name = g.first;
        auto& songs = songs_in_genre[genre_name];

        
        sort(songs.begin(), songs.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            if (a.first == b.first) return a.second < b.second; // 재생수 같으면 인덱스 오름차순
            return a.first > b.first; // 재생수 내림차순
        });

        //
        for (int i = 0; i < songs.size() && i < 2; i++) {
            answer.push_back(songs[i].second);
        }
    }

    return answer;
}