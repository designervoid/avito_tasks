import time
import sys
import random

dict_stats = {
    'health_points': 0,
    'food_points': 0,
    'water_points': 0,
    'money_points': 0
}

string_health = 'Health: {}'
string_food = 'Food: {}'
string_water = 'Water: {}'
string_money = 'Money: {}'

greeting_in_the_beginning = ('''
    Hello. It's simple RPG game where you are awake and you can choose:
    a) Explore your house, where you are wake up
    b) Go to the Taverna, and have fun!


    Choose your LVL of game: 
    1. Easy
    2. Medium
    3. Hard
    ''')

action_main_moves = ('''
           Your main moves:
           1. Explore your home
           2. Go to the Taverna
           3. Continue to sleep
           Input your move to continue the game:
           ''')

actions_in_home = ('''
       Your moves:
       a. Go to the safe, take the money
       b. Go to the kitchen, take some food, if y r hungry.
       c. Go to the bed, and takeover of sleep.
       d. Stop explore the home and go to Taverna.
       Input your move to continue the game:
       ''')

actions_in_taverna = ('''
                   Your moves:
                   You are in Taverna. Explore it. 
                   a. Go to the bar.
                   b. Go to the food bar.
                   c. Go to the tables, you can play card games.
                   d. Go to the music station.
                   e. Go home.
                   Input your move to continue the game.
                   ''')

choose_lvl = ('''Choose your LVL of game: 
                 1. Easy
                 2. Medium
                 3. Hard
              ''')


def stats_of_player():
    print('\n ', string_health.format(dict_stats['health_points']))
    print(' ', string_food.format(dict_stats['food_points']))
    print(' ', string_water.format(dict_stats['water_points']))
    print(' ', string_money.format(dict_stats['money_points']))


def increase_parameter(parameter, delta):
    dict_stats[parameter] += delta
    dict_stats[parameter] = min(100, dict_stats[parameter])


def decrease_parameter(parameter, delta):
    dict_stats[parameter] -= delta
    dict_stats[parameter] = max(0, dict_stats[parameter])


def game_lvl_selection(self, points=100):
    print(self)
    player_lvl_selection = int(input())
    points //= player_lvl_selection

    dict_stats['health_points'] = points
    dict_stats['food_points'] = points
    dict_stats['water_points'] = points
    dict_stats['money_points'] = points


def wake_up_at_start_of_game():
    stats_of_player()


def animation_of_sleeping():
    for x in range(100):
        time.sleep(0.1)
        sys.stdout.write(f'\r{x + 1}%')
        sys.stdout.write(' sleeping... zzzz..')
        sys.stdout.flush()


def animation_of_walking(s=0.1):
    for y in range(100):
        time.sleep(s)
        sys.stdout.write(f'\r{y + 1}%')
        sys.stdout.write(' loading... ')
        sys.stdout.flush()


def variation_of_actions_home(self, redress_hp=1, eat_food=4, drink_water=2, take_money=100):
    stats_of_player()
    print(self)
    move = str(input()).lower()
    while move == 'a' \
            or move == 'b' \
            or move == 'c' \
            or move == 'd':
        if move == 'a':
            animation_of_walking(0.01)
            dict_stats['money_points'] += take_money
            variation_of_actions_home(actions_in_home)

        elif move == 'b':
            animation_of_walking(0.01)
            # for enumerate
            increase_parameter('health_points', redress_hp)
            increase_parameter('food_points', eat_food)
            increase_parameter('water_points', drink_water)
            variation_of_actions_home(actions_in_home)

        elif move == 'c':
            animation_of_sleeping()
            variation_of_actions_home(actions_in_home)

        elif move == 'd':
            animation_of_walking()
            variation_of_actions_taverna(actions_in_taverna)
    print('You input wrong symbol!')
    variation_of_actions_home(actions_in_home)


