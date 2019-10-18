import teamsfun as t

def attack(attack, defense):
    whole = attack + defense
    success = attack/whole
    success = 200 * success
    return success

def scoreMe(prim, sec, team, system, homeaway):
    highlist = {}
    lowlist = {}
    mylist = {}

    prim, sec = prim/100, sec/100
    if homeaway == "home":
        ref1 = [
            "hps1", "hps2", "hps3", "hps4", "hps5"
            ]
        ref2 = [
            "hss1", "hss2", "hss3", "hss4", "hss5"
            ]
    else:
        ref1 = [
            "aps1", "aps2", "aps3", "aps4", "aps5"
            ]
        ref2 = [
            "ass1", "ass2", "ass3", "ass4", "ass5"
            ]

    for x in ref1:
        highlist.setdefault(team[x], 0)
    for x in ref2:
        lowlist.setdefault(team[x], 0)

    for x in highlist:
        highlist[x] = system[x] * prim
        mylist.setdefault(x, highlist[x])
    for x in lowlist:
        if x in system:
            lowlist[x] = system[x] * sec
            mylist.setdefault(x, lowlist[x])

    mylist = t.sortMyListPlease(mylist)

    i = 1
    print("Most likely scorers for %s" %team["team"])
    for x in mylist:
        print("%i : %s : %i" %(i, x, int(mylist[x])))
        i += 1
        if i == 5:
            break
    
    return mylist

def mainSim(h, hgli, a, agli, meta):
    #compare the swords
    awpratt = attack(a["apopower"], h["hpdpower"])
    awsdatt = attack(a["asopower"], h["hsdpower"])
    awdpatt = attack(a["adopower"], h["hddpower"])
    hpratt = attack(a["hpopower"], h["apdpower"])
    hsdatt = attack(a["hsopower"], h["asdpower"])
    hdpatt = attack(a["hdopower"], h["addpower"])
    print("%s prime attack: %i" %(a["team"], int(awpratt)))
    print("%s second attack: %i" %(a["team"], int(awsdatt)))
    print("%s depth attack: %i" %(a["team"], int(awdpatt)))
    print("%s prime attack: %i" %(h["team"], int(hpratt)))
    print("%s second attack: %i" %(h["team"], int(hsdatt)))
    print("%s depth attack: %i" %(h["team"], int(hdpatt)))
    
    #determine most likely first blood
    firstcon = attack(h["avfbathome"], a["avfbaway"])
    if firstcon > 100:
        print("%s is more likely to get first blood.  Value: %i (higher = better)" %(h["team"], int(firstcon)))
        firstblood = h["team"]
    else:
        print("%s is more likely to get first blood.  Value: %i (lower = better)" %(a["team"], int(firstcon)))
        firstblood = a["team"]
        
    #determine shots
    if firstblood == h["team"]:
        hshots = h["homeavshotsfb"] * a["awayshotmitigation"]
        ashots = a["awayavshotsfbed"] * h["homeshotmitigation"]
    else:
        hshots = h["homeavshotsfbed"] * a["awayshotmitigation"]
        ashots = a["awayavshotsfb"] * h["homeshotmitigation"]

    print("%s projected shots: %i" %(h["team"], int(hshots)))
    print("%s projected shots: %i" %(a["team"], int(ashots)))

    #determine most likely scorers
    hlist = {}
    alist = {}
    hlist = scoreMe(hpratt, hsdatt, h, t.plwhgoals, "home")
    alist = scoreMe(awpratt, awsdatt, a, t.plwagoals, "away")

    #caution about wolves and weres
    if meta > 74:
        for x in t.plweres:
            if x in h.values():
                print("Bonus, %s is a were" %x)
            if x in a.values():
                print("Bonus, %s is a were" %x)
        for x in t.plvamps:
            if x in h.values():
                print("Beware, %s is a vamp" %x)
            if x in a.values():
                print("Beware, %s is a vamp" %x)
    elif meta < 26:
        for x in t.plweres:
            if x in h.values():
                print("Beware, %s is a were" %x)
            if x in a.values():
                print("Beware, %s is a were" %x)
        for x in t.plvamps:
            if x in h.values():
                print("Bonus, %s is a vamp" %x)
            if x in a.values():
                print("Bonus, %s is a vamp" %x)
    else:
        idonothing = ""

    #determine projected score based on shot percentage vs goalie mitigation
    hgoal = 0
    agoal = 0
    if hgli in t.goalihsp:
        hgoal = t.goalihsp[hgli]
    else:
        hgoal = 0.890

    if agli in t.goaliasp:
        agoal = t.goaliasp[agli]
    else:
        agoal = 0.89
    
    hgoalmit = (attack(t.avsaveperc, hgoal))/100
    agoalmit = (attack(t.avsaveperc, agoal))/100
    
    homegoals = (h["homeshotperc"] * agoalmit)*hshots
    awaygoals = (a["awayshotperc"] * hgoalmit)*ashots

    print("Final Score: %s : %i   %s : %i" %(h["team"], int(homegoals), a["team"], int(awaygoals)))
    print("Adjusted goal score")
    for x in hlist:
        hlist[x] = hlist[x] + ((homegoals-1) * hlist[x]*0.5)
        print ("%s : %.2f" %(x, hlist[x]))
    for x in alist:
        alist[x] = alist[x] + ((awaygoals-1) * alist[x]*0.5)
        print ("%s : %.2f" %(x, alist[x]))

    print("---------------------------------------------")
    return

#####end mainsim

meta = 65
mainSim(t.Panthers, "Bobrovsky, S", t.Avalanche, "Grubauer, P", meta) 
mainSim(t.Penguins, "Murray, M", t.Stars, "Bishop, B", meta) 
mainSim(t.Capitals, "Holtby, B", t.Rangers, "Lundqvist, H", meta)
mainSim(t.Blackhawks, "Crawford, C", t.BlueJackets, "Korpisalo, J", meta) #murray #gibson
mainSim(t.Oilers, "Smith, M", t.RedWings, "Bernier, J", meta) #allen #nilsson
mainSim(t.Ducks, "Gibson, J", t.Hurricanes, "Mrazek, P", meta) #holtby
#mainSim(t.Coyotes, "Raanta, A", t.Predators, "Rinne, P", meta) #hellebuyck #dubnyk
#mainSim(t.GoldenKnights, "Fleury, M", t.Senators, "Nilsson, A", meta) #dell #crawford
#mainSim(t.Kings, "Campbell, J", t.Sabres, "Hutton, C", meta) #bishop #rittich
#mainSim(t.Stars, "Bishop, B", t.Capitals, "Holtby, B", meta)
#mainSim(t.Wild, "Dubnyk, D", t.Penguins, "Murray, M", meta)
#mainSim(t.Avalanche, "Grubauer, P", t.Coyotes, "Kuemper, D", meta)
#mainSim(t.Canucks, "Markstrom, J", t.Flyers, "Hart, C", meta)
#mainSim(t.GoldenKnights, "Fleury, M", t.Flames, "Rittich, C", meta)


