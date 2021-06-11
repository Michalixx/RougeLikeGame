# stats
time_played = 0
bullet_red_fired = 0
bullet_green_fired = 0
bullet_blue_fired = 0
total_money_earned = 0
letters_hits = 0
numbers_hits = 0
chars_hits = 0
letters_killed = 0
numbers_killed = 0
chars_killed = 0
total_wave_completed = 0


def reset_stats():
    global time_played
    global bullet_red_fired
    global bullet_green_fired
    global bullet_blue_fired
    global total_money_earned
    global letters_hits
    global numbers_hits
    global chars_hits
    global letters_killed
    global numbers_killed
    global chars_killed
    global total_wave_completed
    time_played = 0
    bullet_red_fired = 0
    bullet_green_fired = 0
    bullet_blue_fired = 0
    total_money_earned = 0
    letters_hits = 0
    numbers_hits = 0
    chars_hits = 0
    letters_killed = 0
    numbers_killed = 0
    chars_killed = 0
    total_wave_completed = 0


def load_stats():  # load stats from file

    global time_played
    global bullet_red_fired
    global bullet_green_fired
    global bullet_blue_fired
    global total_money_earned
    global letters_hits
    global numbers_hits
    global chars_hits
    global letters_killed
    global numbers_killed
    global chars_killed
    global total_wave_completed

    with open('stats.txt') as reader:  # file name
        time_played = float(reader.readline())
        bullet_red_fired = int(reader.readline())
        bullet_green_fired = int(reader.readline())
        bullet_blue_fired = int(reader.readline())
        total_money_earned = int(reader.readline())
        letters_hits = int(reader.readline())
        numbers_hits = int(reader.readline())
        chars_hits = int(reader.readline())
        letters_killed = int(reader.readline())
        numbers_killed = int(reader.readline())
        chars_killed = int(reader.readline())
        total_wave_completed = int(reader.readline())


def save_stats():
    with open('stats.txt', 'w') as reader:
        reader.write(str(time_played) + "\n")
        reader.write(str(bullet_red_fired) + "\n")
        reader.write(str(bullet_green_fired) + "\n")
        reader.write(str(bullet_blue_fired) + "\n")
        reader.write(str(total_money_earned) + "\n")
        reader.write(str(letters_hits) + "\n")
        reader.write(str(numbers_hits) + "\n")
        reader.write(str(chars_hits) + "\n")
        reader.write(str(letters_killed) + "\n")
        reader.write(str(numbers_killed) + "\n")
        reader.write(str(chars_killed) + "\n")
        reader.write(str(total_wave_completed) + "\n")




