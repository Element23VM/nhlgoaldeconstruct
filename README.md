# nhlgoaldeconstruct
Breaks down team performance based on shot percentage and goals

linkage connects the database to the main file
the main file is the nhl teams one
rosters have current rosters - i hashtag injuries (don't get them all)

the database files keep the games, a "lunar meta" (basically the number is how full a moon is in increments of 7 per day, max 100)
it keeps goals (but not assists), starting goaltenders, shots, and separates home and away stats

to run the file, go to the nhlsim file and adjust the things at the bottom:
they go mainSim(t.(team), ("goaltenderlastname, firstinitial"), t.(awayteam), ("goaltenderlastname, firstinitial"), (meta))

run from IDLE or whatever other program, usually with f5 - if you get an error in another file, your linkage is not set up;
the only thing you have to watch for is typing the team names properly; you'll find them at the bottom of the teamsfun file
the two name teams (Blue Jackets, Golden Knights, Red Wings, Maple Leafs) are just crunched together without spacing, but keep the 
caps... 
