#!/usr/bin/env python3
#Python Project
import os  #To clear screen using os.system('cls')
print("Hey !")
print("Up for something?")
print("How about learning something new?")
print("Well how about Sudoku")
choice=input("(Y/N)")
if ((choice=="N") or (choice=="n") or (choice=="No") or (choice=="NO") or (choice=="no")):
    exit()  
print("Brave Choice!")
temp_variable=os.system('clear')
sudoku="""
         +++++++++++++++++++++++++++++++++++++++
         | 6 |   |   [] 3 | 2 |   [] 4 |   | 7 |
	 +---+---+---++---+---+---++---+---+---+
         |   | 3 |   []   |   | 4 []   | 8 |   |
	 +---+---+---++---+---+---++---+---+---+
	 | 4 |   |   []   |   | 6 []   |   |   |
         +++++++++++++++++++++++++++++++++++++++
         |   | 2 | 7 []   | 3 |   []   |   | 9 |
	 +---+---+---++---+---+---++---+---+---+
         | 3 |   |   [] 8 |   | 7 []   |   | 1 |
	 +---+---+---++---+---+---++---+---+---+
	 | 8 |   |   []   | 1 |   [] 5 | 7 |   |
	 +++++++++++++++++++++++++++++++++++++++
         |   |   |   [] 6 |   |   []   |   | 8 |
	 +---+---+---++---+---+---++---+---+---+
         |   | 8 |   [] 2 |   |   []   | 1 |   |
	 +---+---+---++---+---+---++---+---+---+
	 | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	 +++++++++++++++++++++++++++++++++++++++

"""
print(sudoku)
print("""
         So that's how a typical Sudoku looks like (Thats an easy level)
         How can I say that ?
         Well, We will soon find out""") 
input("Press any key to continue : ")
temp_variable=os.system("clear")
print("""
         The rules for sudoku are:

	 1) No number repeats in any row , any column , or any box !
	 2) Each Box should have all numbers from 1 to 9
	 3) Each line should have all number from 1 to 9

         That's It!
	 Rest is brain game!
	 So lets see what these rules looks like when we apply it!""")
input("Press any key to continue : ")
temp_variable=os.system("clear")
print("""
        The 4th ,5th and 6th rows in this example seem to be eligible for
	filling up :
         (You will hone this art with time , it isn't that difficult
	  just see where you can start filling , without going against the
	  rules )

         +++++++++++++++++++++++++++++++++++++++
         |   | 2 | 7 []   | 3 |   []   |   | 9 |
	 +---+---+---++---+---+---++---+---+---+
         | 3 |   |   [] 8 |   | 7 []   |   | 1 |
	 +---+---+---++---+---+---++---+---+---+
	 | 8 |   |   []   | 1 |   [] 5 | 7 |   |
	 +++++++++++++++++++++++++++++++++++++++

     Seen, anything yet?
     Dont worry if you didn't !
     A good idea is to start by 1 and then go on like 1,2,3,4... and so on """)
input("Press any key to continue: ")
temp_variable=os.system("clear")
print("""
         +++++++++++++++++++++++++++++++++++++++
         |(*)| 2 | 7 []   | 3 |   []   |   | 9 |
	 +---+---+---++---+---+---++---+---+---+
         | 3 |   |   [] 8 |   | 7 []   |   | 1 |
	 +---+---+---++---+---+---++---+---+---+
	 | 8 |   |   []   | 1 |   [] 5 | 7 |   |
	 +++++++++++++++++++++++++++++++++++++++

     See the postition marked with (*) , this place is eligible for a number to
     be filled . """)
number=input("Can you guess which one ? (Enter the number): ")
     if number==1 :
         print("Congratulations! You are right ! ")
     else 
         print("Oops! You are wrong ,the answer was 1, but don't worry ")
print(" So , lets see how the answer is one . ")
input("Press any key to continue : ")
temp_variable=os.system("clear")
print("""
         +++++++++++++++++++++++++++++++++++++++
         |(1)| 2 | 7 []   | 3 |   []   |   | 9 |
	 +---+---+---++---+---+---++---+---+---+
         | 3 |   |   [] 8 |   | 7 []   |   | 1 |
	 +---+---+---++---+---+---++---+---+---+
	 | 8 |   |   []   | 1 |   [] 5 | 7 |   |
	 +++++++++++++++++++++++++++++++++++++++

    (I will be entering each new number found in a () paranthesis )
         if you focus the first BOX (the 3x3 square) and wish to find
         a number that fits in this box , lets say 1 , then we see where 
	 else does 1 appear near it , in any other box.
	 Here , 1 does appear in the second and the third box
	 and that too in 2nd and 3rd rows.
	""")
