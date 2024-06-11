import requests
from nba_api.stats.endpoints import leaguedashplayerstats, leaguegamefinder, leaguedashteamstats
import pandas as pd

# Get player stats
def get_player_stats(season):
    # Create an instance of LeagueDashPlayerStats with the specified season
    pstats = leaguedashplayerstats.LeagueDashPlayerStats(season=season)
    # Get data as a dataframe starting first index
    df = pstats.get_data_frames()[0]

    return df

playerstats_2023 = get_player_stats('2023-24')
print(playerstats_2023.head())

# Get team stats
def get_team_stats(season):

    tstats = leaguedashteamstats.LeagueDashTeamStats(season=season)

    df = tstats.get_data_frames()[0]

    return df

teamstats_2023 = get_team_stats('2023-24')
print(teamstats_2023.head())

# Get indiviual game stats
def get_game_stats(season):

    gstats = leaguegamefinder.LeagueGameFinder(season_nullable=season)

    df = gstats.get_data_frames()[0]

    return df

game_stats2023 = get_game_stats('2023-24')
print(game_stats2023)