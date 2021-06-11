# game settings
MAX_HP = 10
money = 0

bullet_red_level = 1
bullet_red_speed = 10
bullet_red_power = 1

bullet_green_level = 1
bullet_green_speed = 10
bullet_green_power = 1

bullet_blue_level = 1
bullet_blue_speed = 10
bullet_blue_power = 1

money_per_hit = 1
player_speed = 10

# upgrade cost = cost * lvl
hp_cost = 100
bullet_lvl_cost = 1000
bullet_speed_cost = 200
bullet_power_cost = 50
money_per_hit_cost = 10000
player_speed_cost = 1000

# increase per upgrade
hp_increase = 10
bullet_speed_increase = 1
bullet_power_increase = 1
money_per_hit_increase = 1
player_speed_increase = 1


def reset_settings():
    global MAX_HP
    global money
    global bullet_red_power
    global bullet_red_speed
    global bullet_red_level
    global bullet_green_level
    global bullet_green_speed
    global bullet_green_power
    global bullet_blue_level
    global bullet_blue_speed
    global bullet_blue_power
    global money_per_hit
    global player_speed

    MAX_HP = 10
    money = 0

    bullet_red_level = 1
    bullet_red_speed = 10
    bullet_red_power = 1

    bullet_green_level = 1
    bullet_green_speed = 10
    bullet_green_power = 1

    bullet_blue_level = 1
    bullet_blue_speed = 10
    bullet_blue_power = 1

    money_per_hit = 1
    player_speed = 10


def load_settings():

    global MAX_HP
    global money
    global bullet_red_power
    global bullet_red_speed
    global bullet_red_level
    global bullet_green_level
    global bullet_green_speed
    global bullet_green_power
    global bullet_blue_level
    global bullet_blue_speed
    global bullet_blue_power
    global money_per_hit
    global player_speed

    with open('settings.txt') as reader:
        MAX_HP = int(reader.readline())
        money = int(reader.readline())
        bullet_red_level = int(reader.readline())
        bullet_red_speed = int(reader.readline())
        bullet_red_power = int(reader.readline())
        bullet_green_level = int(reader.readline())
        bullet_green_speed = int(reader.readline())
        bullet_green_power = int(reader.readline())
        bullet_blue_level = int(reader.readline())
        bullet_blue_speed = int(reader.readline())
        bullet_blue_power = int(reader.readline())
        money_per_hit = int(reader.readline())
        player_speed = int(reader.readline())


def display_settings():
    print(MAX_HP)


def save_settings():
    with open('settings.txt', 'w') as reader:
        reader.write(str(MAX_HP)+"\n")
        reader.write(str(money)+"\n")
        reader.write(str(bullet_red_level)+"\n")
        reader.write(str(bullet_red_speed)+"\n")
        reader.write(str(bullet_red_power)+"\n")
        reader.write(str(bullet_green_level)+"\n")
        reader.write(str(bullet_green_speed)+"\n")
        reader.write(str(bullet_green_power)+"\n")
        reader.write(str(bullet_blue_level)+"\n")
        reader.write(str(bullet_blue_speed)+"\n")
        reader.write(str(bullet_blue_power)+"\n")
        reader.write(str(money_per_hit)+"\n")
        reader.write(str(player_speed)+"\n")




