from stattlepy import Stattleship
import time
import datetime

def getDateFromString(dateString):
    y,m,d = (int(x) for x in dateString.split('-'))
    return datetime.date(y,m,d)

def getGamesForWeek():
    statQueries = Stattleship()
    Token = statQueries.set_token('ENTER YOUR KEY')

    queryforDate = statQueries.ss_get_results(sport='football',league='nfl',ep='games',status='upcoming')
    seasonStartString = queryforDate[0]['seasons'][0]['starts_on']
    startDate = getDateFromString(seasonStartString)
    week = int(((datetime.date.today() - startDate).total_seconds() / 3600 / 24 // 7) - 4)

    gamesQuery = statQueries.ss_get_results(sport='football',league='nfl',ep='games',status='upcoming',week=str(week),walk=True)
    homeTeams = {}
    for page in gamesQuery:
        for team in page['home_teams']:
            homeTeams[team['id']] = team['name']
        for game in page['games']:
            print game['name'] + "\n"
            print "Home Team: " + homeTeams[game["home_team_id"]]
