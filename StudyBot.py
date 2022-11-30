import random

# Progress: 80.0%

# COMPLETION CHECKLIST (4/5):
# Systems: FULLY FUNCTIONAL
#   * type problems here if they exist
# Math: (4/4) DONE
# Science: (4/4) DONE
# Geography (0/4)

greetings = ["Hello!", "Heyo!", "What's Up?", "Good to see you!", "Back Already?"]
goodbyes = ["Okay, see ya!", "Okay, come back soon!", "Okay, bye!", "Alright, see you around!"]

subjKeys = ["math", "science", "geography"]
subjCorrResponses = ["Good choice! I love %s!", "Okay, I'll get some %s questions ready!",
                        "Sounds good! %s is fun!", "I can do that! I'm pretty handy with %s.", 
                        "%s it is!", "%s is one of my favorites!", "Cool! %s questions are the best!",
                        "Okay! Get ready for some %s questions!", "Nice, I'll prepare some %s questions for you!",
                        "ERROR: 19738 files corrupted. Immediate reboot requir- \nJust kidding. %s coming up.",
                        "%s? Sounds good to me!"]

subjIncorrResponses = ["Uhh... what's that?", "Well this is awkward.", "Oof, don't have that one in my database.",
                        "Ugh, I should have been programmed better.", "That one might be a little out of my league.",
                        "I'm not familiar with that one.", "Hold on, let me check for that one... nope.",
                        "Oh, I wasn't expecting that one.", "I know I'm an AI and all but I'm not THAT good.",
                        "Maybe we can give that one a shot some other time.", "Okay, I hear you, but no.",
                        "I don't think I'm built for that.", "Maybe it's time for an update."]

AnsCorrResponses = ["Great Job!", "Nice one!", "That's it!", "Correct!", "Good Job!", "Amazing!",
                     "Awesome!", "That's correct!", "That's right!", "Right-on!", "Good Answer!"]

AnsIncorrResponses = ["Ooh, so close!", "Almost!", "Not quite!", "A fair attempt. Incorrect, but fair.",
                    "Correct! \nJust kidding. That's not it, silly.", "Yikes.", "Not this time."]

# math initialization
mathSubjKeys = ["addition", "subtraction", "multiplication", "division"]
mathQuestions = ["%d + %d ?", "%d - %d ?", "%d x %d ?", "%d / %d ?"]

# science initialization
scienceSubjKeys = ["space science", "biology", "anatomy", "chemistry"]

spaceQuestions = ["Who said the famous line: That's one small step for man, one giant leap for mankind.?", "What is the name of our galaxy?",
                "Which planet is closest to the sun?", "Which non-dwarf planet is farthest from the sun?",
                "What's the fifth planet from the sun?", "TRUE/FALSE: It is possible for a planet to have more than one moon.",
                'TRUE/FALSE: The first lifeform to fully orbit Earth was a dog named "Laika".', 
                "TRUE/FALSE: Every planet in our solar system orbits the sun.", "TRUE/FALSE: Space is entirely empty, with no molecules existing whatsoever.",
                "TRUE/FALSE: Mars is closer to the sun than Earth.", "TRUE/FALSE: Venus is the largest planet in our solar system.",
                "The rockets which propelled the Apollo 11 spacecraft were named after which planet?", 
                'The "Space Race" refers to a race between the U.S.A. and the Soviet Union to get to the..?',
                "Which dwarf planet was previously considered an official planet until recently?", 
                "What is the largest space organization in the world?"]
spaceAnswers = ["neil armstrong", "milky way", "mercury", "neptune", "jupiter", "true", "true", "true", "false", "false",
                "false", "saturn", "moon", "pluto", "nasa"]

bioQuestions = ["What is referred to as the most basic structure of life?",
                "What is the study of heredity and genes referred to as?", "A (blank) square can be used to determine the liklihood of inherited genetics.",
                "Where is DNA found inside a cell?", "What does DNA stand for?", 
                "What is the process that plants and other organisms use to convert light energy into food?",
                "A (blank) is described as any organic, living system composed of cells which can react and reproduce.",
                "A (blank) models how energy is transferred between organisms.", "Which famous scientist proposed The Theory of Evolution?",
                "Botany is the study of...", "Who discovered penicilin?", "TRUE/FALSE: Cell walls are found only in animal cells.",
                "When DNA changes and results in a new characteristic, it has gone under a...", 
                "What term refers to animals that only eat plants?", "What term refers to animals that only eat other animals?", 
                "What term refers to animals that eat both plants and animals?"]
