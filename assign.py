import re
import random
l=["Arsenal (ENG)","Astana (KAZ)","Atlético (ESP)","Barcelona (ESP)","BATE (BLR)",
"Bayern (GER)","Benfica (POR)","Chelsea (ENG)","CSKA Moskva (RUS)","Dinamo Zagreb (CRO)",
"Dynamo Kyiv (UKR)","Galatasaray (TUR)","Gent (BEL)","Juventus (ITA)","Leverkusen (GER)",
"Lyon (FRA)","M. Tel-Aviv (ISR)","Malmö (SWE)","Man. City (ENG)","Man. United (ENG)",
"Mönchengladbach (GER)","Olympiacos (GRE)","Paris (FRA)","Porto (POR)","PSV (NED)",
"Real Madrid (ESP)","Roma (ITA)","Sevilla (ESP)","Shakhtar Donetsk (UKR)","Valencia (ESP)",
"Wolfsburg (GER)","Zenit (RUS)"]

red_teams=["Barcelona (ESP)","Bayern (GER)","Benfica (POR)","Chelsea (ENG)","Juventus (ITA)","Paris (FRA)","PSV (NED)","Zenit (RUS)"]
for i in red_teams:
    l.remove(i)
Group_A ={}
i=0
while(True):
    if(i==0):
        m= random.choice(red_teams)
        y= re.search(".\(",m)
        Group_A[m[y.start()+1:]]= m[:y.start()]
        red_teams.remove(m)
        i+=1
    elif(i<4):
        m = random.choice(l)
        y = re.search(".\(",m)
        if m[y.start()+1:] not in Group_A:
            Group_A[m[y.start()+1:]] = m[:y.start()]
            i+=1
            l.remove(m)
    if(i==4):
        break
print("Group A")
for i in Group_A.values():
    print(i)
print("\n")
#GROUP B
Group_B ={}
i=0
while(True):
    if(i==0):
        m= random.choice(red_teams)
        y= re.search(".\(",m)
        Group_B[m[y.start()+1:]]= m[:y.start()]
        red_teams.remove(m)
        i+=1
    elif(i<4):
        m = random.choice(l)
        y = re.search(".\(",m)
        if m[y.start()+1:] not in Group_B:
            Group_B[m[y.start()+1:]] = m[:y.start()]
            i+=1
            l.remove(m)
    if(i==4):
        break
print("Group B")
for i in Group_B.values():
    print(i)
print("\n")

#GROUP C
Group_C ={}
i=0
while(True):
    if(i==0):
        m= random.choice(red_teams)
        y= re.search(".\(",m)
        Group_C[m[y.start()+1:]]= m[:y.start()]
        red_teams.remove(m)
        i+=1
    elif(i<4):
        m = random.choice(l)
        y = re.search(".\(",m)
        if m[y.start()+1:] not in Group_C:
            Group_C[m[y.start()+1:]] = m[:y.start()]
            i+=1
            l.remove(m)
    if(i==4):
        break
print("Group C")
for i in Group_C.values():
    print(i)
print("\n")

#GROUP D
Group_D ={}
i=0
while(True):
    if(i==0):
        m= random.choice(red_teams)
        y= re.search(".\(",m)
        Group_D[m[y.start()+1:]]= m[:y.start()]
        red_teams.remove(m)
        i+=1
    elif(i<4):
        m = random.choice(l)
        y = re.search(".\(",m)
        if m[y.start()+1:] not in Group_D:
            Group_D[m[y.start()+1:]] = m[:y.start()]
            i+=1
            l.remove(m)
    if(i==4):
        break
print("Group D")
for i in Group_D.values():
    print(i)
print("\n")
#GROUP E
Group_E ={}
i=0
while(True):
    if(i==0):
        m= random.choice(red_teams)
        y= re.search(".\(",m)
        Group_E[m[y.start()+1:]]= m[:y.start()]
        red_teams.remove(m)
        i+=1
    elif(i<4):
        m = random.choice(l)
        y = re.search(".\(",m)
        if m[y.start()+1:] not in Group_E:
            Group_E[m[y.start()+1:]] = m[:y.start()]
            i+=1
            l.remove(m)
    if(i==4):
        break
print("Group E")
for i in Group_E.values():
    print(i)
print("\n")

#GROUP F
Group_F ={}
i=0
while(True):
    if(i==0):
        m= random.choice(red_teams)
        y= re.search(".\(",m)
        Group_F[m[y.start()+1:]]= m[:y.start()]
        red_teams.remove(m)
        i+=1
    elif(i<4):
        m = random.choice(l)
        y = re.search(".\(",m)
        if m[y.start()+1:] not in Group_F:
            Group_F[m[y.start()+1:]] = m[:y.start()]
            i+=1
            l.remove(m)
    if(i==4):
        break
print("Group F")
for i in Group_F.values():
    print(i)
print("\n")
#GROUP G
Group_G ={}
i=0
while(True):
    if(i==0):
        m= random.choice(red_teams)
        y= re.search(".\(",m)
        Group_G[m[y.start()+1:]]= m[:y.start()]
        red_teams.remove(m)
        i+=1
    elif(i<4):
        m = random.choice(l)
        y = re.search(".\(",m)
        if m[y.start()+1:] not in Group_G:
            Group_G[m[y.start()+1:]] = m[:y.start()]
            i+=1
            l.remove(m)
    if(i==4):
        break
print("Group G")
for i in Group_G.values():
    print(i)
print("\n")

#GROUP H
Group_H ={}
i=0
while(True):
    if(i==0):
        m= random.choice(red_teams)
        y= re.search(".\(",m)
        Group_H[m[y.start()+1:]]= m[:y.start()]
        red_teams.remove(m)
        i+=1
    elif(i<4):
        m = random.choice(l)
        y = re.search(".\(",m)
        if m[y.start()+1:] not in Group_H:
            Group_H[m[y.start()+1:]] = m[:y.start()]
            i+=1
            l.remove(m)
    if(i==4):
        break
print("Group H")
for i in Group_H.values():
    print(i)
