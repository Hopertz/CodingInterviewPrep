"""
   Tournament Winner

   There's an algorithms tournament taking place in which teams of programmers
   compete against each other to solve algorithmic problems as fast as possible.
   Teams compete in a round robin,where each team faces off against all other teams.
   Only two teams compete against each other at a time,and for each competition ,
   one team is designated the home team while the other team is away team.
   In each competition there's always one winner and one loser; there are no ties.
   A team receives 3 points if it wins and 0 points if it loses.The winner of the
   tournament is the team tha receives the most amount of points.

   Given an array of pairs representing the teams that have competed against each other
   and an array containing the results of each competition,write a function that returns
   the winner of the tournament.The input arrays are named competitions and results,
   respectively.The competition array has elements in the form of [homeTeam, awayTeam],
   where each team is a string of at most 30 characters representing the name of the team.
   The results array contains information about the winner of each corresponding competition
   in the competition array.Specifically, results[i] denotes thr winner of each
   competitions[i],where a 1 in the results array means that the home team in the
   corresponding competition won and a 0 means that the away team won.

   Its's guaranteed that exactly one team will win the tournament and that each team will
   compete against all other teams exactly once.It's also guaranteed that the tournament
   will always have at least two teams.

   Sample Input
      competitions = [
       ['HTML', 'C#'],
       ['C#', 'Python']
       ['Python','HTML'],
     ]
     results = [ 0, 0, 1]

   Sample Output
    'Python'
     // C# beats HTML , Python Beats C#, and Python Beats HTML
     // HTML - 0 points
     // C# - 3 points
     // Python - 6 points
"""

# SOLUTION 1

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


# SOLUTION 2

# O(n) time | O(k) space - where n is the number
# of competition and k is the number of teams.
HOME_TEAM_WON = 1
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
