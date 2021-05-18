def game():
    return 44677

score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()
    
if hiScoreStr=='':          #if highscore file value is 0 or null then it will change to the value of score=game() value
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score :   #elseif the highscore value is less than the score value then it will replace with the score value
    with open("hiscore.txt", "w") as f:
        f.write(str(score))