bioAnswers = ["cell", "genetics", "punnett", "nucleus", "deoxyribonucleic acid", "photosynthesis", "organism", 
            "food chain", "charles darwin", "plant", "alexander fleming", "false", "mutation", "herbivore", "carnivore",
            "omnivore"]

anatQuestions = ["How many chambers does the human heart have? (use numerical form)", "What is the largest organ in the human body?",
                'The (blank) is also commonly referred to as the "voice box"', "What is the name of the bone strcture that makes up the spinal column?",
                "What is the biggest part of the human brain?", "What is the largest artery in the human body?",
                "TRUE/FALSE: Veins carry blood TO the heart, while arteries carry blood AWAY from the heart.",
                "The structural protein (blank) can be found in your hair and nails.", "How many bones make up the human body?",
                "Which internal organ is capable of regenerating itself?", "What large, long bone can be found in the upper leg?",
                '"What is the long tube also commonly referred to as the "windpipe"?', "Cells found exclusively in the nervous system are called...",
                "What is the top layer of the skin called?", "The cervix is a structure connecting the vagina and..."]
anatAnswers = ["4", "skin", "larynx", "vertebrae", "cerebrum", "aorta", "true", "keratin", "206", "liver", "femur", "trachea",
            "neuron", "epidermis", "uterus"]

chemQuestions = ["Which subatomic particle with a positive charge is located within the nucleus of the atom?", 
                "The (blank) is the smallest unit of matter.", "In which form of bonding are electtons transferred?",
                "Which element has an atomic number of 6?", "Any substance with a pH rating below 7 is considered a(n)...",
                "Any substance with a pH rating above 7 is considered a(n)...", "Water is comprised of 1 oxygen molecule and 2 (blank) molecules.",
                "If a molecule possesses an uneven distribution of electrons, it is considered...",
                "Groups 4 through 12 of the periodic table represent the (blank) metals.", "Group 17 of the periodic table represents the (blank).",
                "Group 1 (excluding Hydrogen) of the periodic table represents the (blank).", "Which element has an atomic number of 8?", 
                "Which element has an atomic number of 1?", "Which element has an atomic number of 9?", "Which element has the atomic symbol 'S'?", 
                "Which element has the atomic symbol 'K'?", "Which element has the atomic symbol 'Ag'?","Which element has the atomic symbol 'Zn'?", 
                "Which element has the atomic symbol 'I'?"]
chemAnswers = ["proton", "atom", "ionic", "carbon", "acid", "base", "hydrogen", "polar", "transition", "halogen", "alkali metals", "oxygen", "hydrogen", 
                "fluorine", "sulfur", "potassium", "silver", "zinc", "iodine", ]

# geography inialization
geoSubjKeys = ["states", "countries", "continents"]

statesQuestions = ["What is the capital of Alaska?", "What popular tourist attraction lies in South Dakota?",
                "Which state features a picture of a bear on its flag?", "Raleigh is the capital of which state?", 
                "What is the 50th state?", "What Ivy League school is located in Connecticut?", "What is the capital of New York?",
                "What is the capital of Texas?", "What is the largest U.S. state in terms of land area?", "Which state borders 4 of the 5 Great Lakes?"]
statesAnswers = ["juneau", "rushmore", "california", "north carolina", "hawai", "yale", "albany", "austin", "alaska", "michigan"]

countryQuestions = ["What country has the longest coastline in the world?", "What country features a unicorn as its national animal?",
                "Beirut is the capital of which country?", "What country has the largest population as of 2022?",
                "Which country has the largest population in Africa?", "What is the largest country in the world in terms of land area?",
                "Which country held the first modern Olympic Games?", "What country is named after the equator?", 
                "What country is home to the famous Mt. Everest?", "Which country is also officially recognized as a continent?"]
