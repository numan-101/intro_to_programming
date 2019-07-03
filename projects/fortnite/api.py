import requests

GAME_MODS = {'solo': 'p2', 'duo': 'p10', 'squads': 'p9'}
GAME_STATUS = {'wins': 'top1', 'k/d': 'kd', 'played matches': 'matches', 'win ratio': 'winRatio'}
STATUS_ROOT = 'stats'


def get_payer_data(player_name: str, platform: str):
    headers = {'TRN-Api-Key': 'd812c30c-73d3-42cf-8275-c8550100b57a'}
    url = f'https://api.fortnitetracker.com/v1/profile/{platform}/{player_name}'
    return requests.get(url, headers=headers)


number = 5.0
try:
    r = 10/number
    print(r)
except:
    print("Oops! Error occurred.")