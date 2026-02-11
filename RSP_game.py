import random

card = {'가위':0, '바위':1, '보':2}
card_str = list(card.keys())
score_str = ['플레이어', '컴퓨터', '플레이 횟수']
score = [0,0,0]

play = True

def battle():
    global play
    if user=='END':
        scoreboards = dict(zip(score_str,score))
        print(scoreboards)
        play=False

    else:
        score[2] += 1
        user_card = card[user]
        if com_card-user_card==-1 or com_card-user_card==2:
            print(f'플레이어: {user}, 컴퓨터: {card_str[com_card]}')
            print('플레이어가 이겼습니다!')
            score[0] += 1
        elif com_card-user_card==0:
            print('비겼습니다')
        else:
            print(f'플레이어: {user}, 컴퓨터: {card_str[com_card]}')
            print('컴퓨터가 이겼습니다!')
            score[1] += 1

while play:
    user = input('가위,바위,보! (끝내기는 END): ')
    com_card = random.randint(0,2)
    battle()