countryAnswers = ["canada", "scotland", "lebanon", "china", "nigeria", "russia", "greece", "equador", "nepal", "australia"]

contQuestions = ["What is the least populated continent?", "What is the most populated continent?", "Which continent has the most countries?",
                "Which continent speaks the most languages?", "Beavers are native to which continent?", "Which continent is considered the wealthiest?",
                "What is the smallest continent in size?", "What is the largest continent in size?", 
                "Which continent is home to both the highest and lowest points on Earth?", "Which continent is home to the most species?"]
contAnswers = ["antartica", "asia", "africa", "asia", "north america", "europe", "australia", "asia", "asia", "australia"]

mathSubMenu = 0
sciSubMenu = 0
hisSubMenu = 0
engSubMenu = 0

keyFound = False
mainMenu = 0
menu2 = 0
subject = ''
streak = 0
corr = 0
incorr = 0
run = 0

def questionBody(answer, streak, corr, incorr): # function which displays the body for every question
    global trueCase
    trueCase = 0
    print("StudyBot: "+ q)
    print("")
    userInput = input("You:      ")
    print("")
    lowInput = str(userInput.lower())
    if answer in lowInput: # if the user inputs the expected answer 
        print("StudyBot: "+ random.choice(AnsCorrResponses))
        if streak >= 3:
            print("StudyBot: Keep it up! You're on a streak of ",streak,"!")
        trueCase += 1
        return True
    elif lowInput == 'done': # if the user inputs 'done'
        corrPercent = 0
        total = incorr + corr
        if total != 0:
            corrPercent = corr / total
            corrPercent = float("%.2f" % corrPercent)
            corrPercent = f"{corrPercent:.0%}"
        print("StudyBot: Great Session!")
        print("          This time, you had",corr,"correct answers and",incorr,"incorrect answers.")
        print("          You got",corrPercent,"of your questions correct!")
        return False
    else: # if the user inputs an unexpected answer
        print("StudyBot: "+ random.choice(AnsIncorrResponses))
        trueCase = 0
        return True

while mainMenu == 0: # loop which acts as a "main menu" to come back to when the user requests it. These "menus" appear frequently.
    mainMenu += 1  # immediately increments the main menu loop so that the function won't repeat automatically.
    print("")
    if run == 0:
        print("StudyBot: "+ random.choice(greetings)) # selects a random response from the "greetings" array.
    print("          If you're ready to study, let me know which subject you'd like to practice!")
    print("          Whenever you're ready to leave, just say 'exit'!")

    print("")
    userInput = input("You:      ") # takes the user's input
    lowInput = userInput.lower() # converts userInput to all lowercase, so that capitalization on the user's end won't matter.
    print("")

    if lowInput == "exit": # if the desired keyword (exit, in this case) is found anywhere within lowInput, block will run
        print("StudyBot: "+ random.choice(goodbyes))
        break
    while menu2 == 0: # another menu
        keyFound = False 
        trueChecker = 0
        for i in range(len(subjKeys)): # searhes lowInput for any currently implemented subjects.
            if subjKeys[i] in lowInput: 
                subject = subjKeys[i]
                print("StudyBot: "+ random.choice(subjCorrResponses) %subjKeys[i].capitalize())
                keyFound = True
                menu2 += 1
        
        if keyFound == False: # if a subject wasn't found in the user's input
            print("StudyBot: "+ random.choice(subjIncorrResponses))
            print("          Right now, I'm only familiar with:")
            print("          ", end = '')
            for i in range(len(subjKeys)): # prints a list of all currently implemented subjects
                if i == len(subjKeys)-1:
                    print("and",subjKeys[i].capitalize(), end = '.')
                else:
                    print(subjKeys[i].capitalize(), end = ', ')
            print("\n          Maybe we could try one of those instead?")
            print("")
            userInput = input("You:      ") # collects user input (This happens a lot)
            lowInput = userInput.lower() # lowercase user input. (This happens every time input is collected)
            print("")

    if keyFound == True: # if a subject keyword is found in lowInput
        questionLoop = 0
        print("          Remember, If you want to practice a different subject, just say 'done'!")
        print("")
        while questionLoop == 0: # another menu
            questionLoop+=1

