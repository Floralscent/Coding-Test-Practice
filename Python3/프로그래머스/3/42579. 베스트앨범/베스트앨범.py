from collections import defaultdict
def solution(genres, plays):
    
    answer = []
    g_dict = defaultdict(int)
    music = defaultdict(list)
    
    
    for i in range(len(genres)):
        g_dict[genres[i]] += plays[i]
        music[genres[i]].append((plays[i], i))
    #
    genre_play_pairs = []
    
    for genre_name, total_plays in g_dict.items():
        genre_play_pairs.append((total_plays, genre_name))

    #
    genre_play_pairs.sort(reverse=True)
    
    for cnt,g in genre_play_pairs:
        music[g].sort(key=lambda x: (-x[0], x[1]))

        # 장르별로 최대 2곡까지만 앨범에 수록
        for i in range(min(len(music[g]), 2)):
            answer.append(music[g][i][1])

    return answer