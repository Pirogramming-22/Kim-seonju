#8단계
def brGame():
    num = 0
    players = ['player1', 'player2']
    turn = 0
    
    while(num < 31) :
        player = players[turn%2] #번갈아가면서
        
        while(1):
            cnt = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
            if not cnt.isdigit():
                print("정수를 입력하세요")
                continue
                
            cnt = int(cnt)
            
            if cnt not in [1,2,3] :
                print("1,2,3 중 하나를 입력하세요")
                
            else:
                break

        for i in range(cnt):
            num += 1
            print(f"{player} : {num}")
            if num == 31 :  
                print(f"{player} Win!")  
                break
        
        turn += 1
brGame()
