import time
import sys
import random

dict_stats = {
    'health_points': 0,  # очки здоровья
    'food_points': 0,  # очки голода
    'water_points': 0,  # очки жажды
    'money_points': 0  # кол-во денег
}

HEALTH_POINTS = 'Health: {}'
FOOD_POINTS = 'Food: {}'
WATER_POINTS = 'Water: {}'
MONEY_POINTS = 'Money: {}'

greeting_in_the_beginning = '''    
                            Hello. 
                            It's simple RPG game where you can choose:
                            a) Explore your house, where you are wake up
                            b) Go to the Taverna, and have fun!
                            '''

action_main_moves = '''    
                    Your main moves:
                    1. Explore your home
                    2. Go to the Taverna
                    3. Continue to sleep
                    Input your move to continue the game:
                    '''

actions_in_home = '''      
                  Your moves:
                  a. Go to the safe, take the money
                  b. Go to the kitchen, take some food, if y r hungry.
                  c. Go to the bed, and takeover of sleep.
                  d. Stop explore the home and go to Taverna.
                  Input your move to continue the game:
                  '''

actions_in_taverna = '''   
                     Your moves:
                     You are in Taverna. Explore it. 
                     a. Go to the bar.
                     b. Go to the food bar.
                     c. Go to the tables, you can play card games.
                     d. Go to the music station.
                     e. Go home.
                     Input your move to continue the game.
                     '''

choose_lvl = '''
             Choose your LVL of game:  
             1. Easy
             2. Medium
             3. Hard
             '''


def stats_of_player():
    print('\n', HEALTH_POINTS.format(dict_stats['health_points']))
    print('', FOOD_POINTS.format(dict_stats['food_points']))
    print('', WATER_POINTS.format(dict_stats['water_points']))
    print('', MONEY_POINTS.format(dict_stats['money_points']))


def increase_parameter(parameter, delta):
    dict_stats[parameter] += delta
    dict_stats[parameter] = min(100, dict_stats[parameter])


def decrease_parameter(parameter, delta):
    dict_stats[parameter] -= delta
    dict_stats[parameter] = max(0, dict_stats[parameter])


def game_lvl_selection(text, points=100):
    print(text)
    player_lvl_selection = int(input())
    points //= player_lvl_selection
    valid_select = (1, 2, 3)
    while player_lvl_selection not in valid_select:
        print('Wrong value, try again')
        game_lvl_selection(choose_lvl)
    else:
        dict_stats['health_points'], dict_stats['food_points'] = points, points
        dict_stats['water_points'], dict_stats['money_points'] = points, points


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


def variation_of_actions_home(text, hp_up=1, eat=4, drink=2, money_up=100):
    stats_of_player()
    print(text)
    move = input().lower()
    valid_move = ('a', 'b', 'c', 'd')
    while move not in valid_move:
        print('You input wrong symbol!')
        variation_of_actions_home(actions_in_home)
    else:
        if move == 'a':
            animation_of_walking(0.01)
            dict_stats['money_points'] += money_up
            variation_of_actions_home(actions_in_home)

        elif move == 'b':
            animation_of_walking(0.01)
            increase_parameter('health_points', hp_up)
            increase_parameter('food_points', eat)
            increase_parameter('water_points', drink)
            variation_of_actions_home(actions_in_home)

        elif move == 'c':
            animation_of_sleeping()
            variation_of_actions_home(actions_in_home)

        elif move == 'd':
            animation_of_walking()
            variation_of_actions_taverna(actions_in_taverna)


