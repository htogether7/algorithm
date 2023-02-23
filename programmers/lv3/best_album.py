from collections import defaultdict
def solution(genres, plays):
    answer = []
    genre_count = defaultdict(int)
    song_count = defaultdict(list)
    
    for num in range(len(genres)):
        genre_count[genres[num]] += plays[num]
        song_count[genres[num]].append((plays[num], num))
        
    genre_array = []
    for key in genre_count:
        genre_array.append((genre_count[key],key))
    genre_array.sort(key = lambda x : -x[0])

    for key in song_count:
        song_count[key].sort(key = lambda x : (-x[0], x[1]))

    answer = []
    for _, genre in genre_array:
        answer.append(song_count[genre][0][1])
        if len(song_count[genre]) > 1:
            answer.append(song_count[genre][1][1])
    return answer