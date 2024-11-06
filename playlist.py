def process_playlist(playlist):
    if playlist == 'плейлист_1':
        return 'Результат обработки плейлиста 1'
    elif playlist == 'плейлист_2': 
        return 'Результат обработки плейлиста 2'
    else:
        raise ValueError('Неизвестный плейлист')