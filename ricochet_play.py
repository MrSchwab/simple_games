import random


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name, hand=[], money=100):
        self.name = name
        self.hand = hand
        self.money = money
        self.score = 0

    def __str__(self):
        current_hand = ""
        for card in self.hand:
            current_hand += str(card) + " "
        final_status = current_hand + "score: " + str(self.score)
        return final_status

    def setScore(self):
        card_values = {"A":14, "J":11, "Q":12, "K":13}

        for card in self.hand:
            if int(card) in range(2, 11):
                self.score += int(card)
            elif card in card_values:
                self.score += card_values[card]

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

print("Very well, let's introduce ourselves then! I am Pegasus, Danilo's laptop, and I will be your dealer!")

players = []
new_player = True
player_counter = 0

while new_player:
    player_input = input("Please type player name: ")
    player_names = Player(player_input)
    players.append(player_names)
    player_counter += 1
    add_player = str(input("Would you like to add another player? (y/n)"))
    if add_player.upper() != "Y" or player_counter == 5:
        new_player = False

print("Alright. Let's play Ricochet Poker!")
for Player in players:
    print(Player.name)

deck = Deck()
deck.shuffle()

for Player in players:
    Player.draw(deck)
    print(Player.name)
    print(Player.money)
    Player.showHand()

