import time
print("--------------------------------------------------")
print('SELAMAT DATANG KE KUIZ TEKA TOKOH SUKAN MALAYSIA !')
answer = input('Adakah anda bersedia untuk bermain? (ya/tidak): ')
time.sleep(1)
print("--------------------------------------------------")
score = 0
#Chances
chances=1
print("You have to pick", chances,"correct answer.\nYou will get 1 score if you pick a correct answer.\n")
time.sleep(2)
#print('SELAMAT DATANG KE KUIZ TEKA TOKOH SUKAN MALAYSIA !')
#answer = input('Adakah anda bersedia untuk bermain? (ya/tidak): ')

if answer.lower() == 'ya':
    score = 3
    total_questions = 3

    q1 = input('Soalan 1: SIAPAKAH TOKOH BADMINTON NEGARA ? ')
    if q1.lower() == 'Datuk lee chong wei':
        score = +1
        #break
    else:
        #print("INCORRECT!\n")
        #score -= 1
        print("THE CORRECT ANSWER IS", 'Datuk lee chong wei', "\n\n")
    scoreq1=score
#time.sleep(2)

    q2 = input('Soalan 2: SIAPAKAH TOKOH BASIKAL NEGARA? ')
    if q2.lower() == 'Azizulhasni':
        score = +1
        #break
    else:
        #print("INCORRECT!\n")
        #score -= 1
        print("THE CORRECT ANSWER IS", 'Azizulhasni', "\n\n")
    scoreq2=score
#time.sleep(2)

    q3 = input('Soalan 3: SIAPAKAH TOKOH SKUASY NEGARA? ')
    if q3.lower() == 'Datuk nicol an':
        score = +1
        #break
    else:
        #print("INCORRECT!\n")
       #score -= 1
        print("THE CORRECT ANSWER IS",'Datuk nicol an', "\n\n")
    scoreq3=score
#time.sleep(2)

    print(f'Terima kasih kerana bermain! markah anda {score} out of {total_questions} questions correct.')
    print(f'Marks obtained: {score / total_questions * 100:.1f}%')
else:
    print('Okay, maybe next time!')