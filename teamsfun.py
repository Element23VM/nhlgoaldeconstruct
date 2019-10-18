import sys
sys.path.append('/weeks')

import linkage as link
import rosters as ros

y18m10, y18m9, y18m8  = link.y18wm10.pack, link.y18wm9.pack, link.y18wm8.pack
y18m7, y18m6, y18m5 = link.y18wm7.pack, link.y18wm6.pack, link.y18wm5.pack
y18m4, y18m3, y18m2 = link.y18wm4.pack, link.y18wm3.pack, link.y18wm2.pack
y18m1 = link.y18wm1.pack
y19w1, y19w2, y19w3 = link.y19w1.pack, link.y19w2.pack, link.y19w3.pack

relgamedb = {
    "y19w3" : y19w3, "y19w2" : y19w2, "y19w1" : y19w1,
    "y18m1" : y18m1, "y18m2" : y18m2, "y18m3" : y18m3, "y18m4" : y18m4,
    "y18m5" : y18m5, "y18m6" : y18m6, "y18m7" : y18m7, "y18m8" : y18m8
    }

################################FUNCTIONS###############################

def hundredBalance(first, second):

    balancer = first + second
    fperc = first/balancer

    final = 200 * fperc

    return round(final, 2)

#####ENDHUNDRED

def oneOff(reffy, newy):

    for x in reffy:
        if reffy[x] == max(reffy.values()):
            t = reffy[x]
            for y in reffy:
                if t == reffy[y]:
                    newy.setdefault(y, t)
                    return newy
#####ENDONEOFF

def sortMyListPlease(oldlist):
    ref = {}
    
    new = {}

    todelete = {}

    #old list must be duplicated, not referenced again
    for x in oldlist:
        ref.setdefault(x, oldlist[x])

    while len(new) < len(oldlist):
        new = oneOff(ref, new)
        for x in new:
            todelete.setdefault(x)
        for x in todelete:
            if x in ref:
                del ref[x]   

    return new

#####ENDSORTMYLISTPLEASE

def oneOffmin(reffy, newy):

    for x in reffy:
        if reffy[x] == min(reffy.values()):
            t = reffy[x]
            for y in reffy:
                if t == reffy[y]:
                    newy.setdefault(y, t)
                    return newy
#####ENDONEOFF

def sortMyListByMin(oldlist):
    ref = {}
    
    new = {}

    todelete = {}

    #old list must be duplicated, not referenced again
    for x in oldlist:
        ref.setdefault(x, oldlist[x])

    while len(new) < len(oldlist):
        new = oneOffmin(ref, new)
        for x in new:
            todelete.setdefault(x)
        for x in todelete:
            if x in ref:
                del ref[x]   

    return new

#####ENDSORTMYLISTPLEASE

def getShotsPerGame(system):
    
    shots = 0
    games = 0

    for x in system: ##finds the packs
        pack = system[x]
        for y in pack: ##fishing now throough games
            game = pack[y]
            for z in game: ##each game
                
                if z == "hsht":
                    shots += game[z]
                    games += 1
                if z == "asht":
                    shots += game[z]
                    games += 1
                    
    spt = round(shots/games, 2)
    return spt

#####ENDGETSHOTSPG

def getGoalieSavePAtHome(system):

    pdb = {}
    scoredQ = [
        "ag1", "ag2", "ag3", "ag4", "ag5", "ag6", "ag7", "ag8", "ag9",
        "a10", "a11", "a12"
        ]
    notme = ""

    #FIRST, Populate the list
    for x in system: ##finds the packs
        pack = system[x]
        for y in pack: ##fishing now throough games
            game = pack[y]
            for z in game: ##each game

                if z == "agli":
                    if z not in pdb:
                        pdb.setdefault(game[z], 0)

    for a in pdb:
        goals = 0
        shots = 0
        gms = 0
        for x in system: ##finds the packs
            pack = system[x]
            for y in pack: ##fishing now throough games
                game = pack[y]
                if game["hgli"] == a:
                    shots += game["hsht"]

                    for z in game:
                        gms += 1
                        for q in scoredQ:
                            if z == q:
                                if game[z] != notme:
                                    goals += 1

        if shots == 0:
            shots = 1
        if goals == 0:
            goals = 10
        avsaveper = shots/goals/100
        avsaveper = 0.995 - avsaveper
        if gms > 2:
            pdb[a] = avsaveper
        else:
            pdb[a] = 0.899

    pdb = sortMyListPlease(pdb)

    return pdb

#####ENDGOALIESAVEHOME

def getGoalieSavePAtAway(system):

    pdb = {}
    scoredQ = [
        "hg1", "hg2", "hg3", "hg4", "hg5", "hg6", "hg7", "hg8", "hg9",
        "h10", "h11", "h12"
        ]
    notme = ""

    #FIRST, Populate the list
    for x in system: ##finds the packs
        pack = system[x]
        for y in pack: ##fishing now throough games
            game = pack[y]
            for z in game: ##each game

                if z == "agli":
                    if z not in pdb:
                        pdb.setdefault(game[z], 0)

    for a in pdb:
        goals = 0
        shots = 0
        gms = 0
        for x in system: ##finds the packs
            pack = system[x]
            for y in pack: ##fishing now throough games
                game = pack[y]
                if game["hgli"] == a:
                    shots += game["hsht"]

                    for z in game:
                        gms += 1
                        for q in scoredQ:
                            if z == q:
                                if game[z] != notme:
                                    goals += 1

        if shots == 0:
            shots = 1
        if goals == 0:
            goals = 10
        avsaveper = shots/goals/100
        avsaveper = 0.995 - avsaveper
        if gms > 2:
            pdb[a] = avsaveper
        else:
            pdb[a] = 0.899

    pdb = sortMyListPlease(pdb)

    return pdb

