import random
from datetime import timedelta

# Плейлисты из задания
playlist_a = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

playlist_f = (
    {"Free Bird": 9.08, "Enter Sandman": 5.31, "One": 7.45, "Sliver": 2.10, "Come as You Are": 3.45},
    {"Thunderstruck": 4.53, "You Shook Me All Night Long": 3.29, "Everlong": 4.51, "My Hero": 4.02},
)


def extract_songs_from_playlist(playlist):
    if isinstance(playlist, list):  # Проверка типа плейлиста
        return playlist
    elif isinstance(playlist, tuple):
        songs = []
        for dictionary in playlist:
            for song_name, duration in dictionary.items():
                songs.append([song_name, duration])
        return songs
    else:
        raise ValueError("Неверный формат плейлиста")


def get_random_songs(songs, n):
    if len(songs) < n:
        raise ValueError(f"Плейлист содержит меньше {n} песен")

    selected_songs = random.sample(songs, n)
    return selected_songs


def calculate_total_time(selected_songs):
    total_seconds = sum(duration for _, duration in selected_songs)
    return timedelta(seconds=total_seconds)


def get_duration(playlist, n):
    songs = extract_songs_from_playlist(playlist)
    selected_songs = get_random_songs(songs, n)
    total_time = calculate_total_time(selected_songs)
    return total_time


# Примеры вызова функции
print(get_duration(playlist_a, 3))
print(get_duration(playlist_f, 5))