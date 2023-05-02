import random


class T2Cup:
    allTeams = []

    def entry_team(self, teamObj):
        self.allTeams.append(teamObj)


class Team(T2Cup):
    def __init__(self, name) -> None:
        self.teamName = name
        self.playerListOfObject = []
        super().entry_team(self)

    def entry_player(self, player):  # Player is a type of object
        self.playerListOfObject.append(player)

    def __repr__(self) -> str:
        return f"From object. TeamName : {self.teamName}"


class Player:
    def __init__(self, name, teamObj) -> None:
        self.playerName = name
        self.strikeRate = 0.0
        self.runBat = 0
        self.ballUsed = 0
        self.fours = 0
        self.sixes = 0
        self.runBowl = 0
        self.wicketsTaken = 0
        self.ballsBowled = 0
        teamObj.entry_player(self)

    def __repr__(self) -> str:
        return f"playerName : {self.playerName}"


class Innings:
    def __init__(self, team1, team2, battingTeam, bowlingTeam) -> None:
        self.teamOneObj = team1
        self.teamTwoObj = team2
        self.battingTeam = battingTeam
        self.bowlingTeam = bowlingTeam
        self.totalRun = 0
        self.totalWickets = 0
        self.totalOver = 0
        self.currentBall = 0
        self.currentBattingList = [
            battingTeam.playerListOfObject[0], battingTeam.playerListOfObject[1]]
        self.striker = battingTeam.playerListOfObject[0]
        self.currentOverStatus = []
        self.currentBowler = None
        self.allOverStatus = []

    def show_score_board(self):
        print(
            f"*{self.currentBattingList[0].playerName} - {self.currentBattingList[0].runBat}({self.currentBattingList[0].ballUsed})\t", end="")
        print(
            f"{self.currentBattingList[1].playerName} - {self.currentBattingList[1].runBat}({self.currentBattingList[1].ballUsed})")
        print(
            f"{batttingTeamObj.teamName[:3].upper()} | {self.totalRun}-{self.totalWickets}")
        print(f"Overs: {self.totalOver}.{self.currentBall}")
        if self.currentBowler is not None:
            print(
                f"{self.currentBowler.playerName} - {self.currentBowler.runBowl}/{self.currentBowler.wicketsTaken}")

    def set_bowler(self, bowlerObj):
        self.currentBowler = bowlerObj

    def bowl(self, status):
        self.totalRun += status
        self.striker.runBat += status
        self.striker.ballUsed += 1
        self.currentBowler.runBowl += status
        self.currentBowler.ballsBowled += 1
        self.currentBall += 1


cup = T2Cup()
bangladesh = Team('Bangladesh')
india = Team('India')
tamim = Player('Tamim Iqubal', bangladesh)
sakib = Player("Sakib Al Hasan", bangladesh)
mustafizur = Player("Mustafizur Rahman", bangladesh)
virat = Player('Virat Kholi', india)
rohit = Player("Rohit Sharma", india)
bhumra = Player("Bhumra", india)

print(cup.allTeams)

while True:
    print("Select teams to be played")
    for i, val in enumerate(cup.allTeams):
        print(f"{i+1}. {val.teamName}")
    teamOneIndex, teamTwoIndex = map(
        int, input("Enter two team indexes: ").split(" "))
    teamOneIndex -= 1
    teamTwoIndex -= 1
    teamOneObj = cup.allTeams[teamOneIndex]
    teamTwoObj = cup.allTeams[teamTwoIndex]
    tossWin = random.choice([teamOneIndex, teamTwoIndex])
    print(f"{cup.allTeams[tossWin].teamName} win the toss")
    if tossWin == teamOneIndex:
        tossLose = teamTwoIndex
    else:
        tossLose = teamOneIndex
    rand = random.choice([0, 1])
    if rand == 0:
        # Winner team choose Bowling
        print(f"{cup.allTeams[tossWin].teamName} choose bowling")
        batttingTeamObj = cup.allTeams[tossLose]
        bowlingTeamObj = cup.allTeams[tossWin]
    else:
        # Winner team choose Batting
        print(f"{cup.allTeams[tossWin].teamName} choose batting")
        batttingTeamObj = cup.allTeams[tossWin]
        bowlingTeamObj = cup.allTeams[tossLose]
    firstInnings = Innings(teamOneObj, teamTwoObj,
                           batttingTeamObj, bowlingTeamObj)
    firstInnings.show_score_board()
    print("Choose bowler: ")
    for i, val in enumerate(bowlingTeamObj.playerListOfObject):
        print(f"{i+1}. {val.playerName}")
    bowlerIndex = int(input("Enter bowler index: "))
    bowlerIndex -= 1
    bowlerObj = bowlingTeamObj.playerListOfObject[bowlerIndex]
    firstInnings.set_bowler(bowlerObj)
    firstInnings.show_score_board()
    print()
    firstInnings.bowl(6)
    firstInnings.show_score_board()
    break
