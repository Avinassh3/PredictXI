import pandas as pd


wick=[20,20,10]
runs=[500,500,150]
awick=[10,10,5]
aruns=[250,250,90]

def finalteam(b,ds,ddd,num,pit):
    extra = []
    a = pd.read_csv(ds)
    pitch = pit
    play = (a['Nation'] == b[1])
    play2 = (a['Nation'] == b[0])
    p = a[play]
    players = p.append(a[play2])
    c = pd.to_numeric(players['Truns'])
    play = (c > runs[num])
    p2 = players[play]
    p2 = p2.sort_values(by=['score'])
    p2 = p2[::-1]
    team1 = (p2['Nation'] == b[1])
    team2 = (p2['Nation'] == b[0])
    bat = p2[team1]
    bat2 = p2[team2]
    batList = list(bat['Playername'].head(2))
    finalbat = batList + (list(bat2['Playername'].head(2)))
    extra.append(bat.iloc[2, 2])
    extra.append(bat2.iloc[2, 2])
    print("Batsmen :")
    print(finalbat)
    print("\n")

    a2 = pd.read_csv(ddd)
    play = (a2['Nation'] == b[1])
    play2 = (a2['Nation'] == b[0])
    p = a2[play]
    player = p.append(a2[play2])
    c = pd.to_numeric(player['Wickets'])
    play = (c > wick[num])
    bowlers = player[play]
    bowlers = bowlers.sort_values(by=['score'])
    team1 = (bowlers['Nation'] == b[1])
    team2 = (bowlers['Nation'] == b[0])
    bowl = bowlers[team1]
    bowl2 = bowlers[team2]
    bowlList = [x for x in list(bowl['Playername']) if x not in finalbat]
    bowlList2 = [x for x in list(bowl2['Playername']) if x not in finalbat]
    finalbowl = bowlList[:2] + bowlList2[:2]
    if (len(bowlList) >= 3):
        extra.append(bowlList[2])
    if (len(bowlList2) >= 3):
        extra.append(bowlList2[2])
    print("Bowlers: ")
    print(finalbowl)
    print("\n")

    play = (a['Nation'] == b[1])
    play2 = (a['Nation'] == b[0])
    p = a[play]
    players = p.append(a[play2])
    c = pd.to_numeric(players['Truns'])
    play = (c > aruns[num])
    p2 = players[play]
    p2 = p2.sort_values(by=['score'])
    p2 = p2[::-1]
    play = (a2['Nation'] == b[1])
    play2 = (a2['Nation'] == b[0])
    p = a2[play]
    player = p.append(a2[play2])
    c = pd.to_numeric(player['Wickets'])
    play = (c > awick[num])
    bowlers = player[play]
    bowlers = bowlers.sort_values(by=['score'])
    bat = pd.Index(p2['Playername'])
    ball = pd.Index(bowlers['Playername'])
    if (pitch==2):
        all = pd.Series(bat.intersection(ball))
        all1 = [i for i in all if i not in finalbat and i not in finalbowl]
        if (len(all1) >= 2):
            finalall = all1[:2]
            print(finalall)
            if (len(all1) >= 4):
                extra.append(all1[3])
                extra.append(all1[2])
        else:
            play = (a['Nation'] == b[1])
            play2 = (a['Nation'] == b[0])
            p = a[play]
            players = p.append(a[play2])
            c = pd.to_numeric(players['Truns'])
            play = (c > aruns[num])
            p2 = players[play]
            p2 = p2.sort_values(by=['score'])
            p2 = p2[::-1]
            play = (a2['Nation'] == b[1])
            play2 = (a2['Nation'] == b[0])
            p = a2[play]
            player = p.append(a2[play2])
            c = pd.to_numeric(player['Wickets'])
            play = (c > awick[num])
            bowlers = player[play]
            bowlers = bowlers.sort_values(by=['score'])
            bat = pd.Index(p2['Playername'])
            ball = pd.Index(bowlers['Playername'])
            all = pd.Series(bat.intersection(ball))
            all1 = [i for i in all if i not in finalbat and i not in finalbowl]
            finalall = all1[:2]
            print(finalall)
            if (len(all1) >= 4):
                extra.append(all1[3])
                extra.append(all1[2])
    else:
        all = pd.Series(ball.intersection(bat))
        all1 = [i for i in all if i not in finalbat and i not in finalbowl]
        if (len(all1) >= 2):
            finalall = all1[:2]
            print(finalall)
            if (len(all1) >= 4):
                extra.append(all1[3])
                extra.append(all1[2])
        else:
            play = (a['Nation'] == b[1])
            play2 = (a['Nation'] == b[0])
            p = a[play]
            players = p.append(a[play2])
            c = pd.to_numeric(players['Truns'])
            play = (c > aruns[num])
            p2 = players[play]
            p2 = p2.sort_values(by=['score'])
            p2 = p2[::-1]
            play = (a2['Nation'] == b[1])
            play2 = (a2['Nation'] == b[0])
            p = a2[play]
            player = p.append(a2[play2])
            c = pd.to_numeric(player['Wickets'])
            play = (c > awick[num])
            bowlers = player[play]
            bowlers = bowlers.sort_values(by=['score'])
            bat = pd.Index(p2['Playername'])
            ball = pd.Index(bowlers['Playername'])
            all = pd.Series(bat.intersection(ball))
            all1 = [i for i in all if i not in finalbat and i not in finalbowl]
            finalall = all1[:2]
            print(finalall)
            if (len(all1) >= 4):
                extra.append(all1[3])
                extra.append(all1[2])
    print("\n\nextra players which are ideal to be replaced :")
    print(extra)