#####ENDGOALIESAVEAWAY

def getPlayerGoalsAtHome(system):

    pdb = {}
    scoredQ = [
        "hg1", "hg2", "hg3", "hg4", "hg5", "hg6", "hg7", "hg8", "hg9",
        "hg10", "hg11", "hg12"
        ]
    notme = ""

    for x in system: ##finds the packs
        pack = system[x]
        for y in pack: ##fishing now throough games
            game = pack[y]
            for z in game: ##each game

                for q in scoredQ:

                    if z == q:
                        if game[z] != notme:
                            if game[z] not in pdb.keys():
                                pdb.setdefault(game[z], 1)
                            elif game[z] in pdb.keys():
                                pdb[game[z]] += 1

    pdb = sortMyListPlease(pdb)

    return pdb                            

#####ENDGETPLAYERGOALSHOME

def getPlayerGoalsAtAway(system):

    pdb = {}
    scoredQ = [
        "ag1", "ag2",
        "ag3", "ag4",
        "ag5", "ag6",
        "ag7", "ag8",
        "ag9", "ag10",
        "ag11", "ag12"
        ]
    notme = ""

    for x in system: ##finds the packs
        pack = system[x]
        for y in pack: ##fishing now throough games
            game = pack[y]
            for z in game: ##each game

                for q in scoredQ:

                    if z == q:
                        if game[z] != notme:
                            if game[z] not in pdb.keys():
                                pdb.setdefault(game[z], 1)
                            elif game[z] in pdb.keys():
                                pdb[game[z]] += 1

    pdb = sortMyListPlease(pdb)

    return pdb                            

#####ENDGETPLAYERGOALSAWAY

def getAverageSavePerC(system):
    
    goals = 0
    shots = 0
    notme = ""
    scoredQ = [
        "hg1", "ag1", "hg2", "ag2",
        "hg3", "ag3", "hg4", "ag4",
        "hg5", "ag5", "hg6", "ag6",
        "hg7", "ag7", "hg8", "ag8",
        "hg9", "ag9", "hg10", "ag10",
        "hg11", "ag11", "hg12", "ag12"
        ]

    for x in system: ##finds the packs
        pack = system[x]
        for y in pack: ##fishing now throough games
            game = pack[y]
            for z in game: ##each game

                for q in scoredQ:
                    if z == q:
                        if game[z] != notme:
                            goals += 1
                
                if z == "hsht":
                    shots += game[z]
                    
                if z == "asht":
                    shots += game[z]
                                    
                                   
    avsaveper = shots/goals/100
    avsaveper = round(1 - avsaveper, 3)
    return avsaveper

#####ENDGETSAVE%

def setRoster(roster, guys, guysa, team):

    heligibles = {}
    aeligibles = {}

    for x in roster:
        heligibles.setdefault(x, 0)
        aeligibles.setdefault(x, 0)

    for x in heligibles:
        if x in guys.keys():
            heligibles[x] += guys[x]

    for x in aeligibles:
        if x in guysa.keys():
            aeligibles[x] += guysa[x]

    heligibles = sortMyListPlease(heligibles)
    aeligibles = sortMyListPlease(aeligibles)

    i = 1
    while i < 6:
        name = next(iter(heligibles))
        scheme = str(i)
        scheme2 = "hps" + scheme
        team[scheme2] = name
        i += 1
        del heligibles[name]

    i = 1
    while i < 6:
        name = next(iter(heligibles))
        scheme = str(i)
        scheme2 = "hss" + scheme
        team[scheme2] = name
        i += 1
        del heligibles[name]

    i = 1
    while i < 6:
        name = next(iter(aeligibles))
        scheme = str(i)
        scheme2 = "aps" + scheme
        team[scheme2] = name
        i += 1
        del aeligibles[name]

    i = 1
    while i < 6:
        name = next(iter(aeligibles))
        scheme = str(i)
        scheme2 = "ass" + scheme
        team[scheme2] = name
        i += 1
        del aeligibles[name]
    
    return team

#####ENDSETROSTER

def printInOrder(db, string):
    i = 1
    print(string)
    for x in db:
        if isinstance(db[x], str):
            print("%i. %s : %s" %(i, x, db[x]))
        elif isinstance(db[x], dict) or isinstance(db[x], list):
            idontcare = "i don't care"
        else: 
            print("%i. %s : %.2f" %(i, x, db[x]))
        i += 1
    return

#####ENDPRINT

def fillHPrimeOff(team):

    guys = {}

    i = 1
    while i < 6:
        scheme = str(i)
        scheme2 = "hps" + scheme
        guys.setdefault(team[scheme2], 0)
        i += 1

    mysum = 0

    for x in plwhgoals:
        if x in guys.keys():
            guys[x] = plwhgoals[x]

    for x in guys:
        mysum += guys[x]
    
    return mysum

#####ENDFILLPRIME

def fillHSecOff(team):

    guys = {}

    i = 1
    while i < 6:
        scheme = str(i)
        scheme2 = "hss" + scheme
        guys.setdefault(team[scheme2], 0)
        i += 1

    mysum = 0

    for x in plwhgoals:
        if x in guys.keys():
            guys[x] = plwhgoals[x]

    for x in guys:
        mysum += guys[x]
    
    return mysum

