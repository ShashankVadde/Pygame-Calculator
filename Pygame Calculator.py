import pygame
import sys
from decimal import Decimal, getcontext

# Initialize Pygame
pygame.init()

# Create the Window
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Pygame Calculator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKBLUE = (95, 107, 109)

# New button colors
yellow = (255, 216, 108)
darkGrey = (95, 107, 109)
darkBlue = (18, 35, 158)

font = pygame.font.Font(None, 36)

# Global Variables
math = ""
inputText = ""

# Decimals
getcontext().prec = 10 

# Functions for the Calculator Buttons
def buttons(item):
    global math, inputText
    if item == "=":
        equalButton()
    elif item == "Clear":
        clearButton()
    elif item == "Del":
        deleteButton()
    elif item == "+":
        addition()
    elif item == "-":
        subtraction()
    elif item == "*":
        multiplication()
    elif item == "/":
        division()
    else:
        math = math + str(item)
        inputText = math

def clearButton():
    global math, inputText
    math = ""
    inputText = ""

def equalButton():
    global math, inputText
    try:
        result = str(Decimal(eval(math)).quantize(Decimal('0.000')))
        inputText = result
        math = result
    except Exception as e:
        inputText = "Invalid"

def deleteButton():
    global math, inputText
    math = math[:-1]
    inputText = math

def addition():
    global math, inputText
    math = math + "+"
    inputText = math

def subtraction():
    global math, inputText
    math = math + "-"
    inputText = math

def multiplication():
    global math, inputText
    math = math + "*"
    inputText = math

def division():
    global math, inputText
    math = math + "/"
    inputText = math

# Runs the Program Until the User Clicks out of the Window.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for (text, x, y, width, height, color) in buttonData:
                if x <= event.pos[0] <= x + width and y <= event.pos[1] <= y + height:
                    buttons(text)

    screen.fill(WHITE)

    # Input Field (Frame Where the Calculations are done)
    pygame.draw.rect(screen, WHITE, (10, 10, 330, 60))
    textSurface = font.render(inputText, True, BLACK)
    screen.blit(textSurface, (20, 20))

    # Calculator Buttons
    buttonData = [
        ("7", 10, 100, 100, 70, yellow),
        ("8", 120, 100, 100, 70, yellow),
        ("9", 230, 100, 100, 70, yellow),
        ("/", 340, 100, 100, 70, darkGrey),
        ("4", 10, 170, 100, 70, yellow),
        ("5", 120, 170, 100, 70, yellow),
        ("6", 230, 170, 100, 70, yellow),
        ("*", 340, 170, 100, 70, darkGrey),
        ("1", 10, 240, 100, 70, yellow),
        ("2", 120, 240, 100, 70, yellow),
        ("3", 230, 240, 100, 70, yellow),
        ("-", 340, 240, 100, 70, darkGrey),
        ("0", 10, 310, 100, 70, yellow),
        (".", 120, 310, 100, 70, yellow),
        ("Del", 230, 310, 100, 70, darkBlue),
        ("+", 340, 310, 100, 70, darkGrey),
        ("Clear", 10, 380, 330, 70, darkBlue),
        ("=", 340, 380, 100, 70, darkGrey)
    ]

    for (text, x, y, width, height, color) in buttonData:
        pygame.draw.rect(screen, color, (x, y, width, height))
        textSurface = font.render(text, True, BLACK if text not in ("Clear", "Del") else WHITE)
        textRect = textSurface.get_rect(center=(x + width / 2, y + height / 2))
        screen.blit(textSurface, textRect)

    pygame.display.flip()

pygame.quit()
sys.exit()