# math ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if subject == "math":
                print("StudyBot: Which subject would you like to practice?")
                print("          ", end = '')
                for i in range(len(mathSubjKeys)): # lists all currently implemented subjects within "math"
                    if i == len(mathSubjKeys)-1:
                        print(mathSubjKeys[i].capitalize(), end = ', or try them all together?')
                    else:
                        print(mathSubjKeys[i].capitalize(), end = ', ')
                print("\n")
                userInput = input("You:      ")
                mathSubInput = userInput.lower()
                print("")
                mathSubMenu = 0
                while mathSubMenu == 0: # another menu
                    if 'addition' in mathSubInput: # addition case
                        q = mathQuestions[0]
                        i = 0
                        mathSubMenu += 1
                        n = random.randint(0,32) # selects random numbers for use between 0 and 32, inclusive.
                        n1 = random.randint(0,32)
                        answer = str(n + n1) # answer initialization
                        q = q %(n, n1) # question initialization
                    elif 'subtraction' in mathSubInput: # subtraction case
                        q = mathQuestions[1]
                        i = 0
                        mathSubMenu += 1
                        n = random.randint(1,32) # selects random numbers for use between 1 and 32, inclusive.
                        n1 = random.randint(0,n)
                        answer = str(n - n1) # answer initialization
                        q = q %(n, n1) # question initialization
                    elif 'multiplication' in mathSubInput: # mult. case
                        q = mathQuestions[2]
                        i = 0
                        mathSubMenu += 1
                        n = random.randint(0,12) # selects random numbers for use between 0 and 12, inclusive.
                        n1 = random.randint(0,12)
                        answer = str(n * n1) # answer initialization
                        q = q %(n, n1) # question initialization
                    elif 'division' in mathSubInput: # division case
                        q = mathQuestions[3]
                        i = 0
                        mathSubMenu += 1
                        divisor = random.randint(1,12) # selects a random number for use between 1 and 12, inclusive.
                        dividend = random.randint(divisor,divisor*12) # selects an easy dividend based on the divisor, so no decimal answers are expected
                        r = dividend % divisor
                        dividend = dividend - r
                        answer = str(int(dividend/divisor)) # answer initialization
                        q = q %(dividend, divisor) # question initialization
                    elif 'all' in mathSubInput: # case if user prefers to do random subject questions
                        q = random.choice(mathQuestions) # randomly chooses a subject within "math"
                        if q == mathQuestions[0]: # addition case, exact same stuff as what's above
                            i = 0
                            mathSubMenu += 1
                            n = random.randint(0,32)
                            n1 = random.randint(0,32)
                            answer = str(n + n1)
                            q = q %(n, n1)
                        elif q == mathQuestions[1]: # subtraction case, exact same stuff as what's above
                            i = 0
                            mathSubMenu += 1
                            n = random.randint(1,32)
                            n1 = random.randint(0,n)
                            answer = str(n - n1)
                            q = q %(n, n1)
                        elif q == mathQuestions[2]: # mult. case, exact same stuff as what's above
                            i = 0
                            mathSubMenu += 1
                            n = random.randint(0,12)
                            n1 = random.randint(0,12)
                            answer = str(n * n1)
                            q = q %(n, n1)
                        elif q == mathQuestions[3]: # division case, exact same stuff as what's above
                            i = 0
                            mathSubMenu += 1
                            divisor = random.randint(1,12)
                            dividend = random.randint(divisor,divisor*12)
                            r = dividend % divisor
                            dividend = dividend - r
                            answer = str(int(dividend/divisor))
                            q = q %(dividend, divisor)
                    else:
                        answer = "0"
                        print("StudyBot: "+ random.choice(subjIncorrResponses)) # if a subject keyword isn't found in mathSubInput
                        print("          Right now, I'm only familiar with:")
                        print("          ", end = '')
                        for i in range(len(mathSubjKeys)):
                            if i == len(mathSubjKeys)-1:
                                print("and",mathSubjKeys[i].capitalize(), end = '.')
                            else:
                                print(mathSubjKeys[i].capitalize(), end = ', ')
                        print("\n")
                        userInput = input("You:      ")
                        lowInput = userInput.lower()
                        print("")

                    if questionBody(answer, streak + 1, corr, incorr): # calls questionBody using information gathered from above
                        if trueCase > 0: # correct case
                            streak += 1
                            corr += 1
                        else: # incorrect case
                            streak = 0
                            incorr += 1
                        menu = 0
                        mathSubMenu = 0
                    else: # 'done' case
                        corr = 0 # any time you see 'x' = 0 or 'x' += 1, it's just resetting or incrementing variables important to the code
                        incorr = 0
                        streak = 0
                        run += 1
                        menu = 0
                        mainMenu = 0
                        menu2 = 0
        
    # READ: Since each subject case is essentially a copy of the same system, just with different info,
    # the following subject cases are substantially less documented than the one above. Differences between
    # them are still documented, but if you experience any kind of confusion it is recommended to check
    # the subject case above for information, seeing as all cases use the systems and syntax. 

