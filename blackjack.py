from IPython.display import clear_output
import random

player_stand = False
dealer_stand = False

class Player(object):

    def __init__(self):
        self.hand = []

class Dealer(Player):

    def __init__(self):
        self.hand= []

    def dealer_turn(self):
        switch = random.random()
        if switch >= 0.5:
            print 'The Dealer decides to stick!'
            dealer_stand = True
        else:
            print 'The Dealer decides to hit!'
        d.hand = sum(d.hand, random.choice(gp.cards.values()))

class Gameplay(object):
    cards = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

    def __init__(self):
        pass

    def initial_hands(self):
            # Giving players initial hands
            p.hand = sum([random.choice(gp.cards.values()), random.choice(gp.cards.values())])
            d.hand = [random.choice(gp.cards.values()), random.choice(gp.cards.values())]

    def check_win(self):
        end = False
        dealer_sum = str(d.hand)
        while end == False:
                if p.hand > 21:
                    print 'You lose!'
                    end = True
                elif int(dealer_sum) > 21:
                    print 'The dealer goes bust! You win!'
                    end = True
                elif player_stand == True and dealer_stand == True:
                    if p.hand == dealer_sum:
                        print 'It\'s a draw!'
                        end = True
                    elif p.hand > dealer_sum < 21:
                        print 'Player wins!'
                        end = True
                    elif dealer_sum > p.hand < 21:
                        print 'Dealer wins!'
                        end = True


    def game_loop(self):
        while True:
            try:
                print "Player, your hand is " + str(p.hand)
                option = raw_input("Player, do you want to 'stand' or 'hit'? ---> ")
                if option == 'hit':
                    p.hand = p.hand + random.choice(gp.cards.values())
                    print 'Your hand is now ' + str(p.hand)
                    print 'It is now the Dealer\'s turn!'
                elif option == 'stand':
                    print 'Your hand remains at ' + str(p.hand)
                    print 'It is now the Dealer\'s turn!'
                    player_stand = True
                elif option == 'break':
                    break
                Dealer.dealer_turn(d)
                Gameplay.check_win(gp)
            finally:
                         pass

gp = Gameplay()
p = Player()
d = Dealer()
gp.initial_hands()
gp.game_loop()
