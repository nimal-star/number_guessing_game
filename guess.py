
import random,string

def game():
    value1=random.choices(string.ascii_lowercase + string.digits,k=4)
    a="".join(value1)
    return a
print(game())
def game1(hiddencode,guess):
     correct=0
     for i in range(4):
          if guess[i] ==hiddencode[i]:
               correct+=1
     return correct
def playgame():
     secretcode =game()
     list1=[]
     uniquecode=set()
     attempts=0

     while True:
        guesses=input("enter your guess:")
        valid= True
        if len(guesses)!=4:
             valid=False
        else:
            for i in guesses:
                 if i not in (string.ascii_lowercase + string.digits):
                      valid=False
                      break
        if not  valid:
               print("invalid special characters")
               continue
        attempts+=1
        list1.append(secretcode)
        uniquecode.add(guesses)

        game12=game1( secretcode,guesses)
        print(f"{game12} characters correct in position")

        # Check if code is cracked
        if game12 == 4:
            print(f"Code cracked in {attempts} tries! Code type: {type(secretcode)}")
            if attempts <= 3:
                print(f"Master Codebreaker! Unique guesses: {uniquecode}")
            break   
playgame() 
        
