
import spacy

"""
this imports spacy
"""

#removes unnecessary warnings from spacy
import warnings
warnings.filterwarnings("ignore")

def main():
    """
    This is the main function, where the user picks between an auto-generated story or a survey
    """
       
    #gives user the choice of taking a questionnaire or using using similarity function to chose a story for them
    question_user = input("Welcome to Hertie MadLibs! How would you prefer to select a story? If you want a questionnaire, enter '1'. If you prefer to be given a story based off your current mood, enter '2'. ")
    if question_user == "1":
        question1, question2, question3 = survey_part1()
        survey_part2(question1, question2, question3)
        #reminds the code to go to survey_part1 and captures q 1-3. Then passing q1-3 through survey_part2
        
    elif question_user == "2": 
        mood_generator()
    
def survey_part1():
    """Having selected the survey option, the code now prompts the user with three initial questions to determine which two stories the user will then choose between"""
    #everything else
    question1 = input("Are you in a rush? (y/n): ")
    question2 = input("Do you like adventures? (y/n): ")
    question3 = input("Do you want to learn something new? (y/n): ")
    return question1, question2, question3

def survey_part2(question1, question2, question3):
    #defining argument/parameter
    """Having answered the first three questions, the user then must answer a final question to determine which of the allocated pair of stories they will 
    receive. Having done that, they are then prompted to fill out the missing words in whichever mad lib story they are assigned."""

    if question1 == "y" and question2 == "y" and question3 == "y":
        question4 = input("Are you having a weird day? (y/n): ")
    
        if question4 == "y":
            #Weird Day is selected
            noun = input("Enter a noun: ")
            famous = input("Enter a famous person: ")
            nounplur = input("Enter a plural noun: ")
            noun2 = input("Enter a noun: ")
            adjective1 = input("Enter an adjective: ")
            verbing = input("Enter a verb ending in ing: ")
            adjective2 = input("Enter an adjective: ")
            song = input("Enter a song name: ")
            adjective3 = input("Enter an adjective: ")
            verbed = input("Enter a verb in the past tense: ")
            adjective4 = input("Enter an adjective: ")
            verbing2 = input("Enter a verb ending in ing: ")
            supermodel = input ("Enter a supermodel: ")
            place = input("Enter a place: ")
            
            
            print("Once upon a time there was a" , noun + ". It had" , adjective1 + " ",  nounplur + "! One day it met " , famous + "on the side of the" , place + " they were" , verbing + ". It was very" , adjective2 + "; they both looked like hobos! All of the sudden they started singing" , song + " really loudly. They ", verbed + " really ", adjective3 + "! ", famous + " started", verbing2 + " with" , supermodel + ". They looked really" , adjective4 + "!")
              
        else: 
        #homework excuses is selected
            adjective1 = input("Enter an adjective: ")
            noun1 = input("Enter the plural form of a noun: ")
            adjective2 = input("Enter an adjective: ")
            sillyword1 = input("Enter a silly word: ")
            noun2 = input("Enter a noun: ")
            animal1 = input("Enter an animal: ")
            verb1 = input("Enter a verb in the past tense: ")
            occupation1 = input("Enter an occupation: ")
            adjective3 = input("Enter an adjective: ")
            adjective4 = input("Enter an adjective: ")
            noun3 = input("Enter the plural form of a noun: ")
            noun4 = input("Enter a noun: ")
            noun5 = input("Enter a noun: ")
            number1 = input("Enter a number: ")
            sillyword2 = input("Enter a silly word: ")
          
            print("As a teacher, I hear a lot of", adjective1 + " excuses about why my", noun1 + " don’t turn in their homework. Here are the top most", adjective2 + " ones of all time. An alien from Planet", sillyword1 + " landed in my backyard, and when my", noun2 + " asked me to take out the garbage, I got sucked up into the", noun3 +"-ship! My pet", animal1 + " ate it, then", verb1 + " it up, then ate it again! I’m running for", occupation1 + "of the United States, and I had to work on my", adjective3 + " campaign speech. On the way home from school, a band of", adjective4 + "pirates looking for gold", noun3 + "insisted I turn over my backpack—or walk the", noun4 + "! I was too busy breaking the world record for most", noun5 + "eaten in", number1 + "minutes while balancing on one", sillyword2 + ".")
    
    elif question1 == "y" and question2 == "y" and question3 == "n":
        question4 = input("Do you like being outdoors? (y/n):")
        question5 = input("Do you like shopping? (y/n):")
        if question4 == "y" and question5 == "n":
            
            #Camping story is chosen
            sillyname1 = input("Enter a silly name: ")
            noun1 = input("Enter an noun: ")
            adjectivefeeling1 = input("Enter adjective that is a feeling: ")
            verb1 = input("Enter a verb: ")
            adjectivefeeling2 = input("Enter adjective that is a feeling: ")
            animal1 = input("Enter an animal: ")
            verb2 = input("Enter a verb: ")
            color1 = input("Enter a color: ")
            verb3 = input("Enter a verb ending in ´ing´: ")
            adverb1 = input("enter an adverb ending in ´ly´: ")
            number1 = input("Enter a Number that is a measure of time: ")
            adjective2= input("Enter an adjective: ")
            animal2 = input("Enter an animal: ")
            sillyword1= input("Enter a silly word: ")
            noun2= input ("Enter a noun: ")
        
            print("This weekend I am going camping with" , sillyname1 + " I packed my lantern, sleeping bag, and", noun1 + " I am so", adjectivefeeling1 + "to",  verb1 +  "in a tent. I am", adjectivefeeling2 + "we might see a", animal1 + ", they are kind of dangerous. We are going to hike, fish, and", verb2 + 
            "I have heard that the", color1 + "lake is great for", verb3 + ". Then we will", adverb1 + "hike through the forest for", number1 + ". If I see a", adjective2 + animal2 + 
            "while hiking, I am going to bring it home as a pet! At night we will tell", sillyword1+ "stories and roast", noun2 + "around the campfire!!")
              
        elif question4 == "y" and question5 == "y":
            #Summertime story is chosen
            sillyword1 = input("Enter a silly word: ")
            noun1 = input("Enter the plural form of a noun: ")
            noun2 = input("Enter a city: ")
            verb1 = input("Enter a verb in the past tense: ")
            sillyword2 = input("Enter a silly word: ")
            verb2 = input("Enter a verb: ")
            noun3 = input("Enter the plural form of a noun: ")
            verb3 = input("Enter a verb in the past tense: ")
            noun4 = input("Enter the plural form of a noun: ")
            verb4 = input("Enter a verb in the past tense: ")
            language1 = input("Enter a language: ")
            sillyword3 = input("Enter a silly word: ")
            bodypart1 = input("Enter a body part: ")
          
            print("It was the summer of", sillyword1 + " songs. We danced in", noun1 + " all over downtown", noun2 + " until 4 a.m. and", verb1 + sillyword2 + " for six hours in the daytime. I liked that he could ", verb2 + "all the", noun3 + ". He was in a class ahead of me. He", verb3 + noun4 + ", so I did too. It was six weeks of summer. I don’t know how I", verb4 + ". I almost got the ", language1 + "word for", sillyword3 + " tattooed on my", bodypart1 + "when I returned home. But I didn’t. It was enough that I had lived.")
    
        elif question4 == "n" and question5 == "y":
            #going to the mall is selected
            number1 = input("Enter a number: ")
            adjective1 = input("Enter an adjective: ")
            sillyname1 = input("Enter a silly name: ")
            animal1 = input("Enter a silly animal: ")
            noun1 = input("Enter a noun in the plural form: ")
            verb1 = input("Enter a verb ending in 'ing': ")
            noun2 = input("Enter a noun in the plural form: ")
            adjective2 = input("Enter an adjective: ")
            adjective3 = input("Enter an adjective: ")
            noun3 = input("Enter a location: ")
            noun4 = input("Enter a noun: ")
  
            print("Yesterday, me and", number1 + " of my friends took a trip to the mall. While we were there we saw this really", adjective1 + " store called", sillyname1 + " pets. We saw", animal1 + " and", noun1 + verb1 + " in the store display. So we had to go inside. They had miniature", noun1 + " and", adjective2 + " little bunnies. We even got to play with the", adjective3 + " in the", noun2 + " I want a/an", noun3 + " so much!")
    
      
        elif question4 == "n" and question5 == "n":
            #The Short Story is selected
            noun1 = input("Enter a plural noun ")
            occupation1 = input("Enter an occupation: ")
            animals1 = input("Enter an animal, plural: ")
            city1 = input("Enter a city: ")
            verb1 = input("Enter a verb: ")
            noun2 = input("Enter a noun: ")
      
            print("In the book War of the", noun1 + " , the main character is an anonymous", occupation1 + " who records the arrival of", animals1 + " in", city1 + 
          " . Needless to say, havoc reigns as the", animals1 + " continue to", verb1 + " everything in sight, until they are killed by the common", noun2)
    
        elif question1 == "y" and question2 == "n" and question3 == "n":
            question4 = input("Are you hungry? (y/n): ")
            if question4 == "y":
                #How to make a PBJ is selected
                color1= input("Enter a verb color: ")
                noun1= input("Enter a noun/object: ")
                sillyword1= input("Enter an silly word: ")
                adjective1 = input("Enter an adjective: ")
                adjective2 = input("Enter an adjective: ")
                number1 = input("Enter a verb ending in 'ing': ")
                noun2 = input("Enter a noun: ")
                verb1 = input("Enter a verb: ")
                verb2 = input("Enter a verb: ")
                noun3 = input("Enter a noun: ")
                  
                print("Select the type of bread you want to use. Many prefer the taste of", color1 + " bread, while others prefer", noun1 + " bread because it is healthy. Then, choose the flavor of Jam/Jelly. I personally prefer", sillyword1 + " jam, but you can use whatever you want. Next, choose the type of peanut butter–either", adjective1 + " or", adjective2 + " . Take out", number1 + " slice(s) of bread and use a", noun2 + " to", verb1 + " the jam all over one of the pieces of bread. Now", verb2 + " the peanut butter on the other piece of bread. Put them together, and you have a PB&J", noun3 ) 
         
            else:
              #Weekend is selected
              adverb1 = input("Enter an adverb: ")
              noun1 = input("Enter a place: ")
              noun2 = input("Enter the plural form of a noun: ")
              verb1 = input("Enter a verb ending in 'ing': ")
              verb2 = input("Enter a verb ending in 'ing: ")
              adjective1 = input("Enter an adjective: ")
              adjective2 = input("Enter an adjective: ")
              bodypart1 = input("Enter a bodypart: ")
              noun3 = input("Enter a noun in the plural form: ")
              adjective3 = input("Enter an adjective: ")
              verb3 = input("Enter a verb: ")
              noun4 = input("Enter the plural form of a noun: ")
              adjective4 = input("Enter an adjective: ")
              sillyword1 = input("Enter a silly word: ")
              noun5 = input("Enter a noun: ")
              sillyname1 =input("Enter a silly name: ")
              
              print("Ahhh, it is", adverb1 + " Saturday! That means I don’t have to go to", noun1 + "and teach my", noun2 + " all about adding and", verb1 + ". I should probably spend some time", verb2 + "at my second job as a/an", adjective1+  ", undercover-detective superhero! First, let me find my", adjective2 + "cape and", bodypart1 + "-high boots. I wouldn’t want any of my", noun3 + "to know my true", adjective3 + " identity! Now that I’m dressed, I’ll listen in on my walkie-", verb3 + "-ie to see if there are any", noun4 + "in distress or anyone who needs my", adjective4 + " assistance.", sillyword1 + "! A/An", noun5 + "stuck in a tree! That sounds like a job for Mrs.", sillyname1 + ", super teacher and superhero!")
    
    
    elif question1 == "y" and question2 == "n" and question3 == "n": 
        question4 = input("Do you like your hair short? (y/n): ")
        if question4 == "y":
            #The Worst Haircut is selected
            noun1 = input("Enter an Noun: ")
            noun2 = input("Enter a Noun: ")
            adjective1 = input("Enter an adjective: ")
            adjective2 = input("Enter an adjective: ")
            exclamation1 = input("Enter an exclamation: ")
     
            print("Argh! I just had the absolutely worst day at the barber. First, I was running late for my 4:00pm appointment because a", noun1 + " got hit by a", noun2 + " on the freeway, causing major traffic. Then, when I finally arrive at the shop, I find my slot has been taken by some", adjective1 + " man. ´Um excuse me?´ I said, ´You’re in my spot´. The man looked up at me with", adjective2 + " eyes, and drawled ´I was here first. Wait your turn.´ Fuming, I turned to the barber: ", exclamation1 + " ! ")
         
        else:
            #A friendly call is selected
            verb1 = input("Enter a verb ending: ")
            adjective1 = input("Enter an adjective: ")
            verb2 = input("Enter a verb: ")
            bodypart = input("Enter a body part: ")
            adverb = input("Enter an adverb: ")
            noun1 = input("Enter a noun: ")
            verb3 = input("Enter a verb: ")
            animal = input("Enter an animal: ")
            noun2 = input("Enter a noun: ")
            verb4 = input("Enter a verb: ")
            adjective2 = input("Enter an adjective: ")
            color = input("Enter an color: ")
              
            print("Once a day I call my friend to", verb1 + " them. I do it so they know how", adjective1 + " they are. Unfortunately they never", verb2 + " though, so instead i start brushing my ", bodypart + ". Considering I have a/an" , adverb + " thin", bodypart + ", when I call my friend, they always tell me to buy a", noun1 + " to", verb3 + " my problems. I therefore call my", animal + "and tell them to get me a", noun2 + " in order to", verb4 + ". Finally, when I hang up the very", adjective2 + " call, I only see" , color + ".")
 
    elif question1 == "n" and question2 == "y" and question3 == "n":
        question4 = input("Do you like rollercoasters? (y/n): ")
        if question4 == "y":
            #The Fun Park is selected
            adjective = input("Enter an adjective: ")
            plurnoun = input("Enter a plural noun: ")
            adjective2 = input("Enter an adjective: ")
            noun = input("Enter a noun: ")
            adverb = input("Enter an adverb: ")
            number = input("Enter a number: ")
            verbpast = input("Enter a past-tense verb: ")
            adjest = input("Enter an adjective with an est ending: ")
            verbpast2 = input("Enter a past-tense verb: ")
            adverb2 = input("Enter an adverb: ")
            adjective3 = input("Enter an adjective: ") 
            
            print("Today, my fabulous camp group went to a (an)" , adjective + " amusement park. It was a fun park with lots of cool" , plurnoun + " and enjoyable play structures. When we got there, my kind counselor shouted loudly, 'Everybody off the" , noun + "!' We all pushed out in a terrible hurry. My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn't figure out what exciting thing to do first. I saw a scary roller coaster I really liked so, I" , adverb + " ran over to get in the long line that had about" , number + " people in it. When I finally got on the roller coaster I was" , verbpast + ". In fact I was so nervous my two knees were knocking together. This was the" , adjest + " ride I had ever been on! In about two minutes I heard the crank and grinding of the gears. That’s when the ride began! When I got to the bottom, I was a little" , verbpast2 + " but I was proud of myself. The rest of the day went" , adverb2 + ". It was a(n)" , adjective3 + " day at the fun park.") 
         
        else:
            #Family vacation is selected
            adjective1 = input("Enter an adjective: ")
            adjective2 = input("Enter an adjective: ")
            noun1 = input("Enter a noun: ")
            noun2 = input("Enter a noun: ")
            noun3 = input("Enter the plural form of a noun: ")
            noun4 = input("Enter a noun: ")
            noun5 = input("Enter the plural form of a noun: ")
            verb1 = input("Enter a verb ending in ‘ing’: ")
            verb2 = input("Enter a verb ending in ‘ing’: ")
            noun6 = input("Enter the plural form of a noun: ")
            verb3 = input("Enter a verb ending in ‘ing’: ")
            noun7 = input("Enter a noun: ")
            noun8 = input("Enter a noun: ")
            bodypart1 = input("Enter a body part: ")
            noun9 = input("Enter a place: ")
            verb4 = input("Enter a verb ending in ‘ing’: ")
            adjective3 = input("Enter an adjective: ")
            number1 = input("Enter a number: ")
            noun10 = input("Enter the plural form of a noun: ")
            
            print("A vacation is when you take a trip to some", adjective1 + " place with your", adjective2 + " family. Usually you go to some place that is near a/an", noun1 + " or up on a/an", noun2 + ". A good vacation place is one where you can ride", noun3 + " or play", noun4 + " or go hunting for", noun5 + ". I like to spend my time", verb1 + " or", verb2 + ". When parents go on a vacation, they spend their time eating three", noun6 + " a day, and fathers play golf, and mothers sit around", verb3 + ". Last summer, my little brother fell in a/an", noun7 + " and got poison", noun8 + "all over his", bodypart1 + ". My family is going to go to the", noun9 + " and I will practice", verb4 + ". Parents need vacations more than kids because parents are always very", adjective3 + " and because they have to work", number1 + " hours every day all year making enough", noun10 + " to pay for the vacation.")
        
    elif question1 == "n" and question2 == "y" and question3 == "y":
        question4 = input("Sonic? (y/n): ")
        if question4 == "y":
            #sonic story is selected
            adjective1 = input("Enter an adjective: ")
            adjective2 = input("Enter an adjective: ")
            noun1 = input("Enter a noun: ")
            noun2 = input("Enter a noun: ")
            adjective3 = input("Enter a adjective: ")
            noun3 = input("Enter a noun: ")
            noun4 = input("Enter a noun in the plural form: ")
            adjective4 = input("Enter an adjective: ")
            number1 = input("Enter a number: ")
            adjective5 = input("Enter an adverb: ")
            sillyname1 = input("Enter a silly name: ")
            noun5 = input("Enter a noun in plural form: ")
            adjective6 = input("Enter an adjective: ")
            noun6 = input("Enter a noun that is a place: ")
            noun7 = input("Enter a noun in the plural form: ")
            verb1 = input("Enter a verb: ")

            print("Sonic’s abode is a very", adjective1 + " place. At first glance, it seems like a/an", adjective2 + " cave, but if you look closer, you’ll see it’s actually a comfortable", noun1 + ". For one, Sonic has a super-cozy bean bag", noun2 + ". When he feels like listening to some", adjective3 + " tunes from the 1980s, Sonic turns on his old-school", noun3 + " pulls out his collection of", noun4 + " and jams out. In addition to great tunes, Sonic has plenty of", adjective4 + " equipment to keep him busy. There’s a dryer that Sonic uses as a treadmill to run", number1 + " miles a day. He has a/an", adjective5 + " ping pong table where he plays against", sillyname1 + ". And for that final touch, Sonic hung", noun5 + " all over his cave walls. He’s got a/an", adjective6 + " photo of the", noun6 + " next to a poster of", noun7 + ". It may not be much, but Sonic loves to", verb1 + " in his cave all the time.")
        else:
            #the stranger is selected
            verb1 = input("Enter a verb ending in 'ing': ")
            exclamation = input("Enter an exclamation: ")
            adjective1 = input("Enter an adjective: ")
            sillyword1 = input("Enter a silly word: ")
            noun1 = input("Enter a noun: ")
            verb2 = input("Enter a verb ending in 'ing': ")
            noun2 = input("Enter a noun: ")
            adjective2 = input("Enter an adjective: ")
            number1 = input("Enter a number: ")
            adverb1 = input("Enter an adverb: ")
            adjective3 = input("Enter an adjective: ")
            adjective4 = input("Enter an adjective: ")
            room = input("Enter a type of room: ")   
              
            print("I was busy", verb1 + " in my living room on a rainy afternoon when I heard a knock on my door." , exclamation + "! I shouted, and ran to quickly open the door. There, at my doorstep stood a disturbingly" , adjective1 + " individual. “Hello,” he said with a sweeping bow. “My name is Mr.", sillyword1 + ". I received a call that there was a" , noun1 + " spotted near this location. I work for the department of", noun1 + " and have been tasked with", verb2 + " every", noun1 + " I can find. May I come in?” “Well of course!” I replied, “But I can assure you I haven't seen a", noun1 + " in quite some time. May I get you a cup of melted" , noun2 + "?” “If it’s no trouble,” the man said while eyeing me suspiciously. “You have quite the" , adjective2 + " house, I’m sure you could fit at least" , number1 + " " , noun1 + "s in here.” Sweat started to drip from my forehead. “I’m sure I don’t know what you mean.” Hands shaking, I carefully poured the man his hot cup of melted" , noun2 + ". The man sipped his cup" , adverb1 + ". “Mmmm, that’s", adjective3 + ". Well if you do spot any", noun1 + "s, don’t hesitate to give me a call.” With a fluid motion, he produced a card from his coat. Relieved, I took his card and escorted him out. “Have a" , adjective4 + " day!” I called after him. That was a close one, I thought to myself as I went to my hidden" , room + " to check on my secret" , noun1 + ".")
    
    elif question1 == "n" and question2 == "n" and question3 == "y":
        question4 = input("Are you good at geography? (y/n):")
        if question4 == "y":
            #“The Island Nation” is selected
            sillyword1 = input("Enter a silly word: ")
            country1 = input("Enter a country: ")
            animals = input("Enter an animal (plural): ")
            number = input("Enter a number: ")
            country2 = input("Enter a country: ")
            adjective1 = input("Enter aan adjective: ")
            nounplur = input("Enter a plural noun: ")
            verbing = input("Enter a verb ending in ing: ")
            adjective2 = input("Enter an adjective: ")
            sillyword2 = input("Enter a silly word: ")
            noun = input("Enter a noun: ")
            verbing2 = input("Enter a verb ending in ing: ")
            animals2 = input("Enter an animal (plural): ")
            adjective3 = input("Enter aan adjective: ")
            noun2 = input("Enter a noun: ")
            adjective4 = input("Enter aan adjective: ")
            
            print("Located just off the coast of " , country1 + " is the small island nation of " , sillyword1 + ". Though it remains an obscure place to most, with a population of barely " + number + " the island boasts a " + adjective1 + " culture and " + adjective2 + " history. The island’s history has its roots in the legacy of colonization, and its subsequent war for independence from" , country2 + ". Since then, the island has been ruled by a " + adjective2 + " dictatorship reviled throughout the international community for its arsenal of deadly " + nounplur + ". Despite this, the people of " + sillyword1 + " live relatively " + adjective3 + " lives. Every year residents gather on the beach to celebrate their independence day by " + verbing + " until they collapse from exhaustion. Aside from independence day, the most celebrated holiday in " + sillyword1 + " is the Festival of " + sillyword2 + ", where locals dress up as " + animals + "and perform a " + adjective4 + " display of " + verbing2 + ". Tourism makes up a large part of the " + sillyword1 + " economy, but I must warn you, should you decide to visit, make sure to pack a " + noun2 + " in your bag. The island has extremely aggressive " + animals2 + " that have been known to attack tourists on sight, so make sure to keep your " + noun2 + " with you at all times!") 
                  
        else:
            alphabet1 = input("Enter a letter of the alphabet: ")
            adjective1 = input("Enter an adjective: ")
            adjective2 = input("Enter an adjective: ")
            noun2 = input("Enter a noun: ")
            noun3 = input("Enter a noun: ")
            adjective3 = input("Enter an adjective: ")
            occupation1 = input("Enter an occupation: ")
            bodypart1 = input("Enter a body part: ")
            adjective4 = input("Enter an adjective: ")
            noun4 = input("Enter a noun: ")
            sillyname1 = input("Enter a silly name: ")
            noun5 = input("Enter the plural form of a noun: ")
            noun6 = input("Enter a noun: ")
            adjective5 = input("Enter an adjective: ")
            adverb1 = input("Enter an adverb: ")
            noun7 = input("Enter a noun: ")
            
            print("Do you want straight", alphabet1 + " on your report card? Do you want to bring home comments like “excellent” and “", adjective1 + "” on all your tests and", noun1 + "? Follow our",  adjective2 + "-fire guide to becoming the teacher’s", noun2 + " and you’ll be at the top of the", noun3 + " in no time! Tell your teacher every day that she looks", adjective3 + ". Everyone loves compliments, even", occupation1 + "! Raise your", bodypart1 + " to answer questions or volunteer for",  adjective4 + "duties, like erasing the", noun4 + "-board or walking", sillyname1 + " to the bathroom. Do extra credit whenever possible. If you have to do a report on the", noun5 + " of Liberty, build one out of Popsicle sticks and", noun6 + " too! Stay after class to help out with", adjective5 + " chores around the classroom. Use the extra time with your teacher to butter her up—she’ll think", adverb1 + "of you next time she grades one of your", noun7 + "!")
    
    elif question1 == "n" and question2 == "n" and question3 == "n":
        question4 = input("Are you having a horrible day? (y/n):")
        if question4 == "y":
            noun1 = input("Enter a noun that is object: ")
            adjective1 = input("Enter an adjective: ")
            noun2 = input("Enter a noun of a city: ")
            adjective2= input("Enter an adjective of a feeling: ")
            occupation1= input("Enter an occupation: ")
            adjective3 = input("Enter an adjective: ")
            animal1 = input("Enter an animal: ")
            adjective4 = input("Enter an adjective: ")
            noun3 = input("Enter a noun: ")
            number1 = input("Enter a number: ")
            verb1 = input("Enter a verb ending in ´ing´: ")
            adjective5 = input("Enter an adjective: ")
            adjective6 = input("Enter an adjective: ")
            noun4 = input("Enter a noun: ")
            verb2 = input("Enter a verb: ")
            verb3 = input("Enter a verb ending in ´ed: ")

            print("Jenny Kowalski looked at the warped" , noun1 + " in her hands and felt angry. She walked over to the window and reflected on her" , adjective1 + " surroundings. She had always loved picturesque", noun2 + " with its calm, cloudy cliffs. It was a place that encouraged her tendency to feel", adjective2 + " . Then she saw something in the distance, or rather someone. It was the figure of Harry Blacksmith. Harry was a lovable, handsome", occupation1 + " . Jenny gulped. She glanced at her own reflection. Her friends saw her as a", adjective3 + " weirdo. The wind blew like rampaging", animal1 +  ", making Jenny anxious. As Jenny stepped outside and Harry came closer, she could see the", adjective4 + " smile on his face. ´I am here because I want´", noun3 + " ´, Harry bellowed, in a patient tone. He slammed his fist against Jenny's chest, with the force of", number1 + " .I", verb1 + "  love you, Jenny Kowalski. Jenny looked back, even more anxious. ´Harry, get out of my house,´ she replied. They looked at each other with", adjective5 + " feelings like two", adjective6 + noun4 + ". Suddenly, Harry lunged forward and tried to", verb2 + " Jenny in the face. She", verb3 + " Jenny Kowalski went back inside and made herself a nice glass of port.")
    
        else:
            #Last day of work story
            verb1 = input("Enter a verb: ")
            adjective1 = input("Enter an adjective: ")
            verb2 = input("Enter a verb: ")
            adverb = input("Enter an adverb: ")
            verb3 = input("Enter a verb: ")
            adjective2 = input("Enter an adjective: ")
            bodypart = input("Enter a body part: ")
            color = input("Enter a color: ")
            verbing = input("Enter a verb ending in ing: ")
            bodypart2 = input("Enter a body part: ")
            noun2 = input("Enter a noun: ")
            animal = input("Enter an animal: ")
            noun3 = input("Enter a noun: ")
    
            print("On my last day of work I really enjoy to " + verb1 + " with my " + adjective1 + " coworker. We start off by " + verbing + ", before eating. When I eat too much, however, my " + bodypart +" starts to hurt. It " + adverb + " hurts… it hurts so much that even my " + bodypart2 + " starts aching. It almost makes me not want to keep going. But then I think that its my last day at work and so I buy " + noun3 + " for everybody instead. Once the " + noun3 + " is bought, everyone can " + verb3 + " together. Stacy even brought her " + animal + " “Rocky” again. It only takes 10 minutes until “Rocky” chews off the " + noun2 + " though, which makes the last day at work even more entertaining. I "+ verb2 + " when this happens. I think that I will really miss this place, especially during the " + adjective2 + " evenings, where you can see the beautiful " + color + " sunset from the office terrace.") 
 
