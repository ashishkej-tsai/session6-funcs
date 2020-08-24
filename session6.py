vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

deck_single_expression = list(zip(vals*4, sum(list(map(lambda x:([x]*13),suits)), [])))

def deck_function(vals:"list of card values"=vals, suits:"list of card types"=suits) -> "returns tuple of 52 cards":
    '''
    Inputs:
        vals: 13 values of cards 2,3,4,5,6,7,8,9,10,jack,queen,king,ace
        suits: 4 types of cards spades, clubs, hearts, diamonds

    Returns:
        result: 52 types of cards
    '''
    result = []
    for val in vals:
        for suit in suits:
            result.append((val,suit))
    return result

