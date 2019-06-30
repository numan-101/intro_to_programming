from api import *
import json


def get_seasons():
    st1 = Season()
    st1.title = 'All Time'
    st1.key = ''
    st1.index = 1

    st2 = Season()
    st2.title = 'Current'
    st2.key = 'curr_'
    st2.index = 2
    return [st1, st2]


def get_statuses():
    st1 = Status()
    st1.key = 'top1'
    st1.title = 'Wins'
    st1.index = 1

    st2 = Status()
    st2.key = 'kd'
    st2.title = 'K/D'
    st2.index = 2

    st3 = Status()
    st3.key = 'winRatio'
    st3.title = 'Win Ratio'
    st3.index = 3

    st4 = Status()
    st4.key = 'matches'
    st4.title = 'Matches'
    st4.index = 4

    st5 = Status()
    st5.key = 'kills'
    st5.title = 'Kills'
    st5.index = 5

    st6 = Status()
    st6.key = 'kpg'
    st6.title = 'Kills/Mat'
    st6.index = 6
    return [st1, st2, st3, st4, st5, st6]


def get_status_by_index(index: int):
    for status in get_statuses():
        if status.index == index:
            return status
    return None


def get_season_by_index(index: int):
    for season in get_seasons():
        if season.index == index:
            return season
    return None


class Season:
    key = None
    title = None
    index = None

    def menu(self):
        print(f'{self.index}. {self.title}')

    @staticmethod
    def get(season_index: int, seasons_list: list):
        for season in seasons_list:
            if season.index == season_index:
                return season
        return None


class Status:
    key = None
    index = None
    title = None

    def menu(self):
        print(f'{self.index}. {self.title}')

    def parse(self, json_status: json, season: Season, game_mode: str):
        try:
            return json_status[STATUS_ROOT][f"{season.key}{game_mode}"][self.key]["value"]
        except:
            return 0
