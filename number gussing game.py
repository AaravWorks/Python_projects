import random
secret = random.randint(1,10)
guess = int(input("Enter the number 1,10"))
if guess == secret:
    print("correct")
else:
    print("you lose")
    print("ye hai",secret)
    
    
    