#####ENDFILLHSEC

def fillHDOff(team):

    guys = {}

    i = 1
    while i < 6:
        scheme = str(i)
        scheme2 = "hps" + scheme
        guys.setdefault(team[scheme2], 0)
        i += 1

    i = 1
    while i < 6:
        scheme = str(i)
        scheme2 = "hss" + scheme
        guys.setdefault(team[scheme2], 0)
        i += 1

    depguys = {}

    for x in plwhgoals:
        if x in team["roster"]:
            if x not in guys.keys():
                depguys.setdefault(x, 0)

    mysum = 0

    for x in plwhgoals:
        if x in depguys.keys():
            depguys[x] = plwhgoals[x]

    for x in depguys:
        mysum += depguys[x]
    
    return mysum

#####ENDFILLHDEP

def fillAPrimeOff(team):

    guys = {}

    i = 1
    while i < 6:
        scheme = str(i)
        scheme2 = "aps" + scheme
        guys.setdefault(team[scheme2], 0)
        i += 1

    mysum = 0

    for x in plwagoals:
        if x in guys.keys():
            guys[x] = plwagoals[x]

    for x in guys:
        mysum += guys[x]
    
    return mysum

#####ENDFILLPRIME

def fillASecOff(team):

    guys = {}

    i = 1
    while i < 6:
        scheme = str(i)
        scheme2 = "ass" + scheme
        guys.setdefault(team[scheme2], 0)
        i += 1

    mysum = 0

    for x in plwhgoals:
        if x in guys.keys():
            guys[x] = plwagoals[x]

    for x in guys:
        mysum += guys[x]
    
    return mysum

#####ENDFILLASEC

def fillADOff(team):

    guys = {}

    i = 1
    while i < 6:
        scheme = str(i)
        scheme2 = "aps" + scheme
        guys.setdefault(team[scheme2], 0)
        i += 1

    i = 1
    while i < 6:
        scheme = str(i)
        scheme2 = "ass" + scheme
        guys.setdefault(team[scheme2], 0)
        i += 1

    depguys = {}

    for x in plwagoals:
        if x in team["roster"]:
            if x not in guys.keys():
                depguys.setdefault(x, 0)

    mysum = 0

    for x in plwagoals:
        if x in depguys.keys():
            depguys[x] = plwagoals[x]

    for x in depguys:
        mysum += depguys[x]
    
    return mysum

#####ENDFILLADEP

def giveMeHPrimes(system):
    mydb = {}

    for x in system:
        nuke = system[x]
        mydb.setdefault(nuke["hps1"], 0)
        mydb.setdefault(nuke["hps2"], 0)
        mydb.setdefault(nuke["hps3"], 0)
        mydb.setdefault(nuke["hps4"], 0)
        mydb.setdefault(nuke["hps5"], 0)

    for x in mydb:
        if x in plwhgoals.keys():
            mydb[x] = plwhgoals[x]

    mydb = sortMyListPlease(mydb)

    return mydb

#####ENDGIVEMEPRIMES

def giveMeAPrimes(system):
    mydb = {}

    for x in system:
        nuke = system[x]
        mydb.setdefault(nuke["aps1"], 0)
        mydb.setdefault(nuke["aps2"], 0)
        mydb.setdefault(nuke["aps3"], 0)
        mydb.setdefault(nuke["aps4"], 0)
        mydb.setdefault(nuke["aps5"], 0)

    for x in mydb:
        if x in plwagoals.keys():
            mydb[x] = plwagoals[x]

    mydb = sortMyListPlease(mydb)

    return mydb

#####ENDGIVEMEPRIMES

def giveMeHSeconds(system):
    mydb = {}

    for x in system:
        nuke = system[x]
        mydb.setdefault(nuke["hss1"], 0)
        mydb.setdefault(nuke["hss2"], 0)
        mydb.setdefault(nuke["hss3"], 0)
        mydb.setdefault(nuke["hss4"], 0)
        mydb.setdefault(nuke["hss5"], 0)

    for x in mydb:
        if x in plwhgoals.keys():
            mydb[x] = plwhgoals[x]

    mydb = sortMyListPlease(mydb)

    return mydb

#####ENDGIVEMEPRIMES

def giveMeASeconds(system):
    mydb = {}

    for x in system:
        nuke = system[x]
        mydb.setdefault(nuke["ass1"], 0)
        mydb.setdefault(nuke["ass2"], 0)
        mydb.setdefault(nuke["ass3"], 0)
        mydb.setdefault(nuke["ass4"], 0)
        mydb.setdefault(nuke["ass5"], 0)

    for x in mydb:
        if x in plwagoals.keys():
            mydb[x] = plwagoals[x]

    mydb = sortMyListPlease(mydb)

    return mydb

#####ENDGIVEMEPRIMES

def giveMeHDepths(mpr, mse, tms):
    mydb = {}

    for x in tms:
        theteam = tms[x]
        for y in theteam["roster"]:
            if y not in mpr:
                if y not in mse:
                    mydb.setdefault(y, 0)

    for x in mydb:
        if x in plwhgoals:
            mydb[x] = plwhgoals[x]

    mydb = sortMyListPlease(mydb)

    return mydb

#####ENDGIVEMEHDEPTHS

def giveMeADepths(mpr, mse, tms):
    mydb = {}

    for x in tms:
        theteam = tms[x]
        for y in theteam["roster"]:
            if y not in mpr:
                if y not in mse:
                    mydb.setdefault(y, 0)

    for x in mydb:
        if x in plwagoals:
            mydb[x] = plwagoals[x]

    mydb = sortMyListPlease(mydb)

    return mydb

