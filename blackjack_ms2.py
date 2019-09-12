import random

class Card:
    def __init__(self, type, val):
        self.type = type
        self.value = val

    def show(self):
        # return "\n{} of {}".format(self.value, self.type)
        return self.value

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

    def build(self):
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hears']:
            for v in range(1,14):
                self.cards.append(Card(s,v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r =random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()

class Player:
    def __init__(self, name, bal, bet):
        self.hand = []
        self.name = name
        self.balance = bal
        self.bet = bet

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def showHand(self):
        for card in self.hand:
            print('\n'+self.name+'`s current hand: '+card.show())

class Blackjack:

    def __init__(self):
        self.gameinfo = {
            'win': 0,
            'lose': 0,
            'draw': 0
        }
        self.startgame()

    def startgame(self):
        deck = Deck()

        playername = input('What is your name: ')
        playerbal = int(input('What is your current Balance: '))
        playerbet = int(input('How much are you betting: '))

        if playerbet >= playerbal:
            print('\nPlease bet a different amount. The Balance you have cannot cover your previous choice.')
            playerbet = int(input('How much are you betting: '))

        player = Player(playername, playerbal, playerbet)
        dealer = Player("Dealer", 0, 0)
        player.draw(deck)
        dealer.draw(deck)

        # for item in player.hand:print(item.value, sep='\n')
        # exit()

        while deck.cards != []:
            player.showHand()
            dealer.showHand()
            self.nextMove(player, dealer)

    def nextMove(self, player, dealer):
        playermove = input('Will you stand or hit? ').lower()

        if playermove == 'stand':
            dealer.draw()
        elif playermove == 'hit':
            player.draw()

Blackjack()