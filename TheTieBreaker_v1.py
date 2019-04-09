import random
import time


class SuperOver:
    possible_scores = (0, 1, 2, 3, 4, 5, 6, 'out')
    balls = (1, 2, 3, 4, 5, 0)  # number of balls in an over
    team_score = 0

    def __init__(self, team, overs, target, *players):
        self.team = team
        self.overs = overs
        self.target = target
        self.balls_left = overs * 6
        self.players = players

    @property
    def team_players(self):
        return self.players

    @team_players.setter
    def team_players(self, *players):
        self.players = players
        print("Team Players : {}".format(self.players[0]))

    @staticmethod
    def swap_batting_positions():
        batting[0], batting[1] = batting[1], batting[0]
        return batting

    @staticmethod
    def run_machine():
        global running
        if batting[0] == 'Kirat Boli' or batting[0] == 'DB Vellyers':
            running = random.choices(SuperOver.possible_scores, weights=[5, 10, 25, 10, 25, 1, 14, 10])
        elif batting[0] == 'N.S Nodhi' or batting[0] == 'H Mamla':
            running = random.choices(SuperOver.possible_scores, weights=[10, 15, 15, 10, 20, 1, 19, 15])
        return running[0]

    def game_rules(self):
        global batting
        global each_ball_dictionary
        ball_by_ball = []
        total_players = [p for p in self.players]
        player = total_players[0]
        batting = [bat for ind, bat in enumerate(player) if ind < 2]
        each_ball_dictionary = {"ovr": "0.0", "batsman": batting[0], "score": 00}

        def score_card():
            global batting
            SuperOver.team_score = SuperOver.team_score + run
            if run == 1 or run == 3 or run == 5:
                SuperOver.swap_batting_positions()
                each_ball_dictionary['batsman'] = batting[0]

        def over_count():
            global run
            global target
            target = 0
            target = target + SuperOver.team_score
            print("Target", target)
            SuperOver.team_score = 0
            over = 0
            for each_ball in SuperOver.balls:
                if each_ball == 0:
                    over += 1
                    self.balls_left -= 1
                    ball_by_ball.append("{}.{}".format(over, each_ball))
                    each_ball_dictionary['ovr'] = ball_by_ball[-1]
                    run = SuperOver.run_machine()
                    print("{} {} scores {} run(s)".format(each_ball_dictionary['ovr'], each_ball_dictionary['batsman'],
                                                          running[0]))
                    if run == 'out':
                        return
                    else:
                        score_card()
                    if SuperOver.team_score > self.target:
                        break
                    SuperOver.swap_batting_positions()
                    each_ball_dictionary['batsman'] = batting[0]
                else:
                    self.balls_left -= 1
                    ball_by_ball.append("{}.{}".format(over, each_ball))
                    each_ball_dictionary['ovr'] = ball_by_ball[-1]
                    run = SuperOver.run_machine()
                    print("{} {} scores {} run(s)".format(each_ball_dictionary['ovr'], each_ball_dictionary['batsman'],
                                                          running[0]))
                    if run == 'out':
                        return
                    else:
                        score_card()
                    if SuperOver.team_score > self.target:
                        break
                time.sleep(1)

        over_count()
        return ''


super_over1 = SuperOver('Lengaburu', 1, 0, *'players')
super_over1.team_players = ["Kirat Boli", "N.S Nodhi"]
super_over1.game_rules()
team1_score = super_over1.team_score
print('Team1 Scored : {}'.format(team1_score))
super_over2 = SuperOver('Enchai', 1, team1_score, *'players')
super_over2.team_players = ['DB Vellyers', 'H Mamla']
super_over2.game_rules()
team2_score = super_over2.team_score
print('Team2 Scored : {}'.format(team2_score))
if team1_score > team2_score:
    print('{} won the match'.format(super_over1.team))
else:
    print('{} won the match'.format(super_over2.team))

