# O(n) time | O(k) space - where n is the number
# of competition and k is the number of teams.

def tournamentWinner(competitions, results):
    res = {}
    for indx, competition in enumerate(competitions):
        homeTeam, awayTeam = competition
        if results[indx] == 0:
            value = res.setdefault(awayTeam, 0)
            res[awayTeam] = value + 3
        else:
            value = res.setdefault(homeTeam, 0)
        res[homeTeam] = value + 3

    return max(res, key=res.get)


HOME_TEAM_WON = 1


# O(n) time | O(k) space - where n is the number
# of competition and k is the number of teams.


def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for indx, competition in enumerate(competitions):
        homeTeam, awayTeam = competition
        result = results[indx]

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points