def mood_generator(): 
    """Having selected option #2, the code will prompt the user to enter a quick description of their current mood."""
    
    #ask user to enter a word or two about their current mood, use natural language processing to find the story with the closest similarity
    feeling = input("How are you feeling today? (1 sentence or less): ")
    nlp = spacy.load("en_core_web_sm")  # make sure to use larger package!
    mood = nlp(feeling)
    storyranking = storyrank(mood)
    
    #determine which story has the highest similarity
    max_storyranking = max(storyranking)
    
    auto_selection(storyranking, max_storyranking)
    
def storyrank(mood): 
    """
    For each story, creates a variable equal to that story's similarity to the user's mood input and places them in an array.
    """
    nlp = spacy.load("en_core_web_sm")
    
    story1 = nlp("This weekend I am going camping with. I packed my lantern, sleeping bag, and. I am so to in a tent. I am we might see a , they are kind of dangerous. We are going to hike, fish, and. I have heard that the lake is great for . Then we will  hike through the forest for . If I see a while hiking, I am going to bring it home as a pet! At night we will tell stories and roast around the campfire")
    story2 = nlp("Do you want straight  on your report card? Do you want to bring home comments like “excellent” and “ ” on all your tests and ? Follow our -fire guide to becoming the teacher’s , and you’ll be at the top of the  in no time! Tell your teacher every day that she looks . Everyone loves compliments, even ! Raise your  to answer questions or volunteer for  duties, like erasing the board or walking to the bathroom. Do extra credit whenever possible. If you have to do a report on the of Liberty, build one out of Popsicle sticks and , too! Stay after class to help out with chores around the classroom. Use the extra time with your teacher to butter her up—she’ll think  of you next time she grades one of your !")
    story3 = nlp("Select the type of bread you want to use. Many prefer the taste of  bread, while others prefer bread because it is healthy. Then, choose the flavor of Jam Jelly. I personally prefer jam, but you can use whatever you want. Next, choose the type of peanut butter–either  or . Take out slice of bread and use a  to  the jam all over on of the pieces of bread. Now  the peanut butter on the other piece of bread. Put them together, and you have a PB&J")
    story4 = nlp("Jenny Kowalski looked at the warped  in her hands and felt angry. She walked over to the window and reflected on her surroundings. She had always loved picturesque with its calm, cloudy cliffs. It was a place that encouraged her tendency to feel . Then she saw something in the distance, or rather someone. It was the figure of Harry Blacksmith. Harry was a lovable, handsome . Jenny gulped. She glanced at her own reflection. Her friends saw her as a  weirdo. The wind blew like rampaging , making Jenny anxious. As Jenny stepped outside and Harry came closer, she could see the  smile on his face. 'I am here because I want ,' Harry bellowed, in a patient tone. He slammed his fist against Jenny's chest, with the force of  . 'I love you, Jenny Kowalski.' Jenny looked back, even more anxious. 'Harry, get out of my house,' she replied. They looked at each other with feelings, like two .Suddenly, Harry lunged forward and tried to Jenny in the face. She Jenny Kowalski went back inside and made herself a nice glass of port.")
    story5 = nlp("In the book War of the , the main character is an anonymous who records the arrival of in. Needless to say, havoc reigns as the continue to everything in sight, until they are killed by the common.")
    story6 = nlp("Once upon a time there was a . It had ! One day it met  on the side of the they were . It was very ; they both looked like hobos! All of the sudden they started singing really loudly. They  really ! started with . They looked really !")
    story7 = nlp("Today, my fabulous camp group went to a amusement park. It was a fun park with lots of cool and enjoyable play structures. When we got there, my kind counselor shouted loudly, 'Everybody off the .' We all pushed out in a terrible hurry. My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn't figure out what exciting thing to do first. I saw a scary roller coaster I really liked so, I ran over to get in the long line that had about people in it. When I finally got on the roller coaster I was. In fact I was so nervous my two knees were knocking together. This was the ride I had ever been on! In about two minutes I heard the crank and grinding of the gears. That’s when the ride began! When I got to the bottom, I was a little  but I was proud of myself. The rest of the day went . It was a day at the fun park.")
    story8 = nlp("Yesterday, me and of my friends took a trip to the mall. While we were there we saw this really store called  Pets. We saw and in the store display. So we had to go inside. They had miniature and little bunnies. We even got to play with the  in the . I want a/an  so much!")
    story9 = nlp("Once a day I call my friend to  them. I do it so they know how they are. Unfortunately they never though, so instead i start brushing my  Considering I have a/an thin , when I call my friend, they always tell me to buy a to my problems. I therefore call my  and tell them to get me a in order to . Finally, when I hang up the very call, I only see")
    story10 = nlp("On my last day of work I really enjoy to  with my  coworker. We start off by , before eating. When I eat too much, however, my starts to hurt. It  hurts… it hurts so much that even my  starts aching. It almost makes me not want to keep going. But then I think that its my last day at work and so I buy for everybody instead. Once the is bought, everyone can together. Stacy even brought her “Rocky” again. It only takes 10 minutes until “Rocky” chews off the  though, which makes the last day at work even more entertaining. I when this happens. I think that I will really miss this place, especially during the  evenings, where you can see the beautiful  sunset from the office terrace.")
    story11 = nlp("Argh! I just had the absolutely worst day at the barber. First, I was running late for my 4:00pm appointment because a got hit by a  on the freeway, causing major traffic. Then, when I finally arrive at the shop, I find my slot has been taken by some  man. “Um excuse me?” I said, “You’re in my spot”. The man looked up at me with eyes, and drawled “I was here first. Wait your turn.” Fuming, I turned to the barber, !")
    story12 = nlp("I was busy  in my living room on a rainy afternoon when I heard a knock on my door. ! I shouted, and ran to quickly open the door. There, at my doorstep stood a disturbingly  individual. “Hello,” he said with a sweeping bow. “My name is Mr. . I received a call that there was a spotted near this location. I work for the department of , and have been tasked with every I can find. May I come in?” “Well of course!” I replied, “But I can assure you I haven't seen a  in quite some time. May I get you a cup of melted ? If it’s no trouble,” the man said while eyeing me suspiciously. “You have quite the  house, I’m sure you could fit at least s in here.” Sweat started to drip from my forehead. “I’m sure I don’t know what you mean.” Hands shaking, I carefully poured the man his hot cup of melted . The man sipped his cup . “Mmmm, that’s . Well if you do spot any s, don’t hesitate to give me a call.” With a fluid motion, he produced a card from his coat. Relieved, I took his card and escorted him out. “Have a day!” I called after him. That was a close one, I thought to myself as I went to my hidden  to check on my secret .")
    story13 = nlp("Located just off the coast of is the small island nation of . Though it remains an obscure place to most, with a population of barely , the island boasts a culture and history. The island’s history has its roots in the legacy of colonization, and its subsequent war for independence from. Since then, the island has been ruled by a dictatorship reviled throughout the international community for its arsenal of . Despite this, the people of live relatively ives. Every year residents gather on the beach to celebrate their independence day by  until they collapse from exhaustion. Aside from independence day, the most celebrated holiday in is the Festival of , where locals dress up as  and perform a  Tourism makes up a large part of the economy, but I must warn you, should you decide to visit, make sure to pack a  in your bag. The island has extremely aggressive that have been known to attack tourists on sight, so make sure to keep your  with you at all times!")
    story14 = nlp("As a teacher, I hear a lot of  excuses about why my  don’t turn in their homework. Here are the top most  ones of all time . . .An alien from Planet  landed in my backyard, and when my  asked me to take out the garbage, I got sucked up into the  -ship!  My pet  ate it . . . then  it up . . . then ate it again! I’m running for  of the United States, and I had to work on my  campaign speech. On the way home from school, a band of  pirates looking for gold  plural insisted I turn over my backpack—or walk the ! I was too busy breaking the world record for most  eaten in  minutes while balancing on one")
    story15 = nlp("A vacation is when you take a trip to some  place with your  family. Usually you go to some place that is near a/an or up on a/an . A good vacation place is one where you can ride or play or go hunting for . I like to spend my time or . When parents go on a vacation, they spend their time eating three a day, and fathers play golf, and mothers sit around . Last summer, my little brother fell in a an and got poison  all over his. My family is going to go to the , and I will practice . Parents need vacations more than kids because parents are always very  and because they have to work  hours every day all year making enough to pay for the vacation.")
    story16 = nlp("Ahhh, it’s Saturday! That means I don’t have to go to and teach my  all about adding and . I should probably spend some time  at my second job as a/an  , undercover-detective superhero! First, let me find my  cape and high boots. I wouldn’t want any of my to know my true  identity! Now that I’m dressed, I’ll listen in on my walkie to see if there are any  in distress or anyone who needs my  assistance! A/An stuck in a tree! That sounds like a job for Mrs. , super teacher and superhero!")
    story17 = nlp("Sonic’s abode is a very  place. At first glance, it seems like a/an  cave, but if you look closer, you’ll see it’s actually a comfortable . For one, Sonic has a super-cozy beanbag . When he feels like listening to some  tunes from the 1980s, Sonic turns on his old-school , pulls out his collection of , and jams out. In addition to great tunes, Sonic has plenty of  equipment to jeep him bust. There’s a dryer that Sonic uses as a treadmill to run miles a day. He has a/an  ping pong table where he plays against . And for that final touch, Sonic hung  all over his cave walls. He’s got a/an  photo of the  next to a poster of . It may not be much, but Sonic loves to  in his cave all the time.")
    story18 = nlp("It was the summer of  songs. We danced in  all over downtown  until 4 a.m. and  for six hours in the daytime. I liked that he could  all the. He was in a class ahead of me. He  Marlboro Reds, so I did too. It was six weeks of summer. I don’t know how I. I almost got the word for  tattooed on my  when I returned home. But I didn’t. It was enough that I had lived.")
          
    #assign each story a value equal to its similarity to the user's mood input
    story1rank = mood.similarity(story1)
    story2rank = mood.similarity(story2)
    story3rank = mood.similarity(story3)
    story4rank = mood.similarity(story4)
    story5rank = mood.similarity(story5)
    story6rank = mood.similarity(story6)
    story7rank = mood.similarity(story7)
    story8rank = mood.similarity(story8)
    story9rank = mood.similarity(story9)
    story10rank = mood.similarity(story10)
    story11rank = mood.similarity(story11)
    story12rank = mood.similarity(story12)
    story13rank = mood.similarity(story13)
    story14rank = mood.similarity(story14)
    story15rank = mood.similarity(story15)
    story16rank = mood.similarity(story16)
    story17rank = mood.similarity(story17)
    story18rank = mood.similarity(story18)
    
    storyranking = [story1rank ,  story2rank , story3rank , story4rank ,  story5rank , story6rank , story7rank , story8rank ,  story9rank , story10rank , story11rank , story12rank ,  story13rank , story14rank , story15rank , story16rank ,  story17rank , story18rank]
    
    return storyranking   
      

