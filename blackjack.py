from deck import Deck

def init():
    """
    initializes deck and player and dealer hands.
    """

    deck = Deck() 
    suits = ['♠', '♥', '♦', '♣']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for number in numbers:
            deck.add_card({'suit' : suit, 'value' : number})
    deck.shuffle(3)

    dealer = Deck()
    player = Deck()
    for i in range(2):
        dealer.add_card(deck.draw_card())
        player.add_card(deck.draw_card())

    return deck, player, dealer

def format_hand(hand, is_dealer):
    """returns the contents of a hand as a str, 
    if hand belongs to dealer then it will censor all but one card.

    Parameters
    ----------
    hand: Deck
        collection of cards that can accessed with methods.
    is_dealer: bool
        a flag to indicate whether hand should be censored.

    Returns
    -------
    str

    Raises
    ------
    Nothing.
    """

    iterable = hand.get_iterator()
    output = ""
    for idx, card in enumerate(iterable):
        if is_dealer and idx > 0:
            output += '?? '
        else:
            output += f'{card["suit"]}{card["value"]} '
    return output

def prompt_game_options(hand):
    """ prompts user to repspond to game options

    Parameters
    ----------
    hand: Deck
        used to change which options are availible.

    Returns
    -------
    str:
        name of valid choice player has made.

    Raises
    ------
    Nothing.

    """
    choice = 'nothing'
    options = ['hit', 'stand']
    print('you may [hit], [stand]')


    while True:
        choice = input("> ")
        if choice in options:
            return choice

def get_hand_value(hand):
    ace_count = 0
    iterator = hand.get_iterator()
    total = 0

    for card in iterator:
        if card['value'] == 'A':
            ace_count += 1
        else:
            total += hand.get_card_value(card)
    
    for num_used in range(ace_count):
        if (11 + total) + (ace_count - num_used) <= 21:
            total += 11
        else:
            total += 1

    return total

def print_both_hands(player, dealer):
    print(f'player: {format_hand(player, is_dealer = False)}')
    print('')
    print(f'dealer: {format_hand(dealer, is_dealer = True)}')

def calculate_winner(deck, player, dealer):
    """performs end game procedure for dealer and calculates winner.

    Parameters
    ----------
    player: Deck
        the players cards
    dealer: Deck
        the dealers cards
    
    Returns
    -------
    bool:
        True if player won, false otherwise.

    Raises
    ------
    Noting.
    """
    player_pts = get_hand_value(player)
    dealer_pts = get_hand_value(dealer)

    # check if player is above 21
    if player_pts > 21:
        return False

    # draw for dealer
    while dealer_pts <= 17:
        dealer.add_card(deck.draw_card())
        dealer_pts = get_hand_value(dealer)
    
    if dealer_pts > 21 or dealer_pts < player_pts:
        return True
    return False
    
def prompt_bet(balance):

    while True:
        amt = input("enter bet amt: $")
        if amt.isdigit():
            amt = int(amt)
            if amt < balance:
                return amt

def game_loop(deck, player, dealer):
    """main gameloop for blackjack"""

    balance = 100
    playing_game = True


    while playing_game:
        print("\n\nNEW GAME\n\n")
        print(f'you have ${balance} to bet.')
        bet_amt = prompt_bet(balance)
        print(f'you bet {bet_amt}, you are able to win {bet_amt * 2}.')
        
        while get_hand_value(player) <= 21:
            print_both_hands(player, dealer)    
            choice = prompt_game_options(player)
            if choice == 'stand':
                break
            elif choice == 'hit':
                player.add_card(deck.draw_card)
        
        player_won = calculate_winner(deck, player, dealer)
        print('final hand:')
        print_both_hands(player, dealer)
        
        # deal reward or penalty
        if player_won:
            balance += bet_amt * 2
            print(f'you won ${bet_amt * 2}! you now have {balance}')
        else:
            balance -= bet_amt
            print(f'you lost ${bet_amt * 2}, you now have {balance}')
           

if __name__ == "__main__":
    deck, player, dealer = init()
    game_loop(deck, player, dealer)
    