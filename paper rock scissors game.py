import random

print('{  ROCK PAPER SCISSOR GAME  }'.center(70, "-"))

# SCORES:
R, P, S = "ROCK", "PAPER", "SCISSORS"
RPS = [R, P, S]  # kompiuteristvis aris rom aarchios
my_score, comp_score = 0, 0  # qulebi
print('\t\t\t\t\t\t  !!! R U L E S !!! \n     This is "Rock Paper Scissors" game its simple but here are some rules:\n\n    1) input only this three wors or firs letters\n'
      '    2)rounds more than 1, it have no maximum \n    3) HAVE FUN \n\n')
print("[   WHAT'S YOUR NAME   ]".center(70,'-'))
name = str(input(">: ")).upper()


# tamaShi sadamdec iqneba
while True:  # tamaShi sadamdec iqneba
    score = int(input("GAME TO: "))
    if score == 0:
        print("CHOOSE MORE THEN 0  (O_O)")
        continue
    else:
        print(f'GAME TO {score} POINTS')
        print('{     GAME ON, GOOD LUCK    }'.center(70, '-'))
        break

# gardaqmnis input inforacias
while (my_score or comp_score) < score:  # gardaqmnis input inforacias
    for i in range(1):
        my_choise = str(input("MY CHOISE IS: "))
        my_choise = my_choise.upper()
        comp_choise = random.choice(RPS)

        for elementi in my_choise[0]:
            if my_choise[0] == "R":
                my_choise = "ROCK"  # nebismieri sityva romelic iwyeba R-ze
                print(f"{name}S CHOISE --> [  {my_choise}  ] VS [  {comp_choise}  ] <-- COMPUTER CHOISE")
                if my_choise == comp_choise:
                    print("[          DREW          ]".center(70, '='))
                elif comp_choise == P:
                    comp_score += 1
                elif comp_choise == S:
                    my_score += 1

            elif my_choise[0] == "S":
                my_choise = "SCISSORS"  # nebismieri sityva romelic iwyeba S-ze
                print(f"{name}S CHOISE --> [  {my_choise}  ] VS [  {comp_choise}  ] <-- COMPUTER CHOISE")
                if my_choise == comp_choise:
                    print("[          DREW          ]".center(70, '='))
                elif comp_choise == R:
                    comp_score += 1
                elif comp_choise == P:
                    my_score += 1

            elif my_choise[0] == "P":
                my_choise = "PAPER"  # nebismieri sityva romelic iwyeba P-ze
                print(f"{name}S CHOISE --> [  {my_choise}  ] VS [  {comp_choise}  ] <-- COMPUTER CHOISE")
                if my_choise == comp_choise:
                    print("[          DREW          ]".center(70, '='))
                elif comp_choise == S:
                    comp_score += 1
                elif comp_choise == R:
                    my_score += 1
            else:
                print("Hmmm...  O_O")  # add score to compiuter
                continue

            print("[          SCORES          ]".center(70, "="))
            print(f'[   {name} {my_score} : {comp_score} COMPUTER   ]'.center(70, '='))

if my_score == score:
    print('\n\n')
    print("*"*70)
    print(f'WINNER IS {name}'.center(70,"*"))
    print("*"*70)
elif comp_score == score:
    print('\n\n')
    print("*"*70)
    print("[      WINNER IS COMPUTER      ]".center(70,"*"))
    print("*"*70)

print("\n")


print("created by:\t\t\t Joni Sturua")
