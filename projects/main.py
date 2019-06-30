from terminaltables import AsciiTable
from classes import *
from api import *


def print_stat(status: Status, season: Season, data: list):
    table = [
        ['Mode'],
        ['Solo'],
        ['Duo'],
        ['Squads'],
        ['Total']
    ]

    for player in data:
        so_val = float(status.parse(player, season, GAME_MODS["solo"]))
        du_val = float(status.parse(player, season, GAME_MODS["duo"]))
        sq_val = float(status.parse(player, season, GAME_MODS["squads"]))
        table[0].append(player["epicUserHandle"])
        table[1].append(str(so_val))
        table[2].append(str(du_val))
        table[3].append(str(sq_val))
        table[4].append(str(sq_val + du_val + so_val))
    print('+---')
    print(f'| {status.title} - {season.title}')
    print(AsciiTable(table).table)


players_count = 0
players_names = []
players_platforms = []
players_data = []

while True:
    print(f'Player {players_count + 1}:')
    user_player_name = input(f'epic name > ')
    if user_player_name == 'done':
        break
    user_player_platform = input(f'platform (pc/psn) > ')
    if user_player_platform == 'done':
        break

    players_count += 1
    players_names.append(user_player_name)
    players_platforms.append(user_player_platform)


print('Loading..')

# get data from API
for index in range(0, players_count):
    players_data.append(get_payer_data(players_names[index], players_platforms[index]).json())

while True:
    op_exit = len(get_statuses()) + 2
    op_all = len(get_statuses()) + 1
    print(f'----------------------------------')
    print(f'Please select an option (by #):')
    for x in get_statuses():
        x.menu()
    print(f'{op_all}. All Status')
    print(f'{op_exit}. Exit')

    stat_index = input('>')

    if stat_index == str(op_exit):
        break
    elif stat_index == str(op_all):
        for stat in get_statuses():
            for seas in get_seasons():
                print_stat(stat, seas, players_data)
    else:
        print('Select Season')
        for x in get_seasons():
            x.menu()
        season_index = input('>')

        print_stat(
            get_status_by_index(int(stat_index)),
            get_season_by_index(int(season_index)),
            players_data
        )

print('Goodbye')
