from pyfiglet import figlet_format
from termcolor import colored

def Print_art(msg, color):
    Valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

    if color not in Valid_colors:
        color = "magenta"
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


msg = input("what would you like to print? ")
color =  input("what color? ")

Print_art(msg, color)
