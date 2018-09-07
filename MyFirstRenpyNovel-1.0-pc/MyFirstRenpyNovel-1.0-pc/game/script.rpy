image deathclaw = im.Scale("deathclaw.png", 600, 700)
image big = im.Scale("deathclaw.png", 900, 1000)
image tome = im.Scale("tome.png", 200, 300)
image mushroom = im.Scale("mushroom.png", 700, 700)
image fallout = Frame("fallout.jpg")

define D = Character("Dan", color="#ff0000")

label start:
    play music "sound/bensound-betterdays.mp3"
    play audio "sound/hello.mp3"
    D "Hey..."
    D "Hey, Brie.{w=.2}It's me.{w=.2} It's your pal, Dan."
    D "Listen, you gotta' help me.{w=.2} They did something to me."
    D "I can't really explain it, but they{w=.1}.{w=.1}.{w=.1}.{w=.1} Changed me."
    scene fallout with dissolve
    show deathclaw at truecenter with dissolve
    D "{b}They changed my form.{/b}"
    show deathclaw at right with move
    D "This isn't normal.{w=.2} I'm not supposed to look like this."
    show deathclaw at truecenter with move
    D "They said that if I don't revert back to my original form, then I'll be stuck looking like this {i}forever{/i}."
    D "..."
    D "But there is some bright news.{w=.2} I was able to get my hands on some crusty tome here."
    show deathclaw at left with move
    show tome at truecenter with dissolve
    D "At first glance, it appears to be a guide book."
    D "For some reason, it only repeats the phrase, \"Lol, you wasted money. Play FONV instead\" for 140 pages."
    D "But the last 10 pages are a veritable feast of pro gamer tips to turn me back into my true self."
    D "It says that I gotta' ask someone \"Hey, wanna' hang out?\" and they gotta' replay with \"Yeah.\""
    hide tome with dissolve
    D "So, Brie.{w=.2} Please.{w=.2} Please.{w=.2} Please release me from my curse."
    menu:
        D "{b}Do you wanna' hang out?{/b}"
        "Yeah.":
            jump good_end
        "Nah.":
            jump bad_end
    return

label good_end:
    D "Really?!{w=.2} Thank you!{w=.2} Thank you!{w=.2} Thank-"
    show deathclaw at truecenter with move
    play audio "sound/hnng.mp3"
    D "HNNG!"
    D "I can feel it working!{w=.2} I'm-HNNG-reverting to my original form!"
    hide deathclaw with dissolve
    play audio "sound/hnng.mp3"
    D "HNNNNNNNG!"
    show mushroom at truecenter with dissolve
    play audio "sound/hello.mp3"
    D "I LIVE!!!"
    "Congratulations! You win!"
    "Let's hang out."
    return

label bad_end:
    D "..."
    D "What..?"
    D "No, try that again."
    menu:
        D "{b} Try that again.{/b}"
        "Yeah.":
            jump good_end
        "Nah.":
            jump very_bad_end
    return

label very_bad_end:
    D "...{w} ..."
    D "I thought that you were {i}my friend{/i}."
    D "I thought that you would have done {i}anything{/i} to help me escape this despicable form."
    D "But you betrayed me."
    hide deathclaw with dissolve
    show big at truecenter with dissolve
    D "YOU. {w}BETRAYED. {w}ME."
    D "This form isn't despicable! {i}You{/i} are the one who is despicable."
    play audio "sound/degenerates.mp3"
    D "I'll show you! I'll destroy you! Degenerates like you belong on a cross!"
    menu:
        "{b}Your pal, Dan, attacks. How will you proceed?{/b}"
        "You kidnapped my son, Dan! Time to die!":
            pass
        "You monster! You murdered my wife, Dan! I'm going to kill you!":
            pass
        "Dan, we both know how this has to end. I'm sorry.":
            pass
        "You know, Dan, in a hundred years, when I finally die, I only hope I go to Hell, so I can kill you all over again, you piece of shit.":
            pass
    hide big with dissolve
    "You kick Dan in his forehead and his brain explodes into mist."
    D "You're... {w=.2}Despicable.{w=.2} You're... {w=.2}A degenerate. {w=.2}You're..."
    play audio "sound/hnng.mp3"
    "Dan inhales softly and with his last breath, he says..."
    D "still my nakama{w=.2}.{w=.2}.{w=.2}."
    "Congratulations! You lose!"
    return