input("Press any key to continue: ")
temp_variable=os.system("clear")
print("""
         +++++++++++++++++++++++++++++++++++++++
         |   | 2 | 7 []   | 3 |   []   |   | 9 |
	 +---+---+---++---+---+---++---+---+---+
         | 3 |   |   [] 8 |   | 7 []   |   | 1 |
	 +---+---+---++---+---+---++---+---+---+
	 | 8 |   |   []   | 1 |   [] 5 | 7 |   |
	 +++++++++++++++++++++++++++++++++++++++

So let's mark the boxes that go invalid for the position of 1 in the 1st box(3x3) with 'x' """)
input("Press any key to continue: ")
temp_variable=os.system("clear")
print("""
         +++++++++++++++++++++++++++++++++++++++
         |   | 2 | 7 []   | 3 |   []   |   | 9 |
	 +---+---+---++---+---+---++---+---+---+
         | 3 | x | x [] 8 |   | 7 []   |   | 1 |
	 +---+---+---++---+---+---++---+---+---+
	 | 8 | x | x []   | 1 |   [] 5 | 7 |   |
	 +++++++++++++++++++++++++++++++++++++++

   The 1st and 2nd rows go invalid since in these rows 1 already occured .
   Now as is Visible We got only 1 box left as valid for the number 1 in
   box 1.
   And since all numbers should appear in a box once 
   we hence know that 1 has to be in first row first column
   (The other two boxes are already invalid since they already have 1 once
    in them)
   So , we can be sure of position of 1 in the 1st box , and that's because
   of the 2nd and 3rd boxes only ! )
   Hence , that position goes to 1 ! 
   Now lets see how the whole sudoku looks like :""")
input("Press any key to continue : ")
temp_variable=os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 |   [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   |   []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           |(1)| 2 | 7 []   | 3 |   []   |   | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 |   | 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   []   | 1 |   [] 5 | 7 |   |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   |   []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
print("So , lets see which another one is eligible for filling ")
print("Now , we'll consider whole sudoku , and slowly and gradually we'll fill the complete grid ")
input("Press any key to continue: ")
temp_variable=os.system("clear")
print("""
       It might be a bit difficult in the start , but slowly you WILL learn
       how to find a number.
       What I do , is to , go from 1-9 in that order determining which one
       to be filled next
       like in the sudoku we'll see in the next page , We will first see 
       if we can find more '1's and if not then we'll proceed to 2 , then
       3 and so on...
      """) 
input("Press any key to continue")
temp_variable=os.system("clear")
print("""
        Now , try and find out if more '1's can be filled up.
	Analyse Box wise, it might be helpful.
	It wont be too lengthy as you have to check validity of '1' number
	in each box .
	Discard it immediately , if it already has one.
	else see for '1's in the all the boxes near the one you chose.
	Let's call the box you chose as HAPPY
	if HAPPY doesn't have '1' in it's own 3x3 box , then , 
        see for boxes near it that .
	see for boxes whose rows or columns run into HAPPY ,
	ONLY ROWS AND COLUMNS
	no diagnals
	If any row from nearby boxes run into HAPPY , with a 1 in them
	then discard the 1x1 boxes that come in that row .
	Then try and zero in to one box left as a possibility.
	If you see more 1x1 boxes as a possibility then leave that box for now.
	Those might prove little difficult if you are a beginner.
	Play with them after you've cleared the basics! 
	Good luck with the grid on the next screen! """)
input("Press any key to continue: ")
temp_variable=os.system("clear")
print(sudoku)
print("Once you find out ... ")
input("Press any key to continue: ")
while True
     choice=input("Did you find it ? (y/n) ")
     if ( choice=='y' or choice=='Y' )
        print("Congratulations! ")
	break
     else
        print("Don't worry, try again! \n If you're fed up or don't want to")
	print("try again , press y ")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 |   [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   |   []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 []   | 3 |   []   |   | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 |   | 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   []   | 1 |   [] 5 | 7 |   |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   |(*)[]   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""


     



       


    
 
