#!/usr/bin/env python3

"""Alta3 Research | RZFeeser
    print() - concatenate vs print a series of items"""
#create variable for responses
responses = {'people':{'gravekeeper':{}},'destination':{}, 'items':{'gySel':''}}
path = []

def main():
    print("The year is 2317. The economies of the world are all but collapsed and the few pathetic stakeholders remaining cling to their waning power like a babe to the teat. You've been hiking for days on end looking for gas for your rig you left in the lurch.")
    responses['name'] = input("Snapping out of a daze you'd gotten yourself into the last few miles, you are standing before a aggrevated man you don't know who seemingly came out of nowwhere who intensely demands information from you. \n \n Who the hell are you? Answer me dangit!  ")
    responses['destination']['place'] = input(F"Well {responses['name']}, where the hell do you think you're going?")
    responses['people']['gravekeeper']['answer'] = input(F"I got news for you Columbus, is it possible to get to {responses['destination']['place']} without trompin' across hollowed ground!?   ")
    if responses['people']['gravekeeper']['answer'] == 'no':
        print("\nChrist Almighty! We've got a spicy one here don't we Geebs!")
        path.append("B")
    else: 
        path.append('A')
        responses['people']['gravekeeper']['answer'] = input("At least you've got SOME sense in you. You got sense enough to help me install a fence to prevent spacers like you from commitin' the same mistake?")
    print("\nA man appears some distance behind the scruffy bear in coveralls before you and begins kicking up dust in tattered boots with a tangle of several generations of footwear knotted together barely holding the sides of them to their bearer's ankles. As he walked you could easily imagine them as dog heads with floppy ears under their master's weight. The front of one was ripped clear across the sole and the toes flopped up and down exposing some bare toes through and exaggeratedly long dragging out the side of the rip as if their tongues were dragging beside them from sheer exhaustion, and waiting for the day their tossed and laid to rest once and for all")
    responses['items']['gySel'] = input(F"\nThinking quickly to resovle this situation, you grab... \n  Choose one letter option: a) whistle, b) pencil and paper, c) pocketknife, d) nearby branch   ")

    if responses['items']['gySel'] == "a":
        print("\n You reach into your shirt and pull out your whistle and let out everything you've got. before the man could take another step, your shepard Bones sprints from a nearby position and easily brings down the man, freeing one his boots from further torturous foot pressure and fungal seepage.")
    elif responses['items']['gySel'] == 'b':
        print("\n Grabbing a pencil and paper, you approach the men to take notes of the encounter with these disgruntled men")
    elif responses['items']['gySel'] == 'c':
        print(" \n You discretely extend the blade of your switchknife and step quickly to the man in front before the farther comes any closer.")
    else:
        print("\n Thinking quickly you look around and grab a large branch laying on the ground. It's strong in your hands and feels light enough to swing quickly. Watching the men intently you stand defensively and await for an indication of their intention toward you.")

main()
