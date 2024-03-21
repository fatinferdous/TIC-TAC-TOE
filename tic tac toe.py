def prbo( xst , yst):
    #1
    if(xst[1]):
         x1 = "X"
    elif(yst[1]):
         x1 = "0"
    else:
         x1 = 1
     #2
    if(xst[2]):
         x2 = "X"
    elif(yst[2]):
         x2 = "0"
    else:
         x2 = 2
     #3
    if(xst[3]):
         x3 = "X"
    elif(yst[3]):
         x3 = "0"
    else:
         x3 = 3
     #4
    if(xst[4]):
         x4 = "X"
    elif(yst[4]):
         x4 = "0"
    else:
         x4 = 4 
     #5
    if(xst[5]):
         x5 = "X"
    elif(yst[5]):
         x5 = "0"
    else:
         x5 = 5 
     #6
    if(xst[6]):
         x6 = "X"
    elif(yst[6]):
         x6 = "0"
    else:
         x6 = 6 
     #7
    if(xst[7]):
         x7 = "X"
    elif(yst[7]):
         x7 = "0"
    else:
         x7 = 7 
     #8
    if(xst[8]):
         x8 = "X"
    elif(yst[8]):
         x8 = "0"
    else:
         x8 = 8 
     #9
    if(xst[9]):
         x9 = "X"
    elif(yst[9]):
         x9 = "0"
    else:
         x9 = 9 
                                                                  
    print(f"{x1} | {x2} | {x3}")
    print("--|---|--")
    print(f"{x4} | {x5} | {x6}")
    print("--|---|--")
    print(f"{x7} | {x8} | {x9}")

xst = [0,0,0,0,0,0,0,0,0,0]
yst = [0,0,0,0,0,0,0,0,0,0] 
turn = 1

def sum(a,b,c):
     return a+b+c

def cwin(xst,yst):
     win = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
     for w in win:
          if(sum(xst[w[0]],xst[w[1]],xst[w[2]]) == 3):
               print("X won the match")
               return 1
          if(sum(yst[w[0]],yst[w[1]],yst[w[2]]) == 3):
               print("0 won the match")
               return 0
     return -1
    
print("Wellcome to fatin tic tac toe Game")
print("It's two player game")
r = input("If you want to play then write yes : ")


while True :
    if(r != "yes"):
         break
    prbo(xst,yst)
    if( turn == 1):
          my = int(input("it is X turn : "))
          xst[my] = 1
    else:
          your = int(input("it is 0 turn : "))
          yst[your] = 1
    turn = 1 - turn
    p = cwin(xst,yst)
    if(p == 1 or p == 0):
         
         break
         
