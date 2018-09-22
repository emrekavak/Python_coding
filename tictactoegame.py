# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:38:29 2018

@author: EMRE KAVAK / TİC - TOC - TOE GAME / GTU COMPUTER ENGINEERING
"""
# önceki hesaplanmıs deney bilgileri
rate = 82.68 # dogruluk oranı
reaction = 20 # tepkime adım sayısı

def checkKat(inp): # katelizor check
    if inp == 'A' or inp == 'B' or inp == 'C':
        return True
    else:
        return False
    
def checkEnz(enz): # enzim check
    if not enz :
        return True
    if enz == 'X' or enz == 'Y' or enz == 'Z' or enz == 'T' or enz == 'V' or enz == 'U' or enz == 'K' or enz == 'L'or enz == 'M':
        return True
    else:
        return False
    
def checkTrueInputs(kat,enz): # check katalizor ve enzim birlikte dogru girilmis mi (olusturulan kurallara gore)
    if kat == 'A':
        if enz == 'U' or enz == 'K' or enz == 'L' or enz == 'M':
            return False
        else:
            return True
    if kat == 'B':
        if not enz:
            return True
        else:
            return False
    if kat == 'C':
        if enz == 'X' or enz =='M':
            return False
        else :
            return True
        
def calculate(kat,enz): # maliyet, dogruluk yüzdesi ve tepkime adım sayısı hesaplayan kısım
    global reaction
    global rate
    cost = 0
    if kat == 'A':
        if not enz:
            reaction -= 5
            rate -= 12.57
            cost = reaction * 36 + 95
        if enz == 'X' or enz == 'Y' or enz == 'Z':
            reaction -= 7
            rate -= 18.54
            cost = reaction * 36 + 110
        if enz == 'T' or enz == 'V':
            reaction += 3
            rate -= 7.68
            cost = reaction * 36 + 110            
    if kat == 'B':
        if not enz:
            reaction -= 3
            rate -= 11.54
            cost = reaction * 36 + 106
    if kat == 'C':
        if not enz:
            reaction -= 4
            rate -= 16.4402
            cost = reaction * 36 + 109
        if enz == 'V':
            reaction += 1
            rate -= 13.624
            cost = reaction * 36 +124
        if enz == 'Y' or enz == 'Z' or enz == 'K' or enz == 'L': 
            reaction += 2
            rate += 6.554
            cost = reaction * 36 + 124
        if enz == 'U' or enz == 'T':
            reaction -=9
            rate -=22.0
            cost = reaction * 36 + 124
    return cost
                          
print("BASF Kimya Fabrikası Bilişim Çözümleri X5620F Kodlu Deney Simülasyonuna Hoşgeldiniz.")    
check = False
while(check == False):
    kat = input("Katalizör tercihi yapınız >")
    if checkKat(kat) != True :
        print("Yanlış katalizör isimi girdiniz. Lütfen doğru giriniz.")
        check = False
    else:
        check = True

check = False
while(check == False):
    enz = input("Enzim tercihi yapınız >")
    if checkEnz(enz) == False  or checkTrueInputs(kat,enz) == False:
        print("Yanlış Enzim isimi girdiniz. Lütfen doğru giriniz. ")
    else:
        result = calculate(kat,enz)
        print("Deney bilgileri:")
        print("Toplam tepkime sayısı:",reaction)
        print("Doğruluk değeri:%.2f"%rate,"%")
        print("Toplam Maliyet:%.3f"%result)
        if rate >= 55:
            print("Sonuç:Piyasaya sürülebilir.")
        else :
            print("Sonuç:Piyasaya sürülemez.")
        check = True