#####ENDGIVEMEADEPTHS

def giveMeAvgHPrOff(tms):
    mysum = []

    for x in tms:
        theteam = tms[x]
        mysum.append(theteam["homeprimeoffpot"])

    avg = sum(mysum)/len(mysum)
    
    return round(avg, 2)

#####ENDGIVEMEAVGPROFF

def giveMeAvgAPrOff(tms):
    mysum = []

    for x in tms:
        theteam = tms[x]
        mysum.append(theteam["awayprimeoffpot"])

    avg = sum(mysum)/len(mysum)
    
    return round(avg, 2)

#####ENDGIVEMEAAVGPROFF

def giveMeAvgHSeOff(tms):
    mysum = []

    for x in tms:
        theteam = tms[x]
        mysum.append(theteam["homesecoffpot"])

    avg = sum(mysum)/len(mysum)
    
    return round(avg, 2)

#####ENDGIVEMEAVGPROFF

def giveMeAvgASeOff(tms):
    mysum = []

    for x in tms:
        theteam = tms[x]
        mysum.append(theteam["awaysecoffpot"])

    avg = sum(mysum)/len(mysum)
    
    return round(avg, 2)

#####ENDGIVEMEAAVGPROFF

def giveMeAvgHDepOff(tms):
    mysum = []

    for x in tms:
        theteam = tms[x]
        mysum.append(theteam["homedepoffpot"])

    avg = sum(mysum)/len(mysum)
    
    return round(avg, 2)

#####ENDGIVEMEAVGDEOFF

def giveMeAvgADepOff(tms):
    mysum = []

    for x in tms:
        theteam = tms[x]
        mysum.append(theteam["awaydepoffpot"])

    avg = sum(mysum)/len(mysum)
    
    return round(avg, 2)

#####ENDGIVEMEAAVGDEOFF

def calculateHPDef(gdb, team):
    scorers = {}
    goals = ["ag1", "ag2", "ag3", "ag4", "ag5", "ag6", "ag7", "ag8", "ag9", "ag10", "ag11", "ag12"]
    notme = ""
    for x in gdb: ## searches game packs
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["hteam"] == team["team"]:
                for z in game:
                    for g in goals:
                        if z == g:
                            if game[g] != notme:
                                if game[g] not in scorers:
                                    if game[g] in Aprimesdb.keys():
                                        scorers.setdefault(game[g], 1)
                                else:
                                    goalman = game[g]
                                    scorers[goalman] += 1

    
    
    mysum = 0
    for x in scorers:
        mysum += scorers[x]

    return mysum                

#####ENDCALCULATEPRIMEHMDEF

def calculateHSDef(gdb, team):
    scorers = {}
    goals = ["ag1", "ag2", "ag3", "ag4", "ag5", "ag6", "ag7", "ag8", "ag9", "ag10", "ag11", "ag12"]
    notme = ""
    for x in gdb: ## searches game packs
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["hteam"] == team["team"]:
                for z in game:
                    for g in goals:
                        if z == g:
                            if game[g] != notme:
                                if game[g] not in scorers:
                                    if game[g] in Aseconddb.keys():
                                        scorers.setdefault(game[g], 1)
                                else:
                                    goalman = game[g]
                                    scorers[goalman] += 1

    mysum = 0
    for x in scorers:
        mysum += scorers[x]

    return mysum                

#####ENDCALCULATEPRIMEHMDEF

def calculateHDDef(gdb, team):
    scorers = {}
    goals = ["ag1", "ag2", "ag3", "ag4", "ag5", "ag6", "ag7", "ag8", "ag9", "ag10", "ag11", "ag12"]
    notme = ""
    for x in gdb: ## searches game packs
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["hteam"] == team["team"]:
                for z in game:
                    for g in goals:
                        if z == g:
                            if game[g] != notme:
                                if game[g] not in scorers:
                                    if game[g] in Adepthdb.keys():
                                        scorers.setdefault(game[g], 1)
                                else:
                                    goalman = game[g]
                                    scorers[goalman] += 1

    mysum = 0
    for x in scorers:
        mysum += scorers[x]

    return mysum                

#####ENDCALCULATEPRIMEHMDEF

def calculateAPDef(gdb, team):
    scorers = {}
    goals = ["ag1", "ag2", "ag3", "ag4", "ag5", "ag6", "ag7", "ag8", "ag9", "ag10", "ag11", "ag12"]
    notme = ""
    for x in gdb: ## searches game packs
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["hteam"] == team["team"]:
                for z in game:
                    for g in goals:
                        if z == g:
                            if game[g] != notme:
                                if game[g] not in scorers:
                                    if game[g] in Hprimesdb.keys():
                                        scorers.setdefault(game[g], 1)
                                else:
                                    goalman = game[g]
                                    scorers[goalman] += 1

    mysum = 0
    for x in scorers:
        mysum += scorers[x]

    return mysum                

#####ENDCALCULATEPRIMEHMDEF

def calculateASDef(gdb, team):
    scorers = {}
    goals = ["ag1", "ag2", "ag3", "ag4", "ag5", "ag6", "ag7", "ag8", "ag9", "ag10", "ag11", "ag12"]
    notme = ""
    for x in gdb: ## searches game packs
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["hteam"] == team["team"]:
                for z in game:
                    for g in goals:
                        if z == g:
                            if game[g] != notme:
                                if game[g] not in scorers:
                                    if game[g] in Hseconddb.keys():
                                        scorers.setdefault(game[g], 1)
                                else:
                                    goalman = game[g]
                                    scorers[goalman] += 1

    mysum = 0
    for x in scorers:
        mysum += scorers[x]

    return mysum                

