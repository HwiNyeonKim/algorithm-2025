from collections import defaultdict


def solution(genres, plays):
    records = defaultdict(list)
    for index, (genre, play) in enumerate(zip(genres, plays)):
        records[genre].append((play, index))

    # 1. 각 장르별 베스트 2곡을 찾는다.
    genre_stats = dict()
    for genre, songs in records.items():
        # 재생횟수의 내림차순(-x[0]) & 고유번호의 오름차순(x[1])으로 정렬
        song_played_sorted = sorted(songs, key=lambda x: (-x[0], x[1]))
        total_played = sum(play for play, _ in songs)
        genre_stats[genre] = (total_played, song_played_sorted[:2])

    # 2. 장르 순위 결정 - 총 재생 횟수 기준 내림차순 정렬
    sorted_genre_stats = sorted(
        genre_stats.items(), key=lambda item: item[1][0], reverse=True
    )

    return [
        index for _, (_, songs) in sorted_genre_stats for _, index in songs
    ]
