import random
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
          return Falses
        elif you=='g':
            return True
        elif comp=='w':
            if you=='g':
                return False
            elif you=='s':
                return True
        elif you=='g':
            if you=='s':
                return False
            elif you=='s':
                return True

print('comp trun: Snake(s)Water(w)or Gan(g)?')
randomNo=random.randint(1,3)
if randomNo==1:
    comp='s'
elif randomNo==2:
    comp='w'
elif randomNo==3:
    comp='g'

you=input("your turn :Snake(s) Water(w)or Gun(g)?")  
a=gameWin(comp,you) 
if a==None:
    print("the game is a tie")         
elif a:
    print("you win")
else :
    print("you loss")        