"""
CP1404 Practical
"""

COLOURS = {"aquamarine2": "#76eec6", "blue2": "#0000ee", "chartreuse1": "#7fff00", "cyan1": "#00ffff",
           "darkgoldenrod1": "#ffb90f", "darkgreen": "#006400", "darkorchid1": "#bf3eff", "deeppink1": "#ff1493",
           "ghostwhite": "#f8f8ff", "gray7": "#121212"}

user_choice = input("Colour name: ").lower()
while user_choice:
    if user_choice in COLOURS:
        print(COLOURS[user_choice])
    else:
        print("Invalid Colour")
    user_choice = input("Colour name: ").lower()
