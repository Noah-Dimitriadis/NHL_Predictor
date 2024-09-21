import requests
import pandas as pd
import datetime

season_start_dates = ["2017-10-04",
                        "2018-10-04",
                        "2019-10-02",
                        "2021-01-13",
                        "2021-10-12",
                        "2022-10-07",
                        "2023-10-10"]
season_end_dates = ["2018-04-08",
                    "2019-04-06",
                    "2020-03-12",
                    "2021-05-19",
                    "2022-05-01",
                    "2023-04-14",
                    "2024-04-18"]

def test_single():
    URL =  'https://api-web.nhle.com/v1/score/2018-10-04'

    r = requests.get(url=URL)

    data = r.json()

    for game in data["games"]:
        h_team_name = game['homeTeam']['name']['default']
        h_team_score = game['homeTeam']['score']
        h_team_sog = game['homeTeam']['sog']

        a_team_name = game['awayTeam']['name']['default']
        a_team_score = game['awayTeam']['score']
        a_team_sog = game['awayTeam']['sog']


        h_outcome = h_team_score > a_team_score
        a_outcome = not h_outcome

        print(f'{h_team_name},{h_team_score},{h_team_sog},{h_outcome},{a_team_name},{a_team_score},{a_team_sog},{a_outcome}')

def get_games_day(date:datetime.date) -> list[str]:
    date = date.strftime("%Y-%m-%d")
    URL =  f'https://api-web.nhle.com/v1/score/{date}'

    r = requests.get(url=URL)

    data = r.json()

    games = list()

    for game in data["games"]:
        h_team_name = game['homeTeam']['name']['default']
        h_team_score = game['homeTeam']['score']
        h_team_sog = game['homeTeam']['sog']

        a_team_name = game['awayTeam']['name']['default']
        a_team_score = game['awayTeam']['score']
        a_team_sog = game['awayTeam']['sog']


        h_outcome = h_team_score > a_team_score
        a_outcome = not h_outcome

        row = f'{h_team_name},{h_team_score},{h_team_sog},{h_outcome},{a_team_name},{a_team_score},{a_team_sog},{a_outcome}\n'
        games.append(row)
        
    return games
        

if __name__ == "__main__":
    for i in range(len(season_end_dates)):
        s_year = season_start_dates[i][:4]
        e_year = season_end_dates[i][:4]
        file = open(f"YearData/Year_{s_year}{e_year}.csv", "a")
        file.write('HomeTeam,HomeScore,HomeSOG,Outcome,AwayTeam,AwayScore,AwaySOG,Outcome\n')

        generated = pd.date_range(start=season_start_dates[i], end=season_end_dates[i])
        games = list()

        for date in generated.date:
            day_games = get_games_day(date)
            for game in day_games:
                games.append(game)

        for game in games:
            file.write(game)
        file.close()