def variation_of_actions_taverna(text):
    if dict_stats['health_points'] <= 0:
        death_in_game()
        print(action_main_moves)
    else:
        animation_of_walking(0.01)
        stats_of_player()
        print(text)
        move = input().lower()
        valid_move = ('a', 'b', 'c', 'd', 'e')
        while move not in valid_move:
            print('You input wrong symbol!')
            variation_of_actions_taverna(actions_in_taverna)
        else:
            if move == 'a':
                animation_of_walking(0.01)
                dict_bar = {'1': 'vodka', '2': 'beer'}
                stats_of_player()
                print('{}{}{}{}'.format('Choose your drink: \n1: ',
                                        dict_bar['1'], '\n2: ',
                                        dict_bar['2'],
                                        '\nInput: '))
                action_in_bar = input()
                print(dict_bar[action_in_bar])
                decrease_parameter('health_points', 5)
                variation_of_actions_taverna(actions_in_taverna)
            elif move == 'b':
                animation_of_walking(0.01)
                dict_food_bar = {'1': 'sandwich', '2': 'nuggets'}
                stats_of_player()
                print('{}{}{}{}'.format('Choose your food: \n1: ',
                                        dict_food_bar['1'], '\n2: ',
                                        dict_food_bar['2']))
                print('Input: ')
                action_in_food_bar = input()
                print(dict_food_bar[action_in_food_bar])
                increase_parameter('health_points', 1)
                increase_parameter('food_points', 4)
                increase_parameter('water_points', 2)
                variation_of_actions_taverna(actions_in_taverna)

            elif move == 'c':
                animation_of_walking(0.01)
                dict_tables = {
                    '1': 'John Fedor',
                    '2': 'Fedora John',
                    '3': 'Johan Fedor'
                }
                print('{}{}{}{}{}{}'.format('Choose your opponent: \n1: ',
                                            dict_tables['1'], '\n2: ',
                                            dict_tables['2'], '\n3: ',
                                            dict_tables['3'],
                                            '\nInput: '))
                action_in_tables = input()
                print('{}{}'.format('You choose: ',
                                    dict_tables[action_in_tables]))
                deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
                random.shuffle(deck)
                print('{}{}'.format('Let\'s play twenty-one', '\nMake a bet:'))
                bet = float(input())
                if dict_stats['money_points'] - bet * 1.4 < 0:
                    print('{}'.format('Very big bet, you can back later'))
                    variation_of_actions_taverna(actions_in_taverna)
                else:
                    count = 0
                    want_continue = True
                    while count < 21 and want_continue:
                        print(f'You have {count} points.')
                        current = deck.pop()
                        print(f'You got the card worth {current}')
                        count += current
                        want_continue = input('Wanna take more '
                                              'card? y/n\n') == 'y'
                    if count == 21:
                        print('Yep, you\'ve scored!')
                        dict_stats['money_points'] += bet * 1.2
                        variation_of_actions_taverna(actions_in_taverna)
                    else:
                        if count > 21:
                            print('Sorry, but you lost')
                        if count < 21:
                            print(f'You have {count} points '
                                  f'and you\'ve finished the game')
                        dict_stats['money_points'] -= bet * 1.4
                        variation_of_actions_taverna(actions_in_taverna)

            elif move == 'd':
                animation_of_walking(0.01)
                dict_taverna_music = {
                    '1': 'artist_1 - song_name_1',
                    '2': 'artist_2 - song_name_2'
                }
                choice_in_bar = input('Wanna listen music? y/n\n').lower()
                while choice_in_bar == 'y':
                    stats_of_player()
                    print('{}{}{}{}{}'.format('Music in playlist: \n1: ',
                                              dict_taverna_music['1'], '\n2: ',
                                              dict_taverna_music['2'],
                                              '\nInput: '))
                    action_in_taverna_music = input()
                    print(dict_taverna_music[action_in_taverna_music])
                    dict_stats['money_points'] -= 10
                    choice_in_taverna_music_again = input('Want change music? '
                                                          'y/n\n').lower()
                    if choice_in_taverna_music_again == 'y':
                        continue
                    else:
                        break
                variation_of_actions_taverna(actions_in_taverna)

            elif move == 'e':
                animation_of_walking()
                variation_of_actions_home(actions_in_home)


def continue_of_sleeping(text):
    animation_of_sleeping()
    print('\nWake Up!')
    stats_of_player()
    print(text)


def moves_in_game(text):
    print(text)
    move = int(input())
    valid_move = (1, 2, 3)
    while move in valid_move:
        if move == 1:
            variation_of_actions_home(actions_in_home)

        elif move == 2:
            variation_of_actions_taverna(actions_in_taverna)

        elif move == 3:
            continue_of_sleeping(action_main_moves)
    else:
        print('invalid data, try again')
        moves_in_game(action_main_moves)


def death_in_game(text='Wasted'):  # конец игры
    stats_of_player()
    print(text)
    replay_game = input('Want replay? y/n\n').lower()
    if replay_game == 'y':
        game_lvl_selection(choose_lvl)


def the_course_of_the_game(i=0, hunger=10, thirst=20, decrease_health=10):
    while dict_stats['health_points'] > 0:
        moves_in_game(action_main_moves)
        i += 1
        print(i)
        if i % 2 == 0:
            decrease_parameter('food_points', hunger)
            decrease_parameter('water_points', thirst)
            decrease_parameter('health_points', decrease_health)
    death_in_game()


if __name__ == '__main__':
    print(greeting_in_the_beginning)
    game_lvl_selection(choose_lvl)
    wake_up_at_start_of_game()
    the_course_of_the_game()
