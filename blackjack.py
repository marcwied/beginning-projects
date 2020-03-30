import random

# Declare Suits, Rank, assign values to rank

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
               'Ten': 10,
               'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True                                              # variable to control game while loop


class Card:                                                 # creates Card class

    def __init__(self, suit, rank):                         # initializes values of card object
        self.suit = suit
        self.rank = rank

    def __str__(self):                                      # returns string in form of "Five of Hearts"
        return self.rank + ' of ' + self.suit

class Deck:                                                 # creates Deck class

    def __init__(self):
        self.deck = []                                      # creates an empty list(deck) to start with
        for suit in suits:                                  # loops through all suits and ranks
            for rank in ranks:
                self.deck.append(Card(suit,rank))           # builds card objects and adds them to the list(Deck)

    def __str__(self):                                      # optional method to print contents of the deck
        deck_comp = ''                                      # start w/ an empty print string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()             # adds each card object to the print string
        return 'The deck has: ' + deck_comp

    def shuffle(self):                                      # method to shuffle the deck
        random.shuffle(self.deck)

    def deal(self):                                         # method to deal a card and then removes from the deck
        single_card = self.deck.pop()
        return single_card


class Hand:                                                 # creates Hand class

    def __init__(self):                                     # initializes hand object
        self.hand = []                                      # with an empty list
        self.value = 0                                      # value of hand (sum of cards)

    def addcards(self,card):                                # method to add card to players hand list (object)
        self.hand.append(card)                              # adds card to hand list
        self.value += card_values[card.rank]                # sums cards values
        if card.rank == 'Ace' and self.value > 21:          # if player has an ace and value > 21, subtracts 10 from
            self.value -= 10                                # hand value

class Chips:                                                # creates Chips class

    def __init__(self,bet=0):                                                   # initializes player bet and stack values
        self.stack = int(input("How much do you want to buyin for?"))           # creates player stack (buy in amount), based on player input
        self.bet = bet

    def place_bet(self):                                                        # method to place bet
        while True:                                                             # while loop to continuously ask for valid bet
            self.bet = int(input("Place your bet: "))                           # bet is set equal to player input
            if self.bet > self.stack:                                           # if statement to check if bet amount is < chip stack
                print("You cannot bet more than your stack")
                continue                                                        # continues loop until valid input
            break

    def player_wins(self):                                                      # method for player win
        print("Player Wins!")                                                   # notifies player of winning
        self.stack += self.bet                                                  # adds bet to player stack
        print("Player has won ", self.bet)                                      # prints winning amount
        print("Player Stack = ", self.stack)                                    # and prints player new stack amount

    def dealer_wins(self):                                                      # method for dealer winning
        print("Dealer Wins.")                                                   # notifies of dealer winning
        self.stack -= self.bet                                                  # subtracts bet amount from player stack
        print("Player has lost their bet of: ", self.bet)                       # prints the amount player lost
        print("Player Stack = ", self.stack)                                    # and prints player new stack amount

    def push(self):                                                             # method for push (tie)
        print("Its a push")                                                     # notifies of tie
        print("Player Stack = ", self.stack)                                    # prints player stack

def show_player(self):                                                          # function to print players hand and its value
    print("Player's Hand: ", *self.hand, sep='\n ')
    print("Player's Hand = ", self.value)

def show_one(self):                                                             # function to show a single card from the dealers hand
    print("Dealer's Hand:", '\n [Card Hidden]')
    print('',dealer.hand[1],'\n')

def show_all(self):                                                             # function to show all of dealers cards
    print("Dealer's Hand:", *self.hand, sep='\n ')
    print("Dealer's Hand = ", self.value)

def hit(deck, hand):                                                            # function to adds card to the active hand
    hand.addcards(deck.deal())                                                  # deals card from deck, adds to player/dealer hand

def hit_or_stay(deck,hand):                                                     # function for hitting/staying during gameplay
    playing = True                                                              # variable to control function

    while playing:
        x = input('Do you want to hit or stay?')                                # asks for player input, hit or stay?
        if x[0].lower() == 'h':                                                 # takes first letter of player input, formats to lowercase, if 'h', then player has hit
            hit(deck,hand)                                                      # calls hit function for the active player's hand, and removes card from deck
            print('')
            show_player(hand)                                                   # shows players updated hand and hand value
            if hand.value > 21:                                                 # if value > 21, player has busted
                print("BUST!!!")
                break                                                           # breaks from while loop inside hit_or_stay function
        elif x[0].lower() == 's':                                               # if player stays (s)
            print("Player stays on", hand.value)                                # returns value payer stood on
            print('')
            print("Dealer's Turn")                                              # notifies of dealer turn
            playing = False                                                               # breaks while loop in hit_or_stay function
        else:
            print("Invalid Entry")                                              # if invalid entry (!= hit, stay, h or s)
            continue                                                            # continues in loop until valid entry

def dealer_turn(deck,hand):                                                     # function that controls dealer play
    playing = True                                                              # variable to control while loop
    show_all(hand)                                                              # shows entire dealer hand

    while playing:                                                              # while loop for function
        if hand.value <= 16:                                                    # if dealer hand value <= 16, dealer automatically hits
            print("Dealer must hit")
            hit(deck,hand)                                                      # dealer hits, card added to hand, card removed from deck
            print('')
            show_all(hand)                                                      # shows updated dealer hand
            continue                                                            # continues in loop until dealer hand > 16
        elif hand.value <= 21 and hand.value > 16:                              # if dealer hand <= 21 or > 16, dealer automatically stays
            print("Dealer stays")
            print('')
            break                                                               # breaks from dealer_turn function
        elif hand.value > 21:                                                   # if dealer hand > 21, returns dealer busted
            print("Dealer Bust!")
            print('')
            break                                                               # breaks from dealer_turn function

# GAME TEST

while playing:                                                                                          # variable to control game engine

    print("Welcome to BLACKJACK!!! Get closer to 21 than the Dealer without busting to win.")           # prints opening statement
    print(' ')


    deck = Deck()                                                                                       # Creates Game deck
    deck.shuffle()                                                                                      # shuffles new game deck

    player1Stack = Chips()                                                                              # creates player1 chip stack
    player1Stack.place_bet()                                                                            # prompts player for the amount they'd like to bet

    player1 = Hand()                                                                                    # creates player1 hand object
    dealer = Hand()                                                                                     # creates dealer hand object

    player1.addcards(deck.deal())                                                                       # adds single card to player hand object
    dealer.addcards(deck.deal())                                                                        # adds single card to dealer hand object
    player1.addcards(deck.deal())                                                                       # adds single card to player hand object
    dealer.addcards(deck.deal())                                                                        # adds single card to dealer hand object

    show_one(dealer)                                                                                    # shows single dealer card
    show_player(player1)                                                                                # shows player hand and value

    while playing:                                                                                      # inner variable to control in game actions

        hit_or_stay(deck,player1)                                                                       # prompts player to hit or stay
        if player1.value > 21:                                                                          # if player hits and busts, breaks from inner variable
            break
        else:                                                                                           # moves to dealer_turn function once player stays
            dealer_turn(deck,dealer)
            break

    if (player1.value > dealer.value and player1.value <= 21) or dealer.value > 21:                     # if player wins, fires player_wins method
        player1Stack.player_wins()

    elif (player1.value < dealer.value and dealer.value <= 21) or player1.value > 21:                   # if player loses, fires dealer_wins method
        player1Stack.dealer_wins()

    else:                                                                                               # if player hand = dealer hand, fires push method
        player1Stack.push()
    break                                                                                               # terminates game engine