# science ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if subject == "science":
                print("StudyBot: Which subject would you like to practice?")
                print("          ", end = '')
                for i in range(len(scienceSubjKeys)):
                    if i == len(scienceSubjKeys)-1:
                        print(scienceSubjKeys[i].capitalize(), end = ', or try them all together?')
                    else:
                        print(scienceSubjKeys[i].capitalize(), end = ', ')
                print("\n")
                userInput = input("You:      ")
                sciSubInput = userInput.lower()
                print("")
                sciSubMenu = 0
                while sciSubMenu == 0:
                    if 'space science' in sciSubInput or 'space' in sciSubInput:
                        q = random.choice(spaceQuestions) # picks a random question from the "spaceQuestions" array
                        i = 0
                        sciSubMenu += 1
                        for i in range(len(spaceQuestions)): 
                            if spaceQuestions[i] == q:
                                answer = str(spaceAnswers[i]) # selects the desired answer using spaceAnswers[i], which is located at the same position as q in spaceQuestions.
                    elif 'biology' in sciSubInput:
                        q = random.choice(bioQuestions) # picks a random question from the "bioQuestions" array
                        i = 0
                        sciSubMenu += 1
                        for i in range(len(bioQuestions)):
                            if bioQuestions[i] == q:
                                answer = str(bioAnswers[i])
                    elif 'anatomy' in sciSubInput:
                        q = random.choice(anatQuestions) # picks a random question from the "physQuestions" array
                        i = 0
                        sciSubMenu += 1
                        for i in range(len(anatQuestions)):
                            if anatQuestions[i] == q:
                                answer = str(anatAnswers[i])
                    elif 'chemistry' in sciSubInput:
                        q = random.choice(chemQuestions) # picks a random question from the "chemQuestions" array
                        i = 0
                        sciSubMenu += 1
                        for i in range(len(chemQuestions)):
                            if chemQuestions[i] == q:
                                answer = str(chemAnswers[i])
                    elif 'all' in sciSubInput: # picks a random question using all science arrays
                        q = random.choice(scienceSubjKeys)
                        if q == 'space science':
                            q = random.choice(spaceQuestions)
                            i = 0
                            sciSubMenu += 1
                            for i in range(len(spaceQuestions)): 
                                if spaceQuestions[i] == q:
                                    answer = str(spaceAnswers[i])
                        elif q == 'biology':
                            q = random.choice(bioQuestions)
                            i = 0
                            sciSubMenu += 1
                            for i in range(len(bioQuestions)): 
                                if bioQuestions[i] == q:
                                    answer = str(bioAnswers[i])
                        elif q == 'anatomy':
                            q = random.choice(anatQuestions)
                            i = 0
                            sciSubMenu += 1
                            for i in range(len(anatQuestions)): 
                                if anatQuestions[i] == q:
                                    answer = str(anatAnswers[i])
                        elif q == 'chemistry':
                            q = random.choice(chemQuestions)
                            i = 0
                            sciSubMenu += 1
                            for i in range(len(chemQuestions)): 
                                if chemQuestions[i] == q:
                                    answer = str(chemAnswers[i])
                    else:
                        answer = "0"
                        print("StudyBot: "+ random.choice(subjIncorrResponses))
                        print("          Right now, I'm only familiar with:")
                        print("          ", end = '')
                        for i in range(len(scienceSubjKeys)):
                            if i == len(scienceSubjKeys)-1:
                                print("and",scienceSubjKeys[i].capitalize(), end = '.')
                            else:
                                print(scienceSubjKeys[i].capitalize(), end = ', ')
                        print("\n")
                        userInput = input("You:      ")
                        lowInput = userInput.lower()
                        print("")
                    
                    if questionBody(answer, streak + 1, corr, incorr):
                        if trueCase > 0:
                            streak += 1
                            corr += 1
                        else:
                            streak = 0
                            incorr += 1
                        menu = 0
                        sciSubMenu = 0
                    else:
                        corr = 0
                        incorr = 0
                        streak = 0
                        run += 1
                        menu = 0
                        mainMenu = 0
                        menu2 = 0

