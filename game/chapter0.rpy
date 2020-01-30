# The prologue

label chapter0:
    # Clear title music
    stop music fadeout 1.0

    # DEBUG, delete later
    menu:
        "Would you like to test naming and stuff?"

        "Sure":
            $ pick_gender = True
            jump naming

        "Nah":
            narrator "Alright then..."

    $ punk = default_name
    if custom_name == True:
        jump naming

    jump prologue_start

label naming:
    scene bg building
    play music punk_theme fadein 2.0 fadeout 1.0

    show punk

    if pick_gender:
        menu:
            "Are you a boy or a girl?"

            "Boy":
                $ they = _("he")
                $ them = _("him")
                $ their = _("his")
                $ theirs = _("his")
                $ themself = _("himself")

            "Girl":
                $ they = _("she")
                $ them = _("her")
                $ their = _("her")
                $ theirs = _("hers")
                $ themself = _("herself")

            "None of your damn business":
                $ they = _("they")
                $ them = _("them")
                $ their = _("their")
                $ theirs = _("theirs")
                $ themself = _("themself")

    # These display lines of dialogue.
    # Naming
    $ punk = renpy.input("What is [their] name? Note that the maximum length is 10 for display purposes, please understand", allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'", length=10)
    $ punk = punk.strip().title()
    if punk == "":
        $ punk= default_name

    stop music fadeout 1.0
    p @ look "What kinda name is that?"

    show punk at leftside
    show lofi at rightside

    b "Hello!"

    p "..."

    jump prologue_start

label prologue_start:
    scene bg punk bedroom with Fade(0, 0, 1.5)
    play music filling_in fadein 2.0 fadeout 1.0

    narrator "I woke up in my room as usual, with the cruel light of the sun glaring down at my face. If only my mom would let me get those curtains that block out the sunlight, but she says I just wouldn’t get up if I had them."
    narrator "While I argue against it, I must admit she’s right about that. I’d love to just go full nocturnal like a bat or something, bats are pretty cool."

    play music punk_theme fadein 2.0 fadeout 1.0

    narrator "I reached for my music player sitting on the bedstand and put on one of my favorite tunes, a song by the band Spiffiest Teas."
    narrator "Anyways, I figured it’d be yet another day of just chilling and listening to music while I lie in bed, passing the time away while I waste away in this boring town where nothing ever happens. Just the same old thing every day, you know?"
    narrator "At least I’ll be an adult fairly soon, I plan to ditch this dull place the first chance I get. The thought of leaving this dump is just about the only thing that keeps me going, really. When I leave this place, I want to do something exciting."
    narrator "One thing that’d really be cool is if I went somewhere where nobody knows me and start up a band. I’m not much for singing, but I bet I would absolutely shred it on a guitar. Maybe I’d even get one of those fancy electric guitars, that’d be pretty sweet."
    narrator "Of course, I could start up a band here, but there probably isn’t even anyone worth being in a band with. Everyone is just a stick in the mud, never up to doing anything interesting. I really just wish something would happen here, anything to shake things up."
    narrator "Anyways, even the best music can get boring sometimes when you just listen to it on loop. I decided to head out, just to wander around town and doing whatever catches my eye."

    # Prepare for the next scene
    default arcade_done = False
    default park_done = False

    jump bus

label bus:
    show bg bus
    play music filling_in fadein 2.0 fadeout 1.0

    narrator "I got on the bus, not sure where exactly I wanted to go. Figure I'll just ride it until we're near something sort of interesting. The bus route covers a decent amount of town at least, which is good because teenagers can't even get a car in this place."
    narrator "Heard there was some accident some number of years back so they raised the age limit to drive, super dumb."

    if arcade_done == False:
        narrator "One thing I could do was go to the arcade, I suppose. Not exactly a gamer myself, but games where you don't just use a stick or slap some buttons can be fun. Like the ones where you get a gun you can hold, or a steering wheel, or whatever."
    if park_done == False:
        narrator "Another thing I could do is go to the park. Not to play with random little kids of course, I'm not some weirdo.{w} But could just chill on the swings if there's nothing better to do I suppose."
        narrator "The park is next to the woods, which actually makes a good spot to hide out. Just hole up in some random tree and there's nobody to bother you, finding a good spot is half the fun in itself."
        narrator "I remember as a kid I would just wander around there, pretending I was some knight or something while carrying a big stick."

    jump bus_choice
label bus_choice:
    if arcade_done and park_done:
        narrator "There's nowhere else to go, so I just went home."
        jump end
    menu:
        "Where should I go?"

        "Arcade" if arcade_done == False:
            $ arcade_done = True
            jump arcade
        "Park" if park_done == False:
            $ park_done = True
            jump park
        "Home" if park_done and arcade_done:
            jump end
label arcade:
    show bg arcade
    play music an_end_to_the_crazy fadein 2.0 fadeout 1.0
    default tokens = 5
    default start_tokens = tokens
    default lofi_appeared = False
    default rand = 0
    default nua_lore = False

    narrator "I arrived at the arcade, ready to play some games. As you do when at an arcade, not exactly much else. The place smelled like nerds,{w} and not the candy kind. It really could use some air freshener..."
    narrator "Anyways, what game should I play? After fishing through my pockets it looks like I have [tokens] of these little arcade tokens on me. One token is good for one game, which should last a decent amount of time if I don't completely suck."

    jump arcade_choice
label arcade_choice:
    default current_game = ""

    if lofi_appeared == False and tokens == start_tokens:
        # Give a description of the games
        # Describe shooting game
        narrator "The first game is a shooting game called PANIC BANK, where you play some mobster shooting up a bank. Its graphics are a bit dated, but it's pretty fun to shoot up all the cops that show up and see how much loot you can make off with."
        narrator "Of course, the main draw of this game is the gun controller. Other people can play with you, but I'd prefer to not do that. I'd rather just use both guns myself, dual weilding just looks pretty cool."
        narrator "Uses twice as many tokens to do that of course, but it's fucking worth it. It's shoved in the back corner of the arcade, where nobody else really goes. Not the most popular game but I like it better that way."

        # Describe racing game
        narrator "Next up is the racing game, GRAND PIX II. It's based off some famous racing competition, but I'm not enough into actual racing to know which one. The important part is that it's in a big booth, enclosed with a reclined seat and everything."
        narrator "Of course, the controller is a steering wheel. Naturally it costs two tokens because the game's all tricked out, but it's worth it. Just the height of luxury as far as arcade games go."
        narrator "As soon as you lose, someone will always swoop in to take your place. It's just that popular."

        # Describe dancing game
        narrator "Last but not least is the dancing game, DANCE OFF: THE FINAL SHOWDOWN. Honestly it's my favorite game here, but I don't care for the attention it draws. I'm pretty good at it though, at the top of the leaderboard for all the songs and everything."
        narrator "I really like songs with a cool vibe, but I've done all the songs in it by now. Even the cutesy cartoon ones, just gets boring doing the same songs all the time even if they are awesome."
        narrator "Hopefully I won't run into that annoying guy though, sees himself as my rival or something since he's at the top of the rank for every other game. He'll never take this one from me though, the dudes a huge nerd and get too tired quickly."
        narrator "Just has no coordination, sometimes he trips.{w} Doesn't stop him from trying to seek me out whenever I come here to try to make it into a competition or something, imagine caring about scores. Better off not running into that guy, he's a huge pain."
    menu:
        "Shooting" if tokens > 0:
            jump arcade_shooting
        "Racing" if tokens > 1:
            jump arcade_racing
        "Dancing" if tokens > 0:
            jump arcade_dancing
        "Leave" if lofi_appeared == False:
            if lofi_appeared == False:
                show lofi
                play music lofi_theme fadein 2.0 fadeout 1.0
                
                jump annoying_guy
        "Get out of this place before that nerd comes back" if lofi_appeared == True:
            # Go back to the bus
            show bg bus
            play music filling_loop fadein 2.0 fadeout 1.0
            jump bus_choice
label arcade_shooting:
    $ current_game = "PANIC BANK"
    $ rand = renpy.random.randint(1, 10)
    default s = ""

    # Check if lofi guy appeared
    if lofi_appeared == False and (tokens == 1 or rand == 1):
        $ tokens -= 1
        jump annoying_shooting

    if tokens > 1:
        menu:
            "Would you like to use two guns?"

            "Just one gun":
                $ tokens -= 1
                narrator "Can't blow everything all on one game, after all. Even if it is a really cool game."
            "Both guns":
                $ s = "s"
                $ tokens -= 2
                narrator "Awesome, I'm dual wielding."
    else:
        $ tokens -= 1

    if rand == 10:
        narrator "I was completely in the zone in this game, playing for what felt like hours without my mobster getting a single scratch. Of course, all good things must eventually come to an end, but I did get a lot of use out of my token[s]."
        narrator "This time I reached a higher level than ever before,{w} before I hit my inevitable demise at any rate. As a result, I secured the second spot on the leaderboard. Like practically other game in this place, the top spot was taken by NUA."
        if nua_lore == False:
            jump nua
    elif rand > 5:
        narrator "I did alright, I guess. Nothing particularly interesting, but at least I got a decent amount of playtime out of my token[s]. It was a fun time, shooting up cops and all. A good stress reliever."
    else:
        narrator "I did so terribly at this game, I don't even want to think about it anymore... I got gunned down so fast, it's a good thing this game is out of the way and nobody saw that."
    jump arcade_choice
label arcade_racing:
    $ current_game = "GRAND PIX II"
    $ rand = renpy.random.randint(1, 3)
    $ tokens -= 2

    # Check if lofi guy appeared
    if lofi_appeared == False and (tokens == 0 or rand == 1):
        jump annoying_racing

    if rand == 3:
        narrator "It isn't the game I'm the best at, but I'd say I did pretty good. In each race I was consistently at the head of the pack, beating out all of the cars controlled by the game. Not that it meant anything high score wise, that's dominated by NUA."
        if nua_lore == False:
            jump nua
    else:
        narrator "I didn't do so hot at this racing game. I lost the first few races and ran out of continues, quickly getting booted out for the next person to take over. The game is just that popular, after all. At least it killed time I guess."
    jump arcade_choice
label arcade_dancing:
    $ current_game = "DANCE OFF: THE FINAL SHOWDOWN"
    $ rand = renpy.random.randint(1, 6)
    $ tokens -= 1

    # Check if lofi guy appeared
    if lofi_appeared == False and (tokens == 0 or rand == 1):
        jump annoying_dancing

    if rand == 10:
        narrator "When I played this game on the hardest difficulty to my favorite song, I became one with the music and entered a trance state. It was as if I was born to dance, the right moves came to me as naturally as breathing."
        narrator "Once again I beat the high score, not that it meant much as the leaderboard remained filled with my name. Still, it always feels nice to beat my personal best. People surrounded me, in awe of my skill."
        narrator "I didn't ever lose, but rather I ran out of songs that it'd let me play on a single token. As I stepped off the mat, the five people in this arcade clapped for me. Felt like royalty here."
    elif rand > 5:
        narrator "As always, I did pretty good. Didn't beat any records, but I was able to keep playing until I ran out of songs to play. It was really fun, good bang for my single token."
    else:
        narrator "I can't say it was my best go at this game, but this dancing game is still the one I'm the best at in this place. It was just a so-so go, I didn't really get into the music that much."
    jump arcade_choice
label nua:
    narrator "Not that NUA is anyone mysterious, this isn't exactly the smallest town. It's just that nerd, Brian Noonan. He spends most of his time in this arcade and has no life. Apparently it's short for Nuadha which is some mythology thing."
    narrator "The guy even wants people to actually call him that but ew, lame. Find something better to do than being at this place like it's a full time job..."
    $ nua_lore = True
    jump arcade_choice
label annoying_shooting:
    play music lofi_theme fadein 2.0 fadeout 1.0
    show lofi gun
    narrator "I was just minding my own business, about to start this shooting game, when this guy just walked up and lifted the other gun up, holding it in front of him."
    jump annoying_guy
label annoying_racing:
    play music lofi_theme fadein 2.0 fadeout 1.0
    show lofi

    narrator "As I sat down to play this racing game, this nerd came up behind me and leaned over my shoulder. Personal space, buddy!"

    jump annoying_guy
label annoying_dancing:
    play music lofi_theme fadein 2.0 fadeout 1.0
    show lofi

    narrator "I wonder, are there any songs in this game that I haven't played? Of course not, I know this game like the back of my hand. As I was browsing through the song list, this guy came up behind me."

    jump annoying_guy
label annoying_guy:
    if lofi_appeared == False:
        narrator "This guy slid next to me as if he owned the place. I mean he practically does since he has the top score on about every game, but I own at DANCE OFF: THE FINAL SHOWDOWN so there."
        narrator "Every time I come here he walks up and wants to play some game, maybe he's got a crush on me or something.{w} Ew, I like girls a lot more. Even if I was into a guy, nerds aren't my type."

    $ lofi_appeared = True

    menu:
        b "Can I play?"

        "Why not? Go ahead":
            narrator "This guy wanted to play [current_game] with me, so I did. It was alright, for playing with this guy. He really seemed to enjoy it and thanked me afterwards. Poor guy clearly doesn't have friends."
        "No, go away":
            show lofi sad
            b "Please?"
            menu:
                "Fine":
                    narrator "I reluctantly played [current_game] with this nerd, and kicked his ass for being so obnoxious. Or rather the games are all co-op if you play with others so I just sabotaged him."
                "No way!":
                    narrator "I ran away,{w} or rather walked quickly because I would look insane if I booked it out of there like I really wanted to. What a weirdo."
        "I don't have any tokens so guess I can't..." if tokens == 0:
            b "It's okay, I'll lend you some."
            $ tokens += 2
            jump annoying_guy
    hide lofi
    play music an_end_to_the_crazy fadein 2.0 fadeout 1.0
    jump arcade_choice
label park:
    show bg park2
    default swings = False
    default fairy_appeared = False
    default climbed_tree = False
    default grabbed_stick = False

    narrator "So we at the park"
label park_choice:
    menu:
        "What should I do next?"

        "Chill on the swings" if swings == False:
            # TODO: ADD TEXT
            $ swings = True
            jump park_choice

        "Check out the woods":
            show bg forest
            jump woods_choice
label woods_choice:
    menu:
        "What should I do?"
        "Climb a tree" if climbed_tree == False:
            narrator "tree is climbed"
            $ climbed_tree = True
            jump woods_choice
        "Grab a stick" if grabbed_stick == False:
            # look for a stick
            # go deep in woods
            # see fairy
            $ grabbed_stick = True
            $ fairy_appeared = True
            jump woods_choice
        "Get out of here" if fairy_appeared:
            #Go back to the bus
            show bg bus
            jump bus_choice
label end:
    scene black with Fade(1.5, 1.0, 0)

    # This ends the game.
    return
