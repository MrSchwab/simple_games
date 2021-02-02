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


# Considering the code starting from here
player_num = int(input("How many players will there be? Please note that our table sits up to 5 people. "))
print("Very well, let's introduce ourselves then! I am Pegasus, Danilo's laptop, and I will be your dealer!")

if player_num == 1:
    player1 = input(str("Player one, what should I call you? "))
    player1 = Player(player1)

elif player_num == 2:
    player1 = input(str("Player one, what should I call you? "))
    player2 = input(str("Player two, what should I call you? "))
    player1 = Player(player1)
    player2 = Player(player2)

elif player_num == 3:
    player1 = input(str("Player one, what should I call you? "))
    player2 = input(str("Player two, what should I call you? "))
    player3 = input(str("Player three, what should I call you? "))
    player1 = Player(player1)
    player2 = Player(player2)
    player3 = Player(player3)

elif player_num == 4:
    player1 = input(str("Player one, what should I call you? "))
    player2 = input(str("Player two, what should I call you? "))
    player3 = input(str("Player three, what should I call you? "))
    player4 = input(str("Player four, what should I call you? "))
    player1 = Player(player1)
    player2 = Player(player2)
    player3 = Player(player3)
    player4 = Player(player4)

elif player_num == 5:
    player1 = input(str("Player one, what should I call you? "))
    player2 = input(str("Player two, what should I call you? "))
    player3 = input(str("Player three, what should I call you? "))
    player4 = input(str("Player four, what should I call you? "))
    player5 = input(str("Player five, what should I call you? "))
    player1 = Player(player1)
    player2 = Player(player2)
    player3 = Player(player3)
    player4 = Player(player4)
    player5 = Player(player5)

print("Alright. Let's play Ricochet Poker!")

deck = Deck()
deck.shuffle()
# deck.show()

# Round 1:

player1.draw(deck)
print(player1.name, "has a/an:")
player1.showHand()

player2.draw(deck)
print(player2.name, "has a/an:")
player2.showHand()

player3.draw(deck)
print(player3.name, "has a/an:")
player3.showHand()

player4.draw(deck)
print(player4.name, "has a/an:")
player4.showHand()

player5.draw(deck)
print(player5.name, "has a/an:")
player5.showHand()

# and up to here it is too comparmentalized. For example, this does not have
# a variable with the player count. You can make the round a class for example
# have a loop to call for as long as the players want to play

# bob = Player("Bob")
# bob.draw(deck).draw(deck)
# bob.showHand()
# print("nice cards bob")
# deck.show()
