MADLIBS Project
Edoardo Snaidero; Duncan Allen; Priya Mehta

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

#Welcome to Madlibs! The most fun word game in the world (no, seriously)! 

#The purpose of this game is to have fun. We created a MadLib game in python which contains 18 different MadLibs Stories.

#Different genres have been attributed to each individual MadLibs Story.

# Each Player will be either attributed a MadLibs story based on the answers given on a series of questions that determine your mood and hence give you a story
# OR
# Each Player will be attributed a Story based on the user´s word input using SpaCy. With this option, you would be allocated a story most similar to your given word based on your mood.

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

##IMPORTANT NOTICE: It is important to use Colab for this game. There have been several problems that prevent Spacy from running smoothly on Spyder. 

#The first step is to install SpaCy by importing the package onto your preferred IDE (Please do not use Spyder)


#Once Spacy has been installed, we have our first question of the game: Does the user prefer to be given a story based on a questionnaire (enter ´1´), or does the user prefer to be given a story based off your current mood (enter ´2´).

##########################################################################################################################################

#If Player entered option ´1´, then three questions will be asked in order.
The questions are:

1) Are you in a rush? (User must answer with y/n)
2) Do you like adventures? (User must answer with y/n)
3) Do you want to learn something new? (User must answer with y/n)

#Based on the outcome of the questions (E.g: yyy , yyn , ynn , etc..), users will be asked a fourth and fifth question (based on your mood), which will allocate you a story that most similarly assimiliates your answer. 
#This way you can enjoy a MadLibs Story based on how you feel, and have more fun :) 

##########################################################################################################################################


#If the Player entered option ´2´(story allocated based on the given word that describes your mood), no further questions will be asked.
#Instead, user will need to input a word into the text field. Word can be any word describing your mood

#Once the word has been entered by the user, Spacy will then send back one of the 18 available MadLibs stories that is most similar to the word that the user input. 
#This will be done by Spacy using its Similarity function, in which similarity is determined by comparing word vectors, or multi-dimensional meaning representations of a word. 
#Spacy will therefore find the most suitable story based on the entered word, by analyzing which of the story can be considered closest to the given word. 

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################


#If you are encountering problems downloading spacy, or running the code, the user can reach out to the group members through the hertie school. Precisely, it is maintained by Priya ,Duncan or Edoardo.
#The E-Mails are:

#219484@students.hertie-school.org (Duncan Allen)
#213464@students.hertie-school.org (Priya Mehta)
#207393@students-hertie-school.org (Edoardo Snaidero)

The mentioned names are also those who maintain and contribute to the project

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################



Don´t forget to have fun!
