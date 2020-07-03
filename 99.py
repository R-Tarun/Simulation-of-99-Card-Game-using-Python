# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:43:24 2019

@author: TARUN RAMPATI
"""
import random
import time
f={"Ace":11,"2":2,"3":3,"4":-111,"5":5,"6":6,"7":7,"8":8,"9":0,"10":-10,"Jack":-100,"Queen":10,"King":-99}
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def size(self):
         return len(self.items)


class Card:
    def __init__(self,face,suit):
        self.suit=suit
        self.face=face
    def __repr__(self):
        return self.face+ " of "+ self.suit
    def getsuit(self):
        return self.suit
    def getface(self):
        return self.face
    
    
class Deck:
    def __init__(self):
        self.cards=[]
    def create(self):
        cards=[]
        suits=["Spades","Hearts","Clubs","Diamonds"]
        faces=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        for suit in suits:                 
            for face in faces:
                cards.append( Card(face, suit) )
        self.cards=cards
    def shuffle(self):
        self.a=random.randint(100,500)
        for i in range(0,self.a):
            r1=random.randint(0,self.a)%52
            r2=random.randint(0,self.a)%52
            self.cards[r1],self.cards[r2]=self.cards[r2],self.cards[r1]
        

class Player:
    def __init__(self,name):
        self.card=[]
        self.name=name
        self.coins=3
        self.b=Card("","")
        self.l=[]
        self.r=[]
    def draw(self,a):
        self.l.clear()
        self.r.clear()
        self.b=a.pop()
        for i in self.card:
            c=i.getface()
            self.l.append(f.get(c))
            self.r.append(f.get(c))
        c=self.b.getface()
        self.l.append(f.get(c))
        self.r.append(f.get(c))
        self.l.sort()
        self.l.reverse()
        return self.l
    
    def hand(self,s):
        if (s<=99):
           k=[]
           flag=0;
           for i in self.l:
               if (i>0 and i+s<99):
                   flag=1
                   k.append(i)
               else:
                   if (i!=-10 and i<=0):
                       o=self.r.index(i)
                       if (o<=2):
                           self.b,self.card[o]=self.card[o],self.b
                           break
                   else:
                       if(i==-10):
                           o=self.r.index(i)
                           if (o<=2):
                               self.b,self.card[o]=self.card[o],self.b
                               break
           if (flag==1):
               m=min(k)
               o=self.r.index(m)
               if (o<=2):
                   self.b,self.card[o]=self.card[o],self.b
               
        else:
            for i in self.l:
                k=[]
                if (i<0 and i!=-11):
                   k.append(i) 
                   m=max(k)
                   o=self.r.index(m)
                   if (o<=2):
                       self.b,self.card[o]=self.card[o],self.b
                       break
        return self.b
d=Deck()
c=Deck()
d.create()
c.create() 
d.shuffle()
c.shuffle()
s=Stack()
t=random.randint(0,600)
w=random.randint(0,600)
for i in range(0,200):
    r1=random.randint(0,t)%52
    r2=random.randint(0,w)%52
    c.cards[r1],d.cards[r2]=d.cards[r2],c.cards[r1] 
for i in range(0,52):
    s.push(d.cards[i])
    s.push(c.cards[i])
print("DECK after SHUFFLING........")
for i in range(0,104):
    print(s.items[i])
    print("\n")
players=[]
for i in range(0,6):
    players.append(Player("player"+str(i)))

for i in range(0,18):
    j=i%6;
    players[j].card.append(s.pop())



def cal(a,sum):
    m=[11,3,2,7,4,8,5,0,6,1]
    flg=0
    if (a>=0 and sum+a<=99):
        if (a==11):
            if (sum+11<=99):
                sum+=11
                flg=1
            else:
                if(sum+1<=99):
                    sum+=1
                    flg=1
        else:
            sum+=a
            flg=1
    elif(a<0):
        if (a==-99):
            sum=99
            flg=1
        elif (a==-10):
            sum+=a
            flg=1
        elif (a==-100):
            if(sum>99 and sum<110):
                sum-=10
                flg=1
            elif(sum>=110):
                sum=99
                flg=1
            elif(sum==99):
                flg=1
            elif(sum<99):
                for i in m:
                    if(i+sum<=99):
                        flg=1
                        sum+=i
                        break
    g=[]
    g.append(flg)
    g.append(sum)
    return g
p=0
r=[]

while(True):
    r.clear()
    for i in players:
        if (not (s.isEmpty())):
            print("\n\n")
            print("-------------------------------------------------------------")
            print(i.name," is playing....")
            time.sleep(1)
            i.draw(s)
            print(i.name," have cards",i.card)
            time.sleep(1)
            print(i.name," drew ",i.b," from the deck")
            k=i.hand(p)
            time.sleep(1)
            print(i.name," dropped ",k)
            if (k.getface()=="4"):
                players.reverse()
                print(i.name," have cards after dropping",i.card)
                print("Total is ",p)
                break
            print(i.name," have cards after dropping",i.card)
            c=cal(f.get(k.getface()),p)
            p=c[1]
            print("Total is ",p)
        if (c[0]==0):
            r.append(i)
            print("--------------------------------------")
            print(i.name," lose the game")
    for i in r:
        players.remove(i)
    if(len(players)<=1):
        i=players[0]
        print("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(i.name," won the game")
        print("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        break
         




            