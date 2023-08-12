import random
import components

def cardsRender(cardToDraw: str):
    cardShape = components.cardShapes[random.randint(0, 7)]
    renderedCard = f''' ___\n|{cardToDraw}  |\n| {cardShape} |\n|__{cardToDraw}|'''

    return renderedCard


