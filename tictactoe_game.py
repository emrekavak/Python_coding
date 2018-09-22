# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 11:07:18 2018

@author: EMRE KAVAK / TİC - TOC - TOE GAME / GTU COMPUTER ENGINEERING
"""
def printArr(arr):
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()
        
def usersInput(arr): # player1 ve player2 sırasıyla ınput alınan kısım
    print(">>> TURN PLAYER1")
    if getRowAndColumn(arr,'X') == True: 
        print("PLAYER1 (X) is WİNNER!!!")
        return True
    if checkBoardFull(arr) == True:
        print("!!! There isn't an WİNNER.")
        return True
    print(">>> TURN PLAYER2")
    if getRowAndColumn(arr,'O') == True:
        print("PLAYER2 (O) is WİNNER!!!")
        return True
    if checkBoardFull(arr) == True:
        print("!!! There isn't an WİNNER.")
        return True
    return False   

def getRowAndColumn(arr,user): # kullanıcıdan row ve column ınputlarının alındıgı kısım
    check = False
    while(check == False):
        try: # true  input kontrolu (ornegın harf veya sembol gırmısse )
            row = int(input(">>> ROW :"))
            if row < 1 or row > 3:
                print("Wrong row number. Please select between ( 1-2-3 )")
            else :
                check = True
        except ValueError:
            print("Wrong row number. Please select between ( 1-2-3 )")
  
    check = False
    while(check == False):
        try: # true  input kontrolu (ornegın harf veya sembol gırmısse )
            col = int(input(">>> COLUMN :"))
            if col < 1 or col > 3:
                print("Wrong column number. Please select between ( 1-2-3 )")
            else :
                check = True 
        except ValueError: # fırlatılan exception u yakalayan kısım
            print("Wrong column number. Please select between ( 1-2-3 )")
            
    if changeBoard(arr,col-1,row-1,user) != True:
        print("!!! You selected wrong cell. Please Try Again.")
        printArr(arr)
        getRowAndColumn(arr,user) # eger dogru cell (dolu cell secılmısse ) secılmemısse, recursive olarak fonksiyon tekrar cagırılıyor
    if checkWinner(arr,user) == True: # kazanan kontorlu oyuncular row ve column girdikten hemen sonra yapılıyor
        return True
    else :
        return False
     
def changeBoard(arr,x,y,user):
    if arr[x][y] == '.': # secılen kısım bos ıse degıstırcek
        arr[x][y] = user
        printArr(arr) 
        return True
    else:
        printArr(arr) 
        return False

def checkWinner(arr,user): # kazanma durumu kontrolu
    for i in range(0,3):
        count = 0
        for j in range(0,3):
            if arr[i][j] == user:
                count+=1
                if count == 3:
                    return True
    for i in range(0,3):
        count2 = 0
        for j in range(0,3):
            if arr[j][i] == user:
                count2+=1
                if count2 == 3:
                    return True
    return False
    
def checkBoardFull(arr): # oyun boardının dolulugunu kontrol ediyor
    count = 0
    for k in range(0,3):
        for l in range(0,3):
            if arr[k][l] != '.':
                count +=1
    if count == 9 :
        return True
    else:
        return False

arr =[['.','.','.'],['.','.','.'],['.','.','.']] # 3*3 ARRAY
printArr(arr) # first board print
check = False
while(check == False): # oyunun devamlılıgını saglayan dongu
    check = usersInput(arr) # player1 ve player2 ınputs