def auto_selection(storyranking, max_storyranking):
    """
    Selects the story with the highest similarity and asks the user to input their words to finish the mad lib story.
    """

    if max_storyranking == storyranking[0]:
        #Camping story is chosen
        sillyname1 = input("Enter a silly name: ")
        noun1 = input("Enter an noun: ")
        adjectivefeeling1 = input("Enter adjective that is a feeling: ")
        verb1 = input("Enter a verb: ")
        adjectivefeeling2 = input("Enter adjective that is a feeling: ")
        animal1 = input("Enter an animal: ")
        verb2 = input("Enter a verb: ")
        color1 = input("Enter a color: ")
        verb3 = input("Enter a verb ending in ´ing´: ")
        adverb1 = input("enter an adverb ending in ´ly´: ")
        number1 = input("Enter a Number that is a measure of time: ")
        adjective2= input("Enter an adjective: ")
        animal2 = input("Enter an animal: ")
        sillyword1= input("Enter a silly word: ")
        noun2= input ("Enter a noun: ")
    
        print("This weekend I am going camping with" , sillyname1 + " I packed my lantern, sleeping bag, and", noun1 + " I am so", adjectivefeeling1 + "to",  verb1 +  "in a tent. I am", adjectivefeeling2 + "we might see a", animal1 + ", they are kind of dangerous. We are going to hike, fish, and", verb2 + "I have heard that the", color1 + "lake is great for", verb3 + ". Then we will", adverb1 + "hike through the forest for", number1 + ". If I see a", adjective2 + animal2 + "while hiking, I am going to bring it home as a pet! At night we will tell", sillyword1+ "stories and roast", noun2 + "around the campfire!!")
           
    elif max_storyranking == storyranking[1]:
        alphabet1 = input("Enter a letter of the alphabet: ")
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter an adjective: ")
        noun2 = input("Enter a noun: ")
        noun3 = input("Enter a noun: ")
        adjective3 = input("Enter an adjective: ")
        occupation1 = input("Enter an occupation: ")
        bodypart1 = input("Enter a body part: ")
        adjective4 = input("Enter an adjective: ")
        noun4 = input("Enter a noun: ")
        sillyname1 = input("Enter a silly name: ")
        noun5 = input("Enter the plural form of a noun: ")
        noun6 = input("Enter a noun: ")
        adjective5 = input("Enter an adjective: ")
        adverb1 = input("Enter an adverb: ")
        noun7 = input("Enter a noun: ")
          
        print("Do you want straight", alphabet1 + " on your report card? Do you want to bring home comments like “excellent” and “", adjective1 + "” on all your tests and", noun1 + "? Follow our",  adjective2 + "-fire guide to becoming the teacher’s", noun2 + " and you’ll be at the top of the", noun3 + " in no time! Tell your teacher every day that she looks", adjective3 + ". Everyone loves compliments, even", occupation1 + "! Raise your", bodypart1 + " to answer questions or volunteer for",  adjective4 + "duties, like erasing the", noun4 + "-board or walking", sillyname1 + " to the bathroom. Do extra credit whenever possible. If you have to do a report on the", noun5 + " of Liberty, build one out of Popsicle sticks and", noun6 + " too! Stay after class to help out with", adjective5 + " chores around the classroom. Use the extra time with your teacher to butter her up—she’ll think", adverb1 + "of you next time she grades one of your", noun7 + "!")

    elif max_storyranking == storyranking[2]:
        #How to make a PBJ is selected
        color1= input("Enter a verb color: ")
        noun1= input("Enter a noun/object: ")
        sillyword1= input("Enter an silly word: ")
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter an adjective: ")
        number1 = input("Enter a verb ending in 'ing': ")
        noun2 = input("Enter a noun: ")
        verb1 = input("Enter a verb: ")
        verb2 = input("Enter a verb: ")
        noun3 = input("Enter a noun: ")
  
        print("Select the type of bread you want to use. Many prefer the taste of", color1 + " bread, while others prefer", noun1 + " bread because it is healthy. Then, choose the flavor of Jam/Jelly. I personally prefer", sillyword1 + " jam, but you can use whatever you want. Next, choose the type of peanut butter–either", adjective1 + " or", adjective2 + " . Take out", number1 + " slice(s) of bread and use a", noun2 + " to", verb1 + " the jam all over one of the pieces of bread. Now", verb2 + " the peanut butter on the other piece of bread. Put them together, and you have a PB&J", noun3 ) 
    
    elif max_storyranking ==  storyranking[3]:
        noun1 = input("Enter a noun that is object: ")
        adjective1 = input("Enter an adjective: ")
        noun2 = input("Enter a noun of a city: ")
        adjective2= input("Enter an adjective of a feeling: ")
        occupation1= input("Enter an occupation: ")
        adjective3 = input("Enter an adjective: ")
        animal1 = input("Enter an animal: ")
        adjective4 = input("Enter an adjective: ")
        noun3 = input("Enter a noun: ")
        number1 = input("Enter a number: ")
        verb1 = input("Enter a verb ending in ´ing´: ")
        adjective5 = input("Enter an adjective: ")
        adjective6 = input("Enter an adjective: ")
        noun4 = input("Enter a noun: ")
        verb2 = input("Enter a verb: ")
        verb3 = input("Enter a verb ending in ´ed: ")
            
        print("Jenny Kowalski looked at the warped" , noun1 + " in her hands and felt angry. She walked over to the window and reflected on her" , adjective1 + " surroundings. She had always loved picturesque", noun2 + " with its calm, cloudy cliffs. It was a place that encouraged her tendency to feel", adjective2 + " . Then she saw something in the distance, or rather someone. It was the figure of Harry Blacksmith. Harry was a lovable, handsome", occupation1 + " . Jenny gulped. She glanced at her own reflection. Her friends saw her as a", adjective3 + " weirdo. The wind blew like rampaging", animal1 +  ", making Jenny anxious. As Jenny stepped outside and Harry came closer, she could see the", adjective4 + " smile on his face. ´I am here because I want´", noun3 + " ´, Harry bellowed, in a patient tone. He slammed his fist against Jenny's chest, with the force of", number1 + " .I", verb1 + "  love you, Jenny Kowalski. Jenny looked back, even more anxious. ´Harry, get out of my house,´ she replied. They looked at each other with", adjective5 + " feelings like two", adjective6 + noun4 + ". Suddenly, Harry lunged forward and tried to", verb2 + " Jenny in the face. She", verb3 + " Jenny Kowalski went back inside and made herself a nice glass of port.")
        
    elif max_storyranking ==  storyranking[4]:
        #The Short Story is selected
        noun1 = input("Enter a plural noun ")
        occupation1 = input("Enter an occupation: ")
        animals1 = input("Enter an animal, plural: ")
        city1 = input("Enter a city: ")
        verb1 = input("Enter a verb: ")
        noun2 = input("Enter a noun: ")
          
        print("In the book War of the", noun1 + " , the main character is an anonymous", occupation1 + " who records the arrival of", animals1 + " in", city1 + " . Needless to say, havoc reigns as the", animals1 + " continue to", verb1 + " everything in sight, until they are killed by the common", noun2)
      
    elif max_storyranking ==  storyranking[5]:
        #Weird Day is selected
        noun = input("Enter a noun: ")
        famous = input("Enter a famous person: ")
        nounplur = input("Enter a plural noun: ")
        noun2 = input("Enter a noun: ")
        adjective1 = input("Enter an adjective: ")
        verbing = input("Enter a verb ending in ing: ")
        adjective2 = input("Enter an adjective: ")
        song = input("Enter a song name: ")
        adjective3 = input("Enter an adjective: ")
        verbed = input("Enter a verb in the past tense: ")
        adjective4 = input("Enter an adjective: ")
        verbing2 = input("Enter a verb ending in ing: ")
        supermodel = input ("Enter a supermodel: ")
        place = input("Enter a place: ")
        
        print("Once upon a time there was a" , noun + ". It had" , adjective1 + " ",  nounplur + "! One day it met " , famous + "on the side of the" , place + " they were" , verbing + ". It was very" , adjective2 + "; they both looked like hobos! All of the sudden they started singing" , song + " really loudly. They ", verbed + " really ", adjective3 + "! ", famous + " started", verbing2 + " with" , supermodel + ". They looked really" , adjective4 + "!")
          
    elif max_storyranking ==  storyranking[6]:
        #The Fun Park is selected
        adjective = input("Enter an adjective: ")
        plurnoun = input("Enter a plural noun: ")
        adjective2 = input("Enter an adjective: ")
        noun = input("Enter a noun: ")
        adverb = input("Enter an adverb: ")
        number = input("Enter a number: ")
        verbpast = input("Enter a past-tense verb: ")
        adjest = input("Enter an adjective with an est ending: ")
        verbpast2 = input("Enter a past-tense verb: ")
        adverb2 = input("Enter an adverb: ")
        adjective3 = input("Enter an adjective: ")
          
        print("Today, my fabulous camp group went to a (an)" , adjective + " amusement park. It was a fun park with lots of cool" , plurnoun + " and enjoyable play structures. When we got there, my kind counselor shouted loudly, 'Everybody off the" , noun + "!' We all pushed out in a terrible hurry. My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn't figure out what exciting thing to do first. I saw a scary roller coaster I really liked so, I" , adverb + " ran over to get in the long line that had about" , number + " people in it. When I finally got on the roller coaster I was" , verbpast + ". In fact I was so nervous my two knees were knocking together. This was the" , adjest + " ride I had ever been on! In about two minutes I heard the crank and grinding of the gears. That’s when the ride began! When I got to the bottom, I was a little" , verbpast2 + " but I was proud of myself. The rest of the day went" , adverb2 + ". It was a(n)" , adjective3 + " day at the fun park.") 
      
    elif max_storyranking ==  storyranking[7]:
        print("get cringe")
          
    elif max_storyranking ==  storyranking[8]:
        #A friendly call is selected
        verb1 = input("Enter a verb ending: ")
        adjective1 = input("Enter an adjective: ")
        verb2 = input("Enter a verb: ")
        bodypart = input("Enter a body part: ")
        adverb = input("Enter an adverb: ")
        noun1 = input("Enter a noun: ")
        verb3 = input("Enter a verb: ")
        animal = input("Enter an animal: ")
        noun2 = input("Enter a noun: ")
        verb4 = input("Enter a verb: ")
        adjective2 = input("Enter an adjective: ")
        color = input("Enter an color: ")
          
        print("Once a day I call my friend to", verb1 + " them. I do it so they know how", adjective1 + " they are. Unfortunately they never", verb2 + " though, so instead i start brushing my ", bodypart + ". Considering I have a/an" , adverb + " thin", bodypart + ", when I call my friend, they always tell me to buy a", noun1 + " to", verb3 + " my problems. I therefore call my", animal + "and tell them to get me a", noun2 + " in order to", verb4 + ". Finally, when I hang up the very", adjective2 + " call, I only see" , color + ".")
                             
    elif max_storyranking ==  storyranking[9]:
        #Last day of work story
        verb1 = input("Enter a verb: ")
        adjective1 = input("Enter an adjective: ")
        verb2 = input("Enter a verb: ")
        adverb = input("Enter an adverb: ")
        verb3 = input("Enter a verb: ")
        adjective2 = input("Enter an adjective: ")
        bodypart = input("Enter a body part: ")
        color = input("Enter a color: ")
        verbing = input("Enter a verb ending in ing: ")
        bodypart2 = input("Enter a body part: ")
        noun2 = input("Enter a noun: ")
        animal = input("Enter an animal: ")
        noun3 = input("Enter a noun: ")  
          
        print("On my last day of work I really enjoy to " + verb1 + " with my " + adjective1 + " coworker. We start off by " + verbing + ", before eating. When I eat too much, however, my " + bodypart +" starts to hurt. It " + adverb + " hurts… it hurts so much that even my " + bodypart2 + " starts aching. It almost makes me not want to keep going. But then I think that its my last day at work and so I buy " + noun3 + " for everybody instead. Once the " + noun3 + " is bought, everyone can " + verb3 + " together. Stacy even brought her " + animal + " “Rocky” again. It only takes 10 minutes until “Rocky” chews off the " + noun2 + " though, which makes the last day at work even more entertaining. I "+ verb2 + " when this happens. I think that I will really miss this place, especially during the " + adjective2 + " evenings, where you can see the beautiful " + color + " sunset from the office terrace.") 
        
    elif max_storyranking ==  storyranking[10]:
        #The Worst Haircut is selected
        noun1 = input("Enter an Noun: ")
        noun2 = input("Enter a Noun: ")
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter an adjective: ")
        exclamation1 = input("Enter an exclamation: ")
         
        print("Argh! I just had the absolutely worst day at the barber. First, I was running late for my 4:00pm appointment because a", noun1 + " got hit by a", noun2 + " on the freeway, causing major traffic. Then, when I finally arrive at the shop, I find my slot has been taken by some", adjective1 + " man. ´Um excuse me?´ I said, ´You’re in my spot´. The man looked up at me with", adjective2 + " eyes, and drawled ´I was here first. Wait your turn.´ Fuming, I turned to the barber: ", exclamation1 + " ! ")
              
    elif max_storyranking ==  storyranking[11]:
        #the stranger is selected
        
        verb1 = input("Enter a verb ending in 'ing': ")
        exclamation = input("Enter an exclamation: ")
        adjective1 = input("Enter an adjective: ")
        sillyword1 = input("Enter a silly word: ")
        noun1 = input("Enter a noun: ")
        verb2 = input("Enter a verb ending in 'ing': ")
        noun2 = input("Enter a noun: ")
        adjective2 = input("Enter an adjective: ")
        number1 = input("Enter a number: ")
        adverb1 = input("Enter an adverb: ")
        adjective3 = input("Enter an adjective: ")
        adjective4 = input("Enter an adjective: ")
        room = input("Enter a type of room: ")   
          
        print("I was busy", verb1 + " in my living room on a rainy afternoon when I heard a knock on my door." , exclamation + "! I shouted, and ran to quickly open the door. There, at my doorstep stood a disturbingly" , adjective1 + " individual. “Hello,” he said with a sweeping bow. “My name is Mr.", sillyword1 + ". I received a call that there was a" , noun1 + " spotted near this location. I work for the department of", noun1 + " and have been tasked with", verb2 + " every", noun1 + " I can find. May I come in?” “Well of course!” I replied, “But I can assure you I haven't seen a", noun1 + " in quite some time. May I get you a cup of melted" , noun2 + "?” “If it’s no trouble,” the man said while eyeing me suspiciously. “You have quite the" , adjective2 + " house, I’m sure you could fit at least" , number1 + " " , noun1 + "s in here.” Sweat started to drip from my forehead. “I’m sure I don’t know what you mean.” Hands shaking, I carefully poured the man his hot cup of melted" , noun2 + ". The man sipped his cup" , adverb1 + ". “Mmmm, that’s", adjective3 + ". Well if you do spot any", noun1 + "s, don’t hesitate to give me a call.” With a fluid motion, he produced a card from his coat. Relieved, I took his card and escorted him out. “Have a" , adjective4 + " day!” I called after him. That was a close one, I thought to myself as I went to my hidden" , room + " to check on my secret" , noun1 + ".")
    
    elif max_storyranking ==  storyranking[12]:
        #The Island Nation” is selected
        sillyword1 = input("Enter a silly word: ")
        country1 = input("Enter a country: ")
        animals = input("Enter an animal (plural): ")
        number = input("Enter a number: ")
        country2 = input("Enter a country: ")
        adjective1 = input("Enter aan adjective: ")
        nounplur = input("Enter a plural noun: ")
        verbing = input("Enter a verb ending in ing: ")
        adjective2 = input("Enter an adjective: ")
        sillyword2 = input("Enter a silly word: ")
        noun = input("Enter a noun: ")
        verbing2 = input("Enter a verb ending in ing: ")
        animals2 = input("Enter an animal (plural): ")
        adjective3 = input("Enter aan adjective: ")
        noun2 = input("Enter a noun: ")
        adjective4 = input("Enter aan adjective: ")
        
        print("Located just off the coast of " , country1 + " is the small island nation of " , sillyword1 + ". Though it remains an obscure place to most, with a population of barely " + number + " the island boasts a " + adjective1 + " culture and " + adjective2 + " history. The island’s history has its roots in the legacy of colonization, and its subsequent war for independence from" , country2 + ". Since then, the island has been ruled by a " + adjective2 + " dictatorship reviled throughout the international community for its arsenal of deadly " + nounplur + ". Despite this, the people of " + sillyword1 + " live relatively " + adjective3 + " lives. Every year residents gather on the beach to celebrate their independence day by " + verbing + " until they collapse from exhaustion. Aside from independence day, the most celebrated holiday in " + sillyword1 + " is the Festival of " + sillyword2 + ", where locals dress up as " + animals + "and perform a " + adjective4 + " display of " + verbing2 + ". Tourism makes up a large part of the " + sillyword1 + " economy, but I must warn you, should you decide to visit, make sure to pack a " + noun2 + " in your bag. The island has extremely aggressive " + animals2 + " that have been known to attack tourists on sight, so make sure to keep your " + noun2 + " with you at all times!") 
            
    elif max_storyranking ==  storyranking[13]:
        #homework excuses
        adjective1 = input("Enter an adjective: ")
        noun1 = input("Enter the plural form of a noun: ")
        adjective2 = input("Enter an adjective: ")
        sillyword1 = input("Enter a silly word: ")
        noun2 = input("Enter a noun: ")
        animal1 = input("Enter an animal: ")
        verb1 = input("Enter a verb in the past tense: ")
        occupation1 = input("Enter an occupation: ")
        adjective3 = input("Enter an adjective: ")
        adjective4 = input("Enter an adjective: ")
        noun3 = input("Enter the plural form of a noun: ")
        noun4 = input("Enter a noun: ")
        noun5 = input("Enter a noun: ")
        number1 = input("Enter a number: ")
        sillyword2 = input("Enter a silly word: ")
          
        print("As a teacher, I hear a lot of", adjective1 + " excuses about why my", noun1 + " don’t turn in their homework. Here are the top most", adjective2 + " ones of all time. An alien from Planet", sillyword1 + " landed in my backyard, and when my", noun2 + " asked me to take out the garbage, I got sucked up into the", noun3 +"-ship! My pet", animal1 + " ate it, then", verb1 + " it up, then ate it again! I’m running for", occupation1 + "of the United States, and I had to work on my", adjective3 + " campaign speech. On the way home from school, a band of", adjective4 + "pirates looking for gold", noun3 + "insisted I turn over my backpack—or walk the", noun4 + "! I was too busy breaking the world record for most", noun5 + "eaten in", number1 + "minutes while balancing on one", sillyword2 + ".")
          
    elif max_storyranking ==  storyranking[14]:
        #Family vacation is selected
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter an adjective: ")
        noun1 = input("Enter a noun: ")
        noun2 = input("Enter a noun: ")
        noun3 = input("Enter the plural form of a noun: ")
        noun4 = input("Enter a noun: ")
        noun5 = input("Enter the plural form of a noun: ")
        verb1 = input("Enter a verb ending in ‘ing’: ")
        verb2 = input("Enter a verb ending in ‘ing’: ")
        noun6 = input("Enter the plural form of a noun: ")
        verb3 = input("Enter a verb ending in ‘ing’: ")
        noun7 = input("Enter a noun: ")
        noun8 = input("Enter a noun: ")
        bodypart1 = input("Enter a body part: ")
        noun9 = input("Enter a place: ")
        verb4 = input("Enter a verb ending in ‘ing’: ")
        adjective3 = input("Enter an adjective: ")
        number1 = input("Enter a number: ")
        noun10 = input("Enter the plural form of a noun: ")
        
        print("A vacation is when you take a trip to some", adjective1 + " place with your", adjective2 + " family. Usually you go to some place that is near a/an", noun1 + " or up on a/an", noun2 + ". A good vacation place is one where you can ride", noun3 + " or play", noun4 + " or go hunting for", noun5 + ". I like to spend my time", verb1 + " or", verb2 + ". When parents go on a vacation, they spend their time eating three", noun6 + " a day, and fathers play golf, and mothers sit around", verb3 + ". Last summer, my little brother fell in a/an", noun7 + " and got poison", noun8 + "all over his", bodypart1 + ". My family is going to go to the", noun9 + " and I will practice", verb4 + ". Parents need vacations more than kids because parents are always very", adjective3 + " and because they have to work", number1 + " hours every day all year making enough", noun10 + " to pay for the vacation.")
    
    elif max_storyranking ==  storyranking[15]:
        #Weekend is selected
        adverb1 = input("Enter an adverb: ")
        noun1 = input("Enter a place: ")
        noun2 = input("Enter the plural form of a noun: ")
        verb1 = input("Enter a verb ending in 'ing': ")
        verb2 = input("Enter a verb ending in 'ing: ")
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter an adjective: ")
        bodypart1 = input("Enter a bodypart: ")
        noun3 = input("Enter a noun in the plural form: ")
        adjective3 = input("Enter an adjective: ")
        verb3 = input("Enter a verb: ")
        noun4 = input("Enter the plural form of a noun: ")
        adjective4 = input("Enter an adjective: ")
        sillyword1 = input("Enter a silly word: ")
        noun5 = input("Enter a noun: ")
        sillyname1 =input("Enter a silly name: ")
        
        print("Ahhh, it is", adverb1 + " Saturday! That means I don’t have to go to", noun1 + "and teach my", noun2 + " all about adding and", verb1 + ". I should probably spend some time", verb2 + "at my second job as a/an", adjective1+  ", undercover-detective superhero! First, let me find my", adjective2 + "cape and", bodypart1 + "-high boots. I wouldn’t want any of my", noun3 + "to know my true", adjective3 + " identity! Now that I’m dressed, I’ll listen in on my walkie-", verb3 + "-ie to see if there are any", noun4 + "in distress or anyone who needs my", adjective4 + " assistance.", sillyword1 + "! A/An", noun5 + "stuck in a tree! That sounds like a job for Mrs.", sillyname1 + ", super teacher and superhero!")
    
    elif max_storyranking ==  storyranking[16]:
        #sonic story is selected
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter an adjective: ")
        noun1 = input("Enter a noun: ")
        noun2 = input("Enter a noun: ")
        adjective3 = input("Enter a adjective: ")
        noun3 = input("Enter a noun: ")
        noun4 = input("Enter a noun in the plural form: ")
        adjective4 = input("Enter an adjective: ")
        number1 = input("Enter a number: ")
        adjective5 = input("Enter an adverb: ")
        sillyname1 = input("Enter a silly name: ")
        noun5 = input("Enter a noun in plural form: ")
        adjective6 = input("Enter an adjective: ")
        noun6 = input("Enter a noun that is a place: ")
        noun7 = input("Enter a noun in the plural form: ")
        verb1 = input("Enter a verb: ")
          
        print("Sonic’s abode is a very", adjective1 + " place. At first glance, it seems like a/an", adjective2 + " cave, but if you look closer, you’ll see it’s actually a comfortable", noun1 + ". For one, Sonic has a super-cozy bean bag", noun2 + ". When he feels like listening to some", adjective3 + " tunes from the 1980s, Sonic turns on his old-school", noun3 + " pulls out his collection of", noun4 + " and jams out. In addition to great tunes, Sonic has plenty of", adjective4 + " equipment to keep him busy. There’s a dryer that Sonic uses as a treadmill to run", number1 + " miles a day. He has a/an", adjective5 + " ping pong table where he plays against", sillyname1 + ". And for that final touch, Sonic hung", noun5 + " all over his cave walls. He’s got a/an", adjective6 + " photo of the", noun6 + " next to a poster of", noun7 + ". It may not be much, but Sonic loves to", verb1 + " in his cave all the time.")
         
    else:
        #Summertime story is chosen
        sillyword1 = input("Enter a silly word: ")
        noun1 = input("Enter the plural form of a noun: ")
        noun2 = input("Enter a city: ")
        verb1 = input("Enter a verb in the past tense: ")
        sillyword2 = input("Enter a silly word: ")
        verb2 = input("Enter a verb: ")
        noun3 = input("Enter the plural form of a noun: ")
        verb3 = input("Enter a verb in the past tense: ")
        noun4 = input("Enter the plural form of a noun: ")
        verb4 = input("Enter a verb in the past tense: ")
        language1 = input("Enter a language: ")
        sillyword3 = input("Enter a silly word: ")
        bodypart1 = input("Enter a body part: ")
          
        print("It was the summer of", sillyword1 + " songs. We danced in", noun1 + " all over downtown", noun2 + " until 4 a.m. and", verb1 + sillyword2 + " for six hours in the daytime. I liked that he could ", verb2 + "all the", noun3 + ". He was in a class ahead of me. He", verb3 + noun4 + ", so I did too. It was six weeks of summer. I don’t know how I", verb4 + ". I almost got the ", language1 + "word for", sillyword3 + " tattooed on my", bodypart1 + "when I returned home. But I didn’t. It was enough that I had lived.")
              

              
if __name__ =="__main__":
    main()