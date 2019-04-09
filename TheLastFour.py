import random
import time


class CricketMatch:

    """ class CricketMatch will take 2 team and their players dynamically and do the math in accordance to Cricket game.
    After toss, if team2 comes to bat 1st, a random target will be generated and last 4 over will be shown with 40 runs
     left with 3 wickets.

     Attributes:
        pretty much self explanatory.
     """
    possible_scores = (0, 1, 2, 3, 4, 5, 6, 'out')
    balls = (1, 2, 3, 4, 5, 0)  # number of balls in an over
    over = 0
    target = 0
    super_over_button = 'off'

    def __init__(self, team1, team2, overs, target=0, *players):
        """Initialize the instance attributes
        Attributes:
            team1 : holds 1st team name
            team2 : holds 2nd team name
            overs : number of overs left/ or to be played
            balls_left : total balls remaining.
            target : remaining runs in the remaining balls_left
            t1player & t2players holds respective team players
            """
        self.team1 = team1
        self.team2 = team2
        self.overs = overs
        self.balls_left = overs * 6
        self.target = target
        self.t1players = players
        self.t2players = players
        self.first_innings_score = 0

    @property
    def team1_players(self):
        """In laymens term it sets playing 11"""
        return self.t1players

    @team1_players.setter
    def team1_players(self, *players):
        self.t1players = players
        self.t1players = list(self.t1players[0])
        dressing_room1 = {self.team1: self.t1players}
        print(dressing_room1)

    @property
    def team2_players(self):
        """In laymens term it sets playing 11"""
        return self.t2players

    @team2_players.setter
    def team2_players(self, *players):
        self.t2players = players
        self.t2players = list(self.t2players[0])
        dressing_room2 = {self.team2: self.t2players}
        print(dressing_room2)

    def coin_toss(self):
        """Toss section, team will choose to bat/bowl based on weather condition as well as Day/Night match.
            weather : user input the weather condition
            daynight : user inputs the Day or Night match
            e_choose_to : team2 choice after winning the toss
            l_choose_to : team1 choice after winning the toss
            captain : Umpire will decide who will spin the coin
        """
        weather = input("Weather Condition(Clear/Cloudy) : ")
        daynight = input("Match Scheduled(Day/Night) : ")
        e_choose_to = 'Bat'
        l_choose_to = 'Bat'
        if weather == 'Clear' and daynight == 'Day':
            e_choose_to = 'Bowl'
        elif weather == 'Cloudy' and daynight == 'Night':
            l_choose_to = 'Bowl'
        captain = [self.t1players[0], self.t2players[0]]
        captain = random.choice(captain)
        print('Toss : {} will spin the coin'.format(captain))
        coin = ('Head', 'Tail')
        flips = random.choices(coin, weights=[50, 50])
        flip_guessed = random.choices(coin, weights=[50, 50])
        print('{} is the call..'.format(flip_guessed[0]))
        time.sleep(1)
        if flips[0] == 'Head':
            print('Head it is..')
        else:
            print('Tail it is..')
        if captain == self.t1players[0]:
            if flip_guessed[0] == flips[0]:
                print('{} wins the Toss and opted to {} first'.format(self.team2, e_choose_to))
            else:
                print('{} wins the Toss and opted to {} first'.format(self.team1, l_choose_to))
                e_choose_to = ''
        else:
            if flip_guessed[0] == flips[0]:
                print('{} wins the Toss and opted to {} first'.format(self.team1, l_choose_to))
                e_choose_to = ''
            else:
                print('{} wins the Toss and opted to {} first'.format(self.team2, e_choose_to))

        if l_choose_to == 'Bowl' or e_choose_to == 'Bat':
            self.first_innings_score = random.randrange(100, 180)
            print('End of 1st innings : {} posted {} runs.'.format(self.team2, self.first_innings_score))
            print('{} - {}/7 , 16 over'.format(self.team1, self.first_innings_score - self.target))
            self.game_rules(self.first_innings_score)
        else:
            return True

    @staticmethod
    def swap_batting_positions():
        """Change of batting between batsman and runner"""
        try:
            batting[0], batting[1] = batting[1], batting[0]
        except IndexError:
            exit()
        return batting

    @staticmethod
    def run_machine():
        """Batsman's form and how he choose to bat on every ball"""
        global running
        if batting[0] == 'Kirat Boli':
            running = random.choices(CricketMatch.possible_scores, weights=[5, 30, 25, 10, 15, 1, 9, 5])
        elif batting[0] == 'N.S Nodhi':
            running = random.choices(CricketMatch.possible_scores, weights=[10, 40, 20, 5, 10, 1, 4, 10])
        elif batting[0] == 'R Rumrah':
            running = random.choices(CricketMatch.possible_scores, weights=[20, 30, 15, 5, 5, 1, 4, 20])
        elif batting[0] == 'Shashi Henra':
            running = random.choices(CricketMatch.possible_scores, weights=[30, 25, 5, 0, 5, 1, 4, 30])
        return running[0]

    def score_card(self):
        """If batsman is out, next batsman comes in if any, or else team score will be counted"""
        if run != 'out':
            if CricketMatch.super_over_button == 'off':
                self.target = self.target - run
                if self.target <= 0:
                    print("{} won the Match with {} ball(s) to spare".format(self.team1, self.balls_left))
                    exit()
                else:
                    pass
            else:
                CricketMatch.target = CricketMatch.target + run
            if run == 1 or run == 3 or run == 5:
                CricketMatch.swap_batting_positions()
                each_ball_dictionary['batsman'] = batting[0]
            else:
                pass
        else:
            print('{} gone..'.format(batting[0]))
            # Logic to change the batsman if one gets out
            for batsman in total_players:
                if batsman in batting or batsman in batsman_gone:
                    pass
                else:
                    if batsman in yet_to_bat:
                        pass
                    else:
                        yet_to_bat.append(batsman)
            batsman_gone.append(batting[0])
            batting.pop(0)
            try:
                batting.insert(0, yet_to_bat[0])
            except IndexError:
                print("All Out")
                print('{} : {}/10'.format(self.team1, self.first_innings_score - self.target))
                print('{} won the match with {} runs'.format(self.team2, self.target))
                time.sleep(1)
                exit('Match Over')
            each_ball_dictionary['batsman'] = batting[0]
            # print('Already Out', batsman_gone)
            # print('Will bat', yet_to_bat)
            # print("Current Batsman", batting)
            try:
                yet_to_bat.pop(0)
            except IndexError:
                print("All Out")

            # print('batsman remain', yet_to_bat)

    def game_rules(self, innings=40):
        global each_ball_dictionary
        global batting
        global yet_to_bat
        global total_players
        global batsman_gone
        yet_to_bat = []
        ball_by_ball = []
        batsman_gone = []
        total_players = [p for p in self.t1players]
        batting = [bat for ind, bat in enumerate(total_players) if ind < 2]
        each_ball_dictionary = {"ovr": "0.0", "batsman": batting[0], "score": 00}

        def over_count():
            """Iterate through each ball, over wise till end of the last over or till All Out"""
            global run
            current_over = 16
            while CricketMatch.over < self.overs:
                for each_ball in CricketMatch.balls:
                    # move to next over
                    if each_ball == 0:
                        CricketMatch.over += 1
                        current_over += 1
                        self.balls_left -= 1
                        ball_by_ball.append("{}.{}".format(current_over, each_ball))
                        each_ball_dictionary['ovr'] = ball_by_ball[-1]
                        run = CricketMatch.run_machine()
                        print("{} {} scores {} run(s)".format(each_ball_dictionary['ovr'],
                                                              each_ball_dictionary['batsman'],
                                                              running[0]))
                        CricketMatch.score_card(self)
                        CricketMatch.swap_batting_positions()
                        each_ball_dictionary['batsman'] = batting[0]
                        print('{} - {} overs : {}/{})'.format
                              (self.team1, current_over, innings - self.target, 7 + len(batsman_gone)))
                        print('{} runs to win ({} balls remaining)'.format(self.target, self.balls_left))

                    # each ball in an over
                    else:
                        self.balls_left -= 1
                        ball_by_ball.append("{}.{}".format(current_over, each_ball))
                        each_ball_dictionary['ovr'] = ball_by_ball[-1]
                        run = CricketMatch.run_machine()
                        print("{} {} scores {} run(s)".format(each_ball_dictionary['ovr'],
                                                              each_ball_dictionary['batsman'],
                                                              running[0]))
                        self.score_card()
                    time.sleep(0.5)
            if self.target > 0:
                print('{} won the match with {} runs'.format(self.team2, self.target))
        over_count()


match = CricketMatch('Lengaburu', 'Enchai', 4, 40, *'players')
match.team1_players = ["Kirat Boli", "N.S Nodhi", "R Rumrah", "Shashi Henra"]
match.team2_players = ['DB Vellyers', 'H Mamla']
match.coin_toss()
# match.game_rules()


