text=input("Enter your text here: ")
choice= input("Enter 1 to uppercase or 2 to lowercase: ")
if(int(choice)==1):
    print(text.upper())
if(int(choice)==2):
    print(text.lower())
if (int(choice)!=1 and int(choice)!=2):
    print("Sorry, you have made a wrong choice!, Better luck next time")
   