#####ENDCALCULATEPRIMEHMDEF

def calculateADDef(gdb, team):
    scorers = {}
    goals = ["ag1", "ag2", "ag3", "ag4", "ag5", "ag6", "ag7", "ag8", "ag9", "ag10", "ag11", "ag12"]
    notme = ""
    for x in gdb: ## searches game packs
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["hteam"] == team["team"]:
                for z in game:
                    for g in goals:
                        if z == g:
                            if game[g] != notme:
                                if game[g] not in scorers:
                                    if game[g] in Hdepthdb.keys():
                                        scorers.setdefault(game[g], 1)
                                else:
                                    goalman = game[g]
                                    scorers[goalman] += 1

    mysum = 0
    for x in scorers:
        mysum += scorers[x]

    return mysum                

#####ENDCALCULATEPRIMEHMDEF

def calculateHShotsFB(gdb, t):
    mysum = 0
    games = 0
    for x in gdb:
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["hteam"] == t["team"]:
                if game["firstblood"] == t["team"]:
                    mysum += game["hsht"]
                    games += 1

    avg = round(mysum/games, 2)
    return avg

#####ENDCALCULATEHSHOTSFB

def calculateAShotsFB(gdb, t):
    mysum = 0
    games = 0
    for x in gdb:
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["ateam"] == t["team"]:
                if game["firstblood"] == t["team"]:
                    mysum += game["asht"]
                    games += 1

    avg = round(mysum/games, 2)
    return avg

#####ENDCALCULATEHSHOTSFB

def calculateHShotsFBed(gdb, t):
    mysum = 0
    games = 0
    for x in gdb:
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["hteam"] == t["team"]:
                if game["firstblood"] != t["team"]:
                    mysum += game["hsht"]
                    games += 1

    avg = round(mysum/games, 2)
    return avg

#####ENDCALCULATEHSHOTSFB

def calculateAShotsFBed(gdb, t):
    mysum = 0
    games = 0
    for x in gdb:
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["ateam"] == t["team"]:
                if game["firstblood"] != t["team"]:
                    mysum += game["asht"]
                    games += 1

    avg = round(mysum/games, 2)
    return avg

#####ENDCALCULATEHSHOTSFB

def calculateFBH(gdb, t):
    yes = 0
    games = 0
    for x in gdb:
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["hteam"] == t["team"]:
                games += 1
                if game["firstblood"] == t["team"]:
                    yes += 1

    mynum = round(yes/games, 2)

    return mynum

#####ENDCALCULATEHSHOTSFB

def calculateFBA(gdb, t):
    yes = 0
    games = 0
    for x in gdb:
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["ateam"] == t["team"]:
                games += 1
                if game["firstblood"] == t["team"]:
                    yes += 1

    mynum = round(yes/games, 2)

    return mynum

#####ENDCALCULATEHSHOTSFB

def calculateShotMitigationH(gdb, t):
    ttlshots = 0
    games = 0
    for x in gdb:
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["hteam"] == t["team"]:
                ttlshots += game["asht"]
                games += 1

    mynum = round(ttlshots/games, 2)
    mynum = round(mynum/avshotspg, 2)
    return mynum

#####ENDCALCULATEHSHOTSFB

def calculateShotMitigationA(gdb, t):
    ttlshots = 0
    games = 0
    for x in gdb:
        week = gdb[x]
        for y in week:
            game = week[y]

            if game["ateam"] == t["team"]:
                ttlshots += game["hsht"]
                games += 1

    mynum = round(ttlshots/games, 2)
    mynum = round(mynum/avshotspg, 2)
    return mynum

#####ENDCALCULATEHSHOTSFB

def identifyWeres(teams, system):
    weres = {}

    eligibles = {}
    positions = [
        "hps1", "hps2", "hps3", "hps4", "hps5",
        "hss1", "hss2", "hss3", "hss4", "hss5",
        "aps1", "aps2", "aps3", "aps4", "aps5",
        "ass1", "ass2", "ass3", "ass4", "ass5"
        ]

    for x in teams:
        team = teams[x]

        for y in positions:
            if team[y] not in eligibles:
               eligibles.setdefault(team[y], 0)

    for a in eligibles:
        allgoals = 0
        weregoals = 0
        for x in system:
            week = system[x]
            for y in week:
                game = week[y]

                for g in game:
                    if game[g] == a:
                        allgoals += 1
                        if game["lunar"] > 49:
                            weregoals += 1

        perc = weregoals/allgoals
        if perc > 0.75 and allgoals > 4:
            weres.setdefault(a, perc)

    weres = sortMyListPlease(weres)
    #printInOrder(weres, "Weres")
    return weres

#####ENDID

def identifyVamps(teams, system):
    vamps = {}

    eligibles = {}
    positions = [
        "hps1", "hps2", "hps3", "hps4", "hps5",
        "hss1", "hss2", "hss3", "hss4", "hss5",
        "aps1", "aps2", "aps3", "aps4", "aps5",
        "ass1", "ass2", "ass3", "ass4", "ass5"
        ]

    for x in teams:
        team = teams[x]

        for y in positions:
            if team[y] not in eligibles:
               eligibles.setdefault(team[y], 0)

    for a in eligibles:
        allgoals = 0
        vampgoals = 0
        for x in system:
            week = system[x]
            for y in week:
                game = week[y]

                for g in game:
                    if game[g] == a:
                        allgoals += 1
                        if game["lunar"] <= 49:
                            vampgoals += 1

        perc = vampgoals/allgoals
        if perc > 0.75 and allgoals > 4:
            vamps.setdefault(a, perc)

    vamps = sortMyListPlease(vamps)
    #printInOrder(vamps, "Vamps")
    return vamps