# geography -------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if subject == "geography":
            print("StudyBot: Which subject would you like to practice?")
            print("          ", end = '')
            for i in range(len(geoSubjKeys)):
                if i == len(geoSubjKeys)-1:
                    print(geoSubjKeys[i].capitalize(), end = ', or try them all together?')
                else:
                    print(geoSubjKeys[i].capitalize(), end = ', ')
            print("\n")
            userInput = input("You:      ")
            geoSubInput = userInput.lower()
            print("")
            geoSubMenu = 0
            while geoSubMenu == 0:
                if 'state' in geoSubInput:
                    q = random.choice(statesQuestions)
                    i = 0
                    geoSubMenu += 1
                    for i in range(len(statesQuestions)): 
                        if statesQuestions[i] == q:
                            answer = str(statesAnswers[i])
                elif 'countr' in geoSubInput:
                    q = random.choice(countryQuestions)
                    i = 0
                    geoSubMenu += 1
                    for i in range(len(countryQuestions)): 
                        if countryQuestions[i] == q:
                            answer = str(countryAnswers[i])
                elif 'continent' in geoSubInput:
                    q = random.choice(contQuestions)
                    i = 0
                    geoSubMenu += 1
                    for i in range(len(contQuestions)): 
                        if contQuestions[i] == q:
                            answer = str(contAnswers[i])
                elif 'all' in geoSubInput:
                    q = random.choice(geoSubjKeys)
                    if q == 'states':
                        q = random.choice(statesQuestions)
                        i = 0
                        geoSubMenu += 1
                        for i in range(len(statesQuestions)): 
                            if statesQuestions[i] == q:
                                answer = str(statesAnswers[i])
                    elif q == 'countries':
                        q = random.choice(countryQuestions)
                        i = 0
                        geoSubMenu += 1
                        for i in range(len(countryQuestions)): 
                            if countryQuestions[i] == q:
                                answer = str(countryAnswers[i])
                    elif q == 'continents':
                        q = random.choice(contQuestions)
                        i = 0
                        geoSubMenu += 1
                        for i in range(len(contQuestions)): 
                            if contQuestions[i] == q:
                                answer = str(contAnswers[i])

                else:
                    answer = "0"
                    print("StudyBot: "+ random.choice(subjIncorrResponses))
                    print("          Right now, I'm only familiar with:")
                    print("          ", end = '')
                    for i in range(len(geoSubjKeys)):
                        if i == len(geoSubjKeys)-1:
                            print("and",geoSubjKeys[i].capitalize(), end = '.')
                        else:
                            print(geoSubjKeys[i].capitalize(), end = ', ')
                    print("\n")
                    userInput = input("You:      ")
                    lowInput = userInput.lower()
                    print("")
                
                if questionBody(answer, streak + 1, corr, incorr):
                    if trueCase > 0:
                        streak += 1
                        corr += 1
                    else:
                        streak = 0
                        incorr += 1
                    menu = 0
                    geoSubMenu = 0
                else:
                    corr = 0
                    incorr = 0
                    streak = 0
                    run += 1
                    menu = 0
                    mainMenu = 0
                    menu2 = 0