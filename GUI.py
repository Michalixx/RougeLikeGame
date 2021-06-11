import PySimpleGUI as sg
import settings as stt
import stats


def display_gui():
    exit = False
    # sg.theme_previewer()
    sg.theme('DarkAmber')
    money = [sg.Text("Money: " + str(stt.money), key='-MONEY-')]

    hp = [sg.Text("Maximum HP: " + str(stt.MAX_HP), key='-HP-'), sg.Button("+10HP", key="-BUYHP-"),
          sg.Text(str(stt.MAX_HP * stt.hp_cost) + ' Gold', key='-COSTHP-')]

    red_bullet_text = [sg.Text("Red bullet (against Letters)")]

    print(stt.bullet_red_level)
    if stt.bullet_red_level != 4:
        red_bullet_size = [sg.Text("Bullet size: " + str(stt.bullet_red_level), key='-REDSIZE-'),
                    sg.Button("+1", key='-BUYREDSIZE-'),
                     sg.Text(str(stt.bullet_red_level * stt.bullet_lvl_cost) + " Gold", key='-COSTREDSIZE-')]
    else:
        red_bullet_size = [sg.Text("Bullet size: " + str(stt.bullet_red_level), key='-REDSIZE-'),
                           sg.Button("MAX", key='-BUYREDSIZE-'),
                           sg.Text("", key='-COSTREDSIZE-')]

    red_bullet_power = [sg.Text("Bullet power: " + str(stt.bullet_red_power), key="-REDPOWER-"),
                        sg.Button("+1", key='-BUYREDPOWER-'),
                        sg.Text(str(stt.bullet_red_power * stt.bullet_power_cost) + ' Gold', key='-COSTREDPOWER-')]

    red_bullet_speed = [sg.Text("Bullet speed: " + str(stt.bullet_red_speed), key='-REDSPEED-'),
                        sg.Button("+1", key='-BUYREDSPEED-'),
                        sg.Text(str(stt.bullet_red_speed * stt.bullet_speed_cost) + " Gold", key='-COSTREDSPEED-')]

    green_bullet_text = [sg.Text("Greeen bullet (against Numbers)")]

    if stt.bullet_green_level != 4:
        green_bullet_size = [sg.Text("Bullet size: " + str(stt.bullet_green_level), key='-GREENSIZE-'),
                         sg.Button("+1", key='-BUYGREENSIZE-'),
                         sg.Text(str(stt.bullet_green_level * stt.bullet_lvl_cost) + " Gold", key='-COSTGREENSIZE-')]
    else: green_bullet_size = [sg.Text("Bullet size: " + str(stt.bullet_green_level), key='-GREENSIZE-'),
                         sg.Button("MAX", key='-BUYGREENSIZE-'),
                         sg.Text("", key='-COSTGREENSIZE-')]

    green_bullet_power = [sg.Text("Bullet power: " + str(stt.bullet_green_power), key='-GREENPOWER-'),
                          sg.Button("+1", key='-BUYGREENPOWER-'),
                          sg.Text(str(stt.bullet_green_power * stt.bullet_power_cost) + ' Gold', key='-COSTGREENPOWER-')]

    green_bullet_speed = [sg.Text("Bullet speed: " + str(stt.bullet_green_speed), key='-GREENSPEED-'),
                          sg.Button("+1", key='-BUYGREENSPEED-'),
                          sg.Text(str(stt.bullet_green_speed * stt.bullet_speed_cost) + " Gold", key='-COSTGREENSPEED-')]

    blue_bullet_text = [sg.Text("Blue bullet (against Chars)")]

    if stt.bullet_blue_level != 4:
        blue_bullet_size = [sg.Text("Bullet size: " + str(stt.bullet_blue_level), key='-BLUESIZE-'),
                        sg.Button("+1", key='-BUYBLUESIZE-'),
                        sg.Text(str(stt.bullet_blue_level * stt.bullet_lvl_cost) + " Gold", key='-COSTBLUESIZE-')]
    else: blue_bullet_size = [sg.Text("Bullet size: " + str(stt.bullet_blue_level), key='-BLUESIZE-'),
                        sg.Button("MAX", key='-BUYBLUESIZE-'),
                        sg.Text("", key='-COSTBLUESIZE-')]

    blue_bullet_power = [sg.Text("Bullet power: " + str(stt.bullet_blue_power), key='-BLUEPOWER-'),
                         sg.Button("+1", key='-BUYBLUEPOWER-'),
                         sg.Text(str(stt.bullet_blue_power * stt.bullet_power_cost) + ' Gold', key='-COSTBLUEPOWER-')]

    blue_bullet_speed = [sg.Text("Bullet speed: " + str(stt.bullet_blue_speed), key='-BLUESPEED-'),
                         sg.Button("+1", key='-BUYBLUESPEED-'),
                         sg.Text(str(stt.bullet_blue_speed * stt.bullet_speed_cost) + " Gold", key='-COSTBLUESPEED-')]

    money_per_hit = [sg.Text("Money per hit: " + str(stt.money_per_hit), key='-MPH-'),
                     sg.Button("+1", key='-BUYMPH-'),
                     sg.Text(str(stt.money_per_hit*stt.money_per_hit_cost) + " Gold", key='-COSTMPH-')]

    player_speed = [sg.Text("Player speed: " + str(stt.player_speed), key='-PLAYERSPEED-'),
                    sg.Button("+0.1", key='-BUYPLAYERSPEED-'),
                    sg.Text(str(stt.player_speed*stt.player_speed_cost) + " Gold", key='-COSTPLAYERSPEED-')]

    play_button = [sg.Button("PLAY", key='-PLAY-')]

    col1 = [money, hp,  player_speed,
            money_per_hit, red_bullet_text, red_bullet_size, red_bullet_power, red_bullet_speed,
            green_bullet_text, green_bullet_size, green_bullet_power, green_bullet_speed,
            blue_bullet_text, blue_bullet_size, blue_bullet_power, blue_bullet_speed, play_button]

    time_played = [sg.Text("Total time played: " + str(stats.time_played))]
    bullet_red_fired = [sg.Text("Total red bullets fired: " + str(stats.bullet_red_fired))]
    bullet_green_fired = [sg.Text("Total green bullets fired: " + str(stats.bullet_green_fired))]
    bullet_blue_fired = [sg.Text("Total blue bullets fired: " + str(stats.bullet_blue_fired))]
    total_money_earned = [sg.Text("Total money earned: " + str(stats.total_money_earned))]
    letters_hits = [sg.Text("Letters hits: " + str(stats.letters_hits))]
    numbers_hits = [sg.Text("Numbers hits: " + str(stats.numbers_hits))]
    chars_hits = [sg.Text("Chars hits: " + str(stats.chars_hits))]
    letters_killed = [sg.Text("Letters killed: " + str(stats.letters_killed))]
    numbers_killed = [sg.Text("Numbers killed: " + str(stats.numbers_killed))]
    chars_killed = [sg.Text("Chars killed: " + str(stats.chars_killed))]
    total_wave_completed = [sg.Text("Total wave completed: " + str(stats.total_wave_completed))]
    reset_button = [sg.Button("RESET", key='-RESET-')]

    col2 = [time_played, bullet_red_fired, bullet_green_fired, bullet_blue_fired, total_money_earned,
            letters_hits, numbers_hits, chars_hits, letters_killed, numbers_killed, chars_killed,
            total_wave_completed, reset_button]

    layout = [[
        sg.Frame('Upgrades!', col1),
        sg.Frame("Stats!", col2)
    ]]
    window = sg.Window("Demo", layout)
    running = True
    while running:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            running = False
            exit = True
        if event == '-PLAY-':
            running = False

        if event == '-BUYHP-':
            if stt.money >= stt.MAX_HP * stt.hp_cost:
                stt.MAX_HP += stt.hp_increase
                stt.money -= stt.MAX_HP * stt.hp_cost
                window['-HP-'].update("Maximum HP: " + str(stt.MAX_HP))
                window['-COSTHP-'].update(str(stt.MAX_HP * stt.hp_cost) + ' Gold')
                window['-MONEY-'].update("Money: " + str(stt.money))
                stt.save_settings()

        if event == '-BUYREDSIZE-':
            if stt.bullet_red_level < 4:
                if stt.money >= stt.bullet_red_level * stt.bullet_lvl_cost:
                    stt.bullet_red_level += 1
                    stt.money -= stt.bullet_red_level * stt.bullet_lvl_cost
                    if stt.bullet_red_level < 4:
                        window['-COSTREDSIZE-'].update(str(stt.bullet_red_level * stt.bullet_lvl_cost) + " Gold")
                    else:
                        window['-COSTREDSIZE-'].update("")
                        window['-BUYREDSIZE-'].update('MAX')
                    window['-REDSIZE-'].update("Bullet size: " + str(stt.bullet_red_level))
                    window['-MONEY-'].update("Money: " + str(stt.money))
                    stt.save_settings()

        if event == '-BUYREDPOWER-':
            if stt.money >= stt.bullet_red_power * stt.bullet_power_cost:
                stt.money -= stt.bullet_red_power * stt.bullet_power_cost
                stt.bullet_red_power += stt.bullet_power_increase
                window["-REDPOWER-"].update("Bullet power: " + str(stt.bullet_red_power))
                window['-COSTREDPOWER-'].update(str(stt.bullet_red_power * stt.bullet_power_cost) + ' Gold')
                window['-MONEY-'].update("Money: " + str(stt.money))
                stt.save_settings()

        if event == '-BUYREDSPEED-':
            if stt.money >= stt.bullet_red_speed * stt.bullet_speed_cost:
                stt.money -= stt.bullet_red_speed * stt.bullet_speed_cost
                stt.bullet_red_speed += stt.bullet_speed_increase
                window['-REDSPEED-'].update("Bullet speed: " + str(stt.bullet_red_speed))
                window['-COSTREDSPEED-'].update(str(stt.bullet_red_speed * stt.bullet_speed_cost) + " Gold")
                window['-MONEY-'].update("Money: " + str(stt.money))
                stt.save_settings()

        if event == '-BUYGREENSIZE-':
            if stt.bullet_green_level < 4:
                if stt.money >= stt.bullet_green_level * stt.bullet_lvl_cost:
                    stt.bullet_green_level += 1
                    stt.money -= stt.bullet_green_level * stt.bullet_lvl_cost
                    if stt.bullet_green_level < 4:
                        window['-COSTGREENSIZE-'].update(str(stt.bullet_green_level * stt.bullet_lvl_cost) + " Gold")
                    else:
                        window['-COSTGREENSIZE-'].update("")
                        window['-BUYGREENSIZE-'].update('MAX')
                    window['-GREENSIZE-'].update("Bullet size: " + str(stt.bullet_green_level))
                    window['-MONEY-'].update("Money: " + str(stt.money))
                    stt.save_settings()

        if event == '-BUYGREENPOWER-':
            if stt.money >= stt.bullet_green_power * stt.bullet_power_cost:
                stt.money -= stt.bullet_green_power * stt.bullet_power_cost
                stt.bullet_green_power += stt.bullet_power_increase
                window["-GREENPOWER-"].update("Bullet power: " + str(stt.bullet_green_power))
                window['-COSTGREENPOWER-'].update(str(stt.bullet_green_power * stt.bullet_power_cost) + ' Gold')
                window['-MONEY-'].update("Money: " + str(stt.money))
                stt.save_settings()

        if event == '-BUYGREENSPEED-':
            if stt.money >= stt.bullet_green_speed * stt.bullet_speed_cost:
                stt.money -= stt.bullet_green_speed * stt.bullet_speed_cost
                stt.bullet_green_speed += stt.bullet_speed_increase
                window['-GREENSPEED-'].update("Bullet speed: " + str(stt.bullet_green_speed))
                window['-COSTGREENSPEED-'].update(str(stt.bullet_green_speed * stt.bullet_speed_cost) + " Gold")
                window['-MONEY-'].update("Money: " + str(stt.money))
                stt.save_settings()

        if event == '-BUYBLUESIZE-':
            if stt.bullet_blue_level < 4:
                if stt.money >= stt.bullet_blue_level * stt.bullet_lvl_cost:
                    stt.bullet_blue_level += 1
                    stt.money -= stt.bullet_blue_level * stt.bullet_lvl_cost
                    if stt.bullet_blue_level < 4:
                        window['-COSTBLUESIZE-'].update(str(stt.bullet_blue_level * stt.bullet_lvl_cost) + " Gold")
                    else:
                        window['-COSTBLUESIZE-'].update("")
                        window['-BUYBLUESIZE-'].update('MAX')
                    window['-BLUESIZE-'].update("Bullet size: " + str(stt.bullet_blue_level))
                    window['-MONEY-'].update("Money: " + str(stt.money))
                    stt.save_settings()

        if event == '-BUYBLUEPOWER-':
            if stt.money >= stt.bullet_blue_power * stt.bullet_power_cost:
                stt.money -= stt.bullet_blue_power * stt.bullet_power_cost
                stt.bullet_blue_power += stt.bullet_power_increase
                window["-BLUEPOWER-"].update("Bullet power: " + str(stt.bullet_blue_power))
                window['-COSTBLUEPOWER-'].update(str(stt.bullet_blue_power * stt.bullet_power_cost) + ' Gold')
                window['-MONEY-'].update("Money: " + str(stt.money))
                stt.save_settings()

        if event == '-BUYBLUESPEED-':
            if stt.money >= stt.bullet_blue_speed * stt.bullet_speed_cost:
                stt.money -= stt.bullet_blue_speed * stt.bullet_speed_cost
                stt.bullet_blue_speed += stt.bullet_speed_increase
                window['-BLUESPEED-'].update("Bullet speed: " + str(stt.bullet_blue_speed))
                window['-COSTBLUESPEED-'].update(str(stt.bullet_blue_speed * stt.bullet_speed_cost) + " Gold")
                window['-MONEY-'].update("Money: " + str(stt.money))
                stt.save_settings()

        if event == '-BUYMPH-':
            if stt.money >= stt.money_per_hit*stt.money_per_hit_cost:
                stt.money -= stt.money_per_hit*stt.money_per_hit_cost
                stt.money_per_hit += stt.money_per_hit_increase
                window['-MPH-'].update("Money per hit: " + str(stt.money_per_hit))
                window['-COSTMPH-'].update(str(stt.money_per_hit*stt.money_per_hit_cost) + " Gold")
                window['-MONEY-'].update("Money: " + str(stt.money))
                stt.save_settings()

        if event == '-BUYPLAYERSPEED-':
            if stt.money >= stt.player_speed*stt.player_speed_cost:
                stt.money -= stt.player_speed*stt.player_speed_cost
                stt.player_speed += stt.player_speed_increase
                window['-PLAYERSPEED-'].update("Player speed: " + str(stt.player_speed))
                window['-COSTPLAYERSPEED-'].update(str(stt.player_speed*stt.player_speed_cost) + " Gold")
                window['-MONEY-'].update("Money: " + str(stt.money))
                stt.save_settings()

        if event == '-RESET-':
            stt.reset_settings()
            stats.reset_stats()
            stt.save_settings()
            stats.save_stats()
            running = False

    window.close()
    if exit:
        return 1
    else:
        return 0