#####ENDID

def calculateAvGoals(system):
    totalgoals = 0
    teams = 32

    for x in system:
        team = system[x]

        totalgoals += team["homeprimeoffpot"]
        totalgoals += team["homesecoffpot"]
        totalgoals += team["homedepoffpot"]
        totalgoals += team["awayprimeoffpot"]
        totalgoals += team["awaysecoffpot"]
        totalgoals += team["awaydepoffpot"]

    avg = totalgoals/teams
    return avg        

#####AVGOALS

def calculatePowerRank(tms, system):
    mylist = {}

    for x in tms:
        team = tms[x]
        mylist.setdefault(team["team"], 0)

    for x in tms:
        team = tms[x]
        goalsfor = team["homeprimeoffpot"] + team["homesecoffpot"] + team["homedepoffpot"]
        goalsfor += team["awayprimeoffpot"] + team["awaysecoffpot"] + team["awaydepoffpot"]
        goalsagainst = team["homeprimedefpot"] + team["homesecdefpot"] + team["homedepdefpot"]
        goalsagainst += team["awayprimedefpot"] + team["awaysecdefpot"] + team["awaydepdefpot"]
        power = hundredBalance(goalsfor, goalsagainst)
        team["powerlevel"] = power
        mylist[team["team"]] = power

    mylist = sortMyListPlease(mylist)
    #printInOrder(mylist, "Power Rank")
        
    return mylist

#####ENDPR

def calculateShotPerc(system, t):
    totalshots = 0
    totalgoals = t["homeprimeoffpot"] + t["homesecoffpot"] + t["homedepoffpot"]
        
    for x in system:
        week = system[x]
        for y in week:
            game = week[y]
            if game["hteam"] == t["team"]:
                totalshots += game["hsht"]
    
    shotper = round(totalgoals/totalshots, 3)
    return shotper

#####ENDSHOTPERC

def calculateShotPercA(system, t):
    totalshots = 0
    totalgoals = t["awayprimeoffpot"] + t["awaysecoffpot"] + t["awaydepoffpot"]
        
    for x in system:
        week = system[x]
        for y in week:
            game = week[y]
            if game["ateam"] == t["team"]:
                totalshots += game["asht"]
    
    shotper = round(totalgoals/totalshots, 3)
    return shotper
    
#####ENDASHOTPERC

def FillOut1(t, rosteam):

    t["roster"] = rosteam
    t["homeprimeoffpot"] = fillHPrimeOff(t)
    t["homesecoffpot"] = fillHSecOff(t)
    t["homedepoffpot"] = fillHDOff(t)

    t["awayprimeoffpot"] = fillAPrimeOff(t)
    t["awaysecoffpot"] = fillASecOff(t)
    t["awaydepoffpot"] = fillADOff(t)
 
    return t

#####ENDFILLOUT1

def FillOut2(t):

    t["hpopower"] = hundredBalance(t["homeprimeoffpot"], avgPrHOff)
    t["hsopower"] = hundredBalance(t["homesecoffpot"], avgSeHOff)
    t["hdopower"] = hundredBalance(t["homedepoffpot"], avgDepHOff)

    t["apopower"] = hundredBalance(t["awayprimeoffpot"], avgPrAOff)
    t["asopower"] = hundredBalance(t["awaysecoffpot"], avgSeAOff)
    t["adopower"] = hundredBalance(t["awaydepoffpot"], avgDepAOff)

    t["homeprimedefpot"] = calculateHPDef(relgamedb, t)
    t["homesecdefpot"] = calculateHSDef(relgamedb, t)
    t["homedepdefpot"] = calculateHDDef(relgamedb, t)
    t["hpdpower"] = hundredBalance(avgPrHOff, t["homeprimedefpot"])
    t["hsdpower"] = hundredBalance(avgSeHOff, t["homesecdefpot"])
    t["hddpower"] = hundredBalance(avgDepHOff, t["homedepdefpot"]) 

    t["awayprimedefpot"] = calculateAPDef(relgamedb, t)
    t["awaysecdefpot"] = calculateASDef(relgamedb, t)
    t["awaydepdefpot"] = calculateADDef(relgamedb, t)
    t["apdpower"] = hundredBalance(avgPrAOff, t["awayprimedefpot"])
    t["asdpower"] = hundredBalance(avgSeAOff, t["awaysecdefpot"])
    t["addpower"] = hundredBalance(avgDepAOff, t["awaydepdefpot"])

    t["homeavshotsfb"] = calculateHShotsFB(relgamedb, t)
    t["homeavshotsfbed"] = calculateHShotsFBed(relgamedb, t)
    t["awayavshotsfb"] = calculateAShotsFB(relgamedb, t)
    t["awayavshotsfbed"] = calculateAShotsFBed(relgamedb, t)
    t["avfbathome"] = calculateFBH(relgamedb, t)
    t["avfbaway"] = calculateFBA(relgamedb, t)

    t["homeshotmitigation"] = calculateShotMitigationH(relgamedb, t)
    t["awayshotmitigation"] = calculateShotMitigationA(relgamedb, t)
    t["homeshotperc"] = calculateShotPerc(relgamedb, t)
    t["awayshotperc"] = calculateShotPercA(relgamedb, t)

    return t

