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
        self.count = 0

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def showHand(self):
        print(self.name + '`s current hand: ')
        for cards in self.hand:
            print(cards.value, end=" ")
        print('\n')
        # [print(i.value) for i in self.hand]

    def checkHand(self):
        for cards in self.hand:
            self.count += cards.value
        return self.count

class Blackjack:

    def __init__(self):
        self.gameinfo = {
            'win': 0,
            'lose': 0,
            'draw': 0,
            'isWon': False
        }
        self.deck = Deck()
        self.startgame()

    def startgame(self):
        playername = input('What is your name: ')
        playerbal = int(input('What is your current Balance: '))
        playerbet = int(input('How much are you betting: '))

        if playerbet >= playerbal:
            print('\nPlease bet a different amount. The Balance you have cannot cover your previous choice.')
            playerbet = int(input('How much are you betting: '))

        player = Player(playername, playerbal, playerbet)
        dealer = Player("Dealer", 0, 0)
        player.draw(self.deck)
        dealer.draw(self.deck)

        # for item in player.hand:print(item.value, sep='\n')
        # exit()

        while self.gameinfo['isWon'] == False:
            player.showHand()
            dealer.showHand()
            self.nextMove(player, dealer)

        self.checkWinner(player, dealer)


    def nextMove(self, player, dealer):
        playermove = input('Will you stand or hit or stop? ').lower()

        if playermove == 'stand':
            dealer.draw(self.deck)
            if dealer.checkHand() == 21 or player.checkHand() == 21:
                self.gameinfo['isWon'] = True
            elif dealer.checkHand() >= 21 or player.checkHand() >= 21:
                self.gameinfo['isWon'] = True
        elif playermove == 'hit':
            player.draw(self.deck)
            dealer.draw(self.deck)
            if dealer.checkHand() == 21 or player.checkHand() == 21:
                self.gameinfo['isWon'] = True
            elif dealer.checkHand() >= 21 or player.checkHand() >= 21:
                self.gameinfo['isWon'] = True
        elif playermove == 'stop':
            self.gameinfo['isWon'] = True
        else:
            print('Please either Stand or Hit or Stop.\n')
            playermove = input('Will you stand or hit or stop? ').lower()

    def checkWinner(self, player, dealer):
        if dealer.checkHand() == 21:
            print('Dealer has won!')
        elif player.checkHand() == 21:
            print('Player has won!')
        elif dealer.checkHand() >= 21:
            print('Dealer is over 21. Player has won!')
        elif player.checkHand() >= 21:
            print('Player is over 21. Dealer has won!')
        elif player.checkHand() > dealer.checkHand():
            print('Player hand is greater than dealer')
        else:
            print('Dealer has won.')

Blackjack()