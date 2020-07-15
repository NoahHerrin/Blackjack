""" deck.py

Datastructure for storing a collection of cards.

@author Noah Herrin
"""
import copy
import random
import math

class Deck(object):
    """Datastructure for storing a collection of cards.
    
    Fields
    ------
    cards: list(tuple)
        list of card objects which are tuples containing (suit, value)

    Methods
    -------
    draw:
        removes card from the top of the deck and returns it
    add:
        adds a card to the top of the deck
    get_card_value:
        gets the value of a card cards.
    get_hand_value:
        gets the value of all cards in this deck.
    split:
        removes half of the cards from this deck and
        adds them to a newly created deck that is returned
    """

    def __init__(self):
        self.__cards = []
    
    def add_card(self, card):
        """adds a card to the list of cards

        Parameters
        ----------
        card: dict
            card to be added to the deck.

        Returns
        -------
        int:
            number of the cards after new addition.

        Raises
        ------
        Nothing.
        """
        self.__cards.append(card)

    def draw_card(self):
        """removes top card from the deck

        Parameters
        ----------
        None.

        Returns
        -------
        dict:
            the card removed from top of the deck

        Raises
        ------
        Exception
            raised if draw_card is invoked from a deck that has 0 cards

        """
        
        if len(self.__cards) == 0:
            raise Exception("unable to draw from an empty deck.")
        return self.__cards.pop(0)

    def get_card_value(self, card, ace_is_high = True):
        """get's the value of the card in this game.

        Parameters
        ----------
        card: dict
            card whose value will be calculated.
        ace_is_high: bool
            flag indicating whether 'A' will be 1 or 11
        
        Returns
        -------
        int:
            the value of the card.
        
        Raises
        ------
        Nothing.

        """

        face_cards = ['J', 'Q', 'K']

        if card['value'].isdigit():
            return int(card['value'])
        elif card['value'] in face_cards:
            return 10
        elif card['value'] == 'A':
            return 11 if ace_is_high else 1
        else:
            raise Exception(f'Unknown card {card}.')

    def shuffle(self, n):
        """shuffles the list of cards n times.

        Parameter
        ---------
        n: int
            number of times to shuffle the deck.
        
        Returns
        -------
        void.

        Raises
        ------
        Nothing.

        """

        cards_len = len(self.__cards)
        for i in range(n):
            for src in range(cards_len):
                dest = math.floor(random.random() * cards_len)
                temp = self.__cards[src]
                self.__cards[src] = self.__cards[dest]
                self.__cards[dest] = temp
    
    def get_iterator(self):
        """returns an iterator for the cards in the deck

        Parameters
        ----------
        None.

        Returns
        -------
        iterator:
            iterator for the __cards field

        Raises
        ------
        Nothing.

        """
        return copy.copy(self.__cards)