################################TEAM STATS##############################

##Averages##

avshotspg = getShotsPerGame(relgamedb)
avsaveperc = getAverageSavePerC(relgamedb)
global plwhgoals
plwhgoals = getPlayerGoalsAtHome(relgamedb)
global plwagoals
plwagoals = getPlayerGoalsAtAway(relgamedb)
global goalihsp
goalihsp = getGoalieSavePAtHome(relgamedb)
global goaliasp
goaliasp = getGoalieSavePAtAway(relgamedb)
#printInOrder(goalihsp, "goalies")

#printInOrder(plwhgoals, "HOME")
#printInOrder(plwagoals, "Away")

#######FILL OUT OFFENSE FIRST###########
##METROPOLITAN
Devils = {"team" : "Devils"}
Devils = setRoster(ros.Devils, plwhgoals, plwagoals, Devils)
Devils = FillOut1(Devils, ros.Devils)
Rangers = {"team" : "Rangers"}
Rangers = setRoster(ros.Rangers, plwhgoals, plwagoals, Rangers)
Rangers = FillOut1(Rangers, ros.Rangers)
BlueJackets = {"team" : "Blue Jackets"}
BlueJackets = setRoster(ros.BlueJackets, plwhgoals, plwagoals, BlueJackets)
BlueJackets = FillOut1(BlueJackets, ros.BlueJackets)
Flyers = {"team" : "Flyers"}
Flyers = setRoster(ros.Flyers, plwhgoals, plwagoals, Flyers)
Flyers = FillOut1(Flyers, ros.Flyers)
Capitals = {"team" : "Capitals"}
Capitals = setRoster(ros.Capitals, plwhgoals, plwagoals, Capitals)
Capitals = FillOut1(Capitals, ros.Capitals)
Penguins = {"team" : "Penguins"}
Penguins = setRoster(ros.Penguins, plwhgoals, plwagoals, Penguins)
Penguins = FillOut1(Penguins, ros.Penguins)
Hurricanes = {"team" : "Hurricanes"}
Hurricanes = setRoster(ros.Hurricanes, plwhgoals, plwagoals, Hurricanes)
Hurricanes = FillOut1(Hurricanes, ros.Hurricanes)
Islanders = {"team" : "Islanders"}
Islanders = setRoster(ros.Islanders, plwhgoals, plwagoals, Islanders)
Islanders = FillOut1(Islanders, ros.Islanders)

##ATLANTIC

Canadiens = {"team" : "Canadiens"}
Canadiens = setRoster(ros.Canadiens, plwhgoals, plwagoals, Canadiens)
Canadiens = FillOut1(Canadiens, ros.Canadiens)
MapleLeafs = {"team" : "Maple Leafs"}
MapleLeafs = setRoster(ros.MapleLeafs, plwhgoals, plwagoals, MapleLeafs)
MapleLeafs = FillOut1(MapleLeafs, ros.MapleLeafs)
Bruins = {"team" : "Bruins"}
Bruins = setRoster(ros.Bruins, plwhgoals, plwagoals, Bruins)
Bruins = FillOut1(Bruins, ros.Bruins)
Lightning = {"team" : "Lightning"}
Lightning = setRoster(ros.Lightning, plwhgoals, plwagoals, Lightning)
Lightning = FillOut1(Lightning, ros.Lightning)
Sabres = {"team" : "Sabres"}
Sabres = setRoster(ros.Sabres, plwhgoals, plwagoals, Sabres)
Sabres = FillOut1(Sabres, ros.Sabres)
Panthers = {"team" : "Panthers"}
Panthers = setRoster(ros.Panthers, plwhgoals, plwagoals, Panthers)
Panthers = FillOut1(Panthers, ros.Panthers)
Senators = {"team" : "Senators"}
Senators = setRoster(ros.Senators, plwhgoals, plwagoals, Senators)
Senators = FillOut1(Senators, ros.Senators)
RedWings = {"team" : "Red Wings"}
RedWings = setRoster(ros.RedWings, plwhgoals, plwagoals, RedWings)
RedWings = FillOut1(RedWings, ros.RedWings)

##PACIFIC

Sharks = {"team" : "Sharks"}
Sharks = setRoster(ros.Sharks, plwhgoals, plwagoals, Sharks)
Sharks = FillOut1(Sharks, ros.Sharks)
GoldenKnights = {"team" : "Golden Knights"}
GoldenKnights = setRoster(ros.GoldenKnights, plwhgoals, plwagoals, GoldenKnights)
GoldenKnights = FillOut1(GoldenKnights, ros.GoldenKnights)
Canucks = {"team" : "Canucks"}
Canucks = setRoster(ros.Canucks, plwhgoals, plwagoals, Canucks)
Canucks = FillOut1(Canucks, ros.Canucks)
Kings = {"team" : "Kings"}
Kings = setRoster(ros.Kings, plwhgoals, plwagoals, Kings)
Kings = FillOut1(Kings, ros.Kings)
Ducks = {"team" : "Ducks"}
Ducks = setRoster(ros.Ducks, plwhgoals, plwagoals, Ducks)
Ducks = FillOut1(Ducks, ros.Ducks)
Coyotes = {"team" : "Coyotes"}
Coyotes = setRoster(ros.Coyotes, plwhgoals, plwagoals, Coyotes)
Coyotes = FillOut1(Coyotes, ros.Coyotes)
Flames = {"team" : "Flames"}
Flames = setRoster(ros.Flames, plwhgoals, plwagoals, Flames)
Flames = FillOut1(Flames, ros.Flames)
Oilers = {"team" : "Oilers"}
Oilers = setRoster(ros.Oilers, plwhgoals, plwagoals, Oilers)
Oilers = FillOut1(Oilers, ros.Oilers)

