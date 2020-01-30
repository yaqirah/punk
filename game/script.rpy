# The script of the game goes in this file.
# Just define stuff in here, actual story starts in chapter 0

# Declare the main character
define p = Character("punk", dynamic=True, image="punk", who_color="#D999F0")
define b = Character("Brian Noonan", image="lofi", who_color="#852929")
define default_name="Petra"
define custom_name=False
define pick_gender=False
define gender="Girl"
define they = "she"
define them = "her"
define their = "her"
define theirs = "hers"
define themself = "herself"

# Define music
define punk_theme = "audio/punkaf.mp3"
define lofi_theme = "audio/placeholderlofi.mp3"
define filling_in = "audio/fillingin.mp3"
define filling_loop = "audio/fillingloop.mp3"
define an_end_to_the_crazy = "audio/anendtothecrazy.mp3"
define birds = "audio/meadowlark_daniel-simion.mp3"
image black = Solid("#000")

transform leftside:
    xalign 0.25
    yalign 1.0
transform rightside:
    xalign 0.75
    yalign 1.0

# The game starts here.
label start:
    jump chapter0