def variation_of_actions_taverna(self):
    if dict_stats['health_points'] > 0:
        animation_of_walking(0.01)
        stats_of_player()
        print(self)
        move = str(input()).lower()
        while move == 'a' \
                or move == 'b' \
                or move == 'c' \
                or move == 'd' \
                or move == 'e':
            if move == 'a':
                animation_of_walking(0.01)
                dict_bar = {'1': 'vodka', '2': 'beer'}
                stats_of_player()
                print('Choose your drink: ' + '\n1: ' + str(dict_bar['1']) \
                      + '\n2: ' + str(dict_bar['2']) + '\n Input')
                action_in_bar = str(input())
                print(dict_bar[action_in_bar])
                decrease_parameter('health_points', 5)
                variation_of_actions_taverna(actions_in_taverna)
            elif move == 'b':
                animation_of_walking(0.01)
                dict_food_bar = {'1': 'sandwich', '2': 'nuggets'}
                stats_of_player()
                print('Choose your good: ' + '\n1: ' + str(dict_food_bar['1']) \
                      + '\n2: ' + str(dict_food_bar['2']) + '\n Input')
                action_in_food_bar = str(input())
                print(dict_food_bar[action_in_food_bar])
                increase_parameter('health_points', 1)
                increase_parameter('food_points', 4)
                increase_parameter('water_points', 2)
                variation_of_actions_taverna(actions_in_taverna)

            elif move == 'c':
                animation_of_walking(0.01)
                dict_bar = {
                    '1': 'player1', '2': 'player2', '3': 'player3',
                    '4': 'player4', '5': 'player5', '6': 'player6',
                    '7': 'player7', '8': 'player9', '9': 'player9',
                    '10': 'player10'
                }
                print('Choose your opponent: \n1:' + str(dict_bar['1']) + \
                      '\n... \n10:' + str(dict_bar['10']) + '\n Input')
                action_in_tables = str(input())
                print(dict_bar[action_in_tables])
                deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
                random.shuffle(deck)
                print('Let\'s play twenty-one' + '\n' + 'Make a bet:')
                bet = float(input())
                if dict_stats['money_points'] - bet * 1.4 < 0:
                    print('Very big bet, you can back later')
                    variation_of_actions_taverna(actions_in_taverna)
                else:
                    count = 0
                    want_continue = True
                    while count < 21 and want_continue:
                        print('You have %d points.' % count)
                        current = deck.pop()
                        print('You got the card worth %d' % current)
                        count += current
                        want_continue = input('Wanna take more '
                                              'card? y/n\n') == 'y'
                    if count == 21:
                        print('Yep, you\'ve scored!')
                        dict_stats['money_points'] += bet * 1.2
                        variation_of_actions_taverna(actions_in_taverna)
                    else:
                        dict_stats['money_points'] -= bet * 1.4
                        variation_of_actions_taverna(actions_in_taverna)
                        if count > 21:
                            print('Sorry, but you lost')
                        if count < 21:
                            print('You have %d points and you\'ve finished the game' % count)

            elif move == 'd':
                animation_of_walking(0.01)
                dict_taverna_music = {
                    '1': 'artist_1 - song_name_1',
                    '2': 'artist_2 - song_name_2',

                }
                choice_in_bar = input('Wanna listen music? y/n\n').lower()
                while choice_in_bar == 'y':
                    stats_of_player()
                    print(
                        'Choice of music in playlist: ' + str(dict_taverna_music['1']) + '\n' + \
                        str(dict_taverna_music['2']) + '\n Input')
                    action_in_taverna_music = str(input())
                    print(dict_taverna_music[action_in_taverna_music])
                    dict_stats['money_points'] -= 10
                    choice_in_taverna_music_again = input('Wanna change music? y/n\n').lower()
                    if choice_in_taverna_music_again == 'y':
                        continue
                    else:
                        break
                variation_of_actions_taverna(actions_in_taverna)

            elif move == 'e':
                animation_of_walking()
                variation_of_actions_home(actions_in_home)
        print('You input wrong symbol!')
        variation_of_actions_taverna(actions_in_taverna)
    else:
        death_in_game()
        print(action_main_moves)


def continue_of_sleeping(self):
    animation_of_sleeping()
    print('\nWake Up!', 'Choose your path!')
    stats_of_player()
    print(self)


def moves_in_game():
    move = str(input())
    if move == '1':
        variation_of_actions_home(actions_in_home)

    elif move == '2':
        variation_of_actions_taverna(actions_in_taverna)

    elif move == '3':
        continue_of_sleeping(action_main_moves)


def death_in_game():
    print(string_health + str(dict_stats['health_points']) + '\n' +
          string_food + str(dict_stats['food_points']) + '\n' +
          string_water + str(dict_stats['water_points']) + '\n' +
          string_money + str(dict_stats['money_points']))
    print('Wasted')
    replay_game = input('Want replay? y/n\n').lower()
    if replay_game == 'y':
        game_lvl_selection(choose_lvl)


def the_course_of_the_game(i=0, hunger=10, thirst=20, decrease_health_from_hunger_and_thirst=10):
    print(action_main_moves)
    while dict_stats['health_points'] > 0:
        moves_in_game()
        i += 1
        print(i)
        if i % 2 == 0:
            decrease_parameter('food_points', hunger)
            decrease_parameter('water_points', thirst)
            decrease_parameter('health_points', decrease_health_from_hunger_and_thirst)
    death_in_game()


if __name__ == '__main__':
    game_lvl_selection(greeting_in_the_beginning)
    wake_up_at_start_of_game()
    the_course_of_the_game()