##CENTRAL

Stars = {"team" : "Stars"}
Stars = setRoster(ros.Stars, plwhgoals, plwagoals, Stars)
Stars = FillOut1(Stars, ros.Stars)
Avalanche = {"team" : "Avalanche"}
Avalanche = setRoster(ros.Avalanche, plwhgoals, plwagoals, Avalanche)
Avalanche = FillOut1(Avalanche, ros.Avalanche)
Blues = {"team" : "Blues"}
Blues = setRoster(ros.Blues, plwhgoals, plwagoals, Blues)
Blues = FillOut1(Blues, ros.Blues)
Blackhawks = {"team" : "Blackhawks"}
Blackhawks = setRoster(ros.Blackhawks, plwhgoals, plwagoals, Blackhawks)
Blackhawks = FillOut1(Blackhawks, ros.Blackhawks)
Wild = {"team" : "Wild"}
Wild = setRoster(ros.Wild, plwhgoals, plwagoals, Wild)
Wild = FillOut1(Wild, ros.Wild)
Jets = {"team" : "Jets"}
Jets = setRoster(ros.Jets, plwhgoals, plwagoals, Jets)
Jets = FillOut1(Jets, ros.Jets)
Predators = {"team" : "Predators"}
Predators = setRoster(ros.Predators, plwhgoals, plwagoals, Predators)
Predators = FillOut1(Predators, ros.Predators)

teamStudy = {
    "t1" : Devils, "t2" : Rangers, "t3" : BlueJackets, "t4" : Flyers,
    "t5" : Capitals, "t6" : Penguins, "t7" : Hurricanes, "t8" : Islanders,
    "t9" : Canadiens, "t10" : MapleLeafs, "t11" : Bruins, "t12" : Lightning,
    "t13" : Sabres, "t14" : Panthers, "t15" : Senators, "t16" : RedWings,
    "t17" : Sharks, "t18" : GoldenKnights, "t19" : Canucks, "t20" : Kings,
    "t21" : Ducks, "t22" : Coyotes, "t23" : Flames, "t24" : Oilers,
    "t25" : Stars, "t26" : Avalanche, "t27" : Blues, "t28" : Blackhawks,
    "t29" : Wild, "t30" : Jets, "t31" : Predators
    }

##MORE USEFUL DATABASES
global Hprimesdb, Hseconddb, Hdepthdb, Aprimesdb, Aseconddb, Adepthdb
global avgPrHOff, avgPrAOff, avgSeHOff, avgSeAOff, avgDepHOff, avgDepAOff
Hprimesdb = giveMeHPrimes(teamStudy)
Hseconddb = giveMeHSeconds(teamStudy)
Hdepthdb = giveMeHDepths(Hprimesdb, Hseconddb, teamStudy)
Aprimesdb = giveMeAPrimes(teamStudy)
Aseconddb = giveMeASeconds(teamStudy)
Adepthdb = giveMeADepths(Aprimesdb, Aseconddb, teamStudy)
avgPrHOff = giveMeAvgHPrOff(teamStudy)
avgPrAOff = giveMeAvgAPrOff(teamStudy)
avgSeHOff = giveMeAvgHSeOff(teamStudy)
avgSeAOff = giveMeAvgASeOff(teamStudy)
avgDepHOff = giveMeAvgHDepOff(teamStudy)
avgDepAOff = giveMeAvgADepOff(teamStudy)
global plweres, plvamps, avGoals, powerdb
plweres = identifyWeres(teamStudy, relgamedb)
plvamps = identifyVamps(teamStudy, relgamedb)
avGoals = calculateAvGoals(teamStudy)
##NOW THE DEFENSE
Devils, Rangers, BlueJackets, Flyers = FillOut2(Devils), FillOut2(Rangers), FillOut2(BlueJackets), FillOut2(Flyers)
Capitals, Penguins, Hurricanes, Islanders = FillOut2(Capitals), FillOut2(Penguins), FillOut2(Hurricanes), FillOut2(Islanders)
Canadiens, MapleLeafs, Bruins, Lightning = FillOut2(Canadiens), FillOut2(MapleLeafs), FillOut2(Bruins), FillOut2(Lightning)
Sabres, Panthers, Senators, RedWings = FillOut2(Sabres), FillOut2(Panthers), FillOut2(Senators), FillOut2(RedWings)
Sharks, GoldenKnights, Canucks, Kings = FillOut2(Sharks), FillOut2(GoldenKnights), FillOut2(Canucks), FillOut2(Kings)
Ducks, Coyotes, Flames, Oilers = FillOut2(Ducks), FillOut2(Coyotes), FillOut2(Flames), FillOut2(Oilers)
Stars, Avalanche, Blues, Blackhawks = FillOut2(Stars), FillOut2(Avalanche), FillOut2(Blues), FillOut2(Blackhawks)
Wild, Jets, Predators = FillOut2(Wild), FillOut2(Jets), FillOut2(Predators)

powerdb = calculatePowerRank(teamStudy, relgamedb)
#printInOrder(powerdb, "Power Rankings")
#printInOrder(plweres, "WERES")
#printInOrder(plvamps, "VAMPS")
