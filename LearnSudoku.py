#!/usr/bin/env python3
#Python Project
#No input for number towards the end
#No variable storing the result of os.system("clear")
#No : in the else statements
import os  #To clear screen using os.system("clear")
print("Hey !")
print("Up for something?")
print("How about learning something new?")
print("Well how about Sudoku")
choice = input("(Y/N) : ")
if ((choice=="N") or (choice=="n") or (choice=="No") or (choice=="NO") or (choice=="no")) :
    exit()  
print("Brave Choice!")
temp_variable = os.system('clear')
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
temp_variable = os.system("clear")
print("""
         The rules for sudoku are:

	 1) No number repeats in any row , any column , or any box !
	 2) Each Box should have all numbers from 1 to 9
	 3) Each line should have all number from 1 to 9

         That's It!
	 Rest is brain game!
	 So lets see what these rules looks like when we apply it!""")
input("Press any key to continue : ")
temp_variable = os.system("clear")
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
temp_variable = os.system("clear")
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
number = input("Can you guess which one ? (Enter the number): ")
if number==1 :
    print("Congratulations! You are right ! ")
else : 
    print("Oops! You are wrong ,the answer was 1, but don't worry ")
print(" So , lets see how the answer is one . ")
input("Press any key to continue : ")
temp_variable = os.system("clear")
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
temp_variable = os.system("clear")
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
temp_variable = os.system("clear")
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
temp_variable = os.system("clear")
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
temp_variable = os.system("clear")
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
temp_variable = os.system("clear")
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
temp_variable = os.system("clear")
print(sudoku)
print("Once you find out ... ")
input("Press any key to continue: ")
while True :
    choice = input("Did you find it ? (y/n) ") 
    if ( choice=='y' or choice=='Y' ) :
        print("Congratulations! ")
        break
    else :
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
input("Press any key to continue: ")
temp_variable = os.system("clear")
print("So, the answer was 7th row 6th column (*) ")
print(sudoku)
print("This one was bit tougher than the previous one as it involved seeing the sudoku as a whole ")
print("So, lets narrow down how we concluded this position ")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | @ | x [] 3 | 2 |   [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           | x | 3 | x []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 | @ | x []   |   | 6 []   |   |   |
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
print("""
         Now , the 1st 3x3 box is not having a one already, so it should be a 
         viable candidate. But look , there are more than one possibility for 1 
	 (The ones' marked with '@')
      """)  
print(sudoku)
print("(Also notice the 'x' marks the positions not valid for '1' since it has already appeared in the same row)")
print("Same goes for the next 2 boxes of 3x3")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 |   [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   |   []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
       --> | 1 | 2 | 7 []   | 3 |   []   |   | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 |   | 7 []   |   | 1 | <--
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   []-->| 1 |<--[] 5 | 7 |   |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   |(*)[]   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

print(sudoku)
print("""
       Now , as the arrow shows , '1' are already present in the 2nd set of 3x3 boxes 
       so no '1's again , since the rule says :
       "No number should repear in a row , column or a box"
      """)
input("Press any key to continue: ")
temp_variable = os.system("clear")
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
           |   | 8 |   [] 2 |   |   []-->| 1 |<--|
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |-->| 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++

"""
print(sudoku)
print("""
          Now , for the 3rd set ,again the arrow shows the places where '1's are not possible
	  But look carefully , the middle box in the 3rd set , is perfect !
      """)
input("Press any key to continue")
temp_variable = os.system("clear")
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
           |   |   |   [] 6 | x |   []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 | x | x []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 [] x | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

print(sudoku)
print("""
         It , might be visible now, that there is only one box left!
	 And , that is because the places marked with 'x' already had 1 in
	 either their row or their columns .
	 So, the Only box left must have the 1 !
	 Also, since each 3x3 must have all numbers from 1 to 9
	 We can be more sure that the place belongs to none other than
	 '1' ! So here goes our second find .""")
input("Press any key to continue: ")
temp_variable = os.system("clear")
print("Answer: ")
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
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
input("Press any key to continue: ")
temp_variable = os.system("clear")
print("""
         Now , we must proceed to 2 , as their are no obvious places where '1'
	 seems to fit.
	 Do remember , that which ever box you choose to fill a certain number
	 keep in mind not to go over it again until you are satisfied that no other
	 boxes fits the desired number.
	 And , do not forget to check all the boxes !
	 If you are confused about how to proceed so as to not miss anything,
	 then you can try what I do.
	 try all the 3x3 boxes in the order you read .
	 That is , 1st set left to right ,
	 then 2nd set left to right,
	 and then , 3rd one left to right.
	 If you wish to follow this manner , you can 
	 1) continue to play and fill the complete grid.
	 2) solve this on a paper and then check the answer
	 3) quit

	 """)
answer = """ 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 | 9 [] 3 | 2 | 8 [] 4 | 5 | 7 |
	   +---+---+---++---+---+---++---+---+---+
           | 5 | 3 | 2 [] 1 | 7 | 4 [](9)| 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 | 7 | 8 [] 5 | 9 | 6 [] 1 | 3 | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

while True :
   try :
        choice = int(input("Enter your choice: "))
   except ValueError:
        print('Please enter correct choice')
        continue
   if choice==2 :
      print("Answer: ")
      print(answer)
      input("Press any key to continue: ")
      temp_variable = os.system("clear")
      exit()
   elif choice==3 :
      exit()
   elif choice!=1 :
      print("Please Enter correct input .")
   if choice == 1 :
        break

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
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

print("""
        From now on  enter row number , column number as in example shown , I'll show an 
	example by solving for the first '2' 
	The row and column should be entered as shown below , just press enter for this time:
	""")
print(sudoku)
ask_place="Enter the row and column in r,c format or 'none' if no possible occurance :"
input(ask_place+"6,6")
print("Correct! Filling it up.")
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
	   | 8 |   |   []   | 1 |(2)[] 5 | 7 |   |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

print(sudoku)

while True:
    try:
        choice = int(input("Enter the 2 if you found another '2', or press n to jump to next number if no more 2 present or press e to exit ") )
    except ValueError :
        print("Please Enter correct choice ")
        continue
    if choice==2:
        print("Oops! No more visible 2 ,as either more than one possibilities present or the number already present in the row or column or box, lets jump to next number ")
        break
    elif choice=="n":
        print("Correct! , No more 2 visible. Jumping to next number: 3")
        break
    elif choice=="e":
        exit()

input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
print("Now we search for 3")
place=input(ask_place)
if place=="6,9" :
   print("Correct! Filling up the 3")
else :
   print("Oops! This is possibly wrong, wanna try again? ")
   place=input(ask_place)
   if place=="6,9" :
      print("Yups This one is right!")
   else :
      print("Nopes, lets see now what was the answer")
input("Press any key to continue: ")
temp_variable = os.system("clear")
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
	   | 8 |   |   []   | 1 | 2 [] 5 | 7 |(3)|
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""   
print(sudoku)
print("Got it ? Pretty easy one , only one box left if you see the third box in the second set . The 3 from the left two boxes cancel out ")
print("the 4th and 5th rows and hence we're left with only one place to fill!")

while True:
    try:
        choice = int(input("Enter the 3 if you found another '3', or press n to jump to next number if no more 3 present or press e to exit ") )
    except ValueError :
        print('Please enter correct choice')
        continue
    if choice==3:
        print("Oops! No more visible 3 , as either more than one possibilities present or the number already present in the row or column or box, lets jump to next number ")
        break
    elif choice=="n":
        print("Correct! , No more 3 visible. Jumping to next number: 4")
        break
    elif choice=="e":
        exit()

input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
print("Now we search for 4")
place = input(ask_place)
if place == "none" :
   print("Correct! Proceeding to 5")
else :
   print("Oops! This is possibly wrong, wanna try again? ")
   place = input(ask_place)
   if place=="none" :
      print("Yups This one is right!")
   else :
      print("Nopes, This time there is no visible 4")
input("Press any key to continue: ")
temp_variable = os.system("clear")
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
	   | 8 |   |   []   | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 
print(sudoku)
print("Now we search for 5")
place=input(ask_place)
if place == "none" :
   print("Correct! Proceeding to 6")
else :
   print("Oops! This is possibly wrong, wanna try again? ")
   place=input(ask_place)
   if place == "none" :
      print("Yups This one is right!")
   else :
      print("Nopes, This time there is no visible 5")
input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
print("Now we search for 6")
place=input(ask_place)
if place=="5,5" :
   print("Correct! Filling up the 6")
else :
   print("Oops! This is possibly wrong, wanna try again? ")
   place=input(ask_place)
   if place=="5,5" :
      print("Yups This one is right!")
   else :
      print("Nopes, lets see now what was the answer")
input("Press any key to see the answer: ")
print("This time it was the fifth row and 5th column i.e 5,5 ")
input("Press any key to continue: ")
temp_variable = os.system("clear")
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
           | 3 |   |   [] 8 |(6)| 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   []   | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 
print(sudoku)
print("Now we search for 6")
place = input(ask_place)
if place=="none" :
   print("Correct! ")
else :
   print("Oops! This is possibly wrong, wanna try again? ")
   place=input(ask_place)
   if place == "none" :
      print("Yups This one is right!")
   else :
      print("Nopes, This time there is no visible 6")
input("Press any key to continue: ")
temp_variable = os.system("clear")
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
           | 3 |   |   [] 8 | 6 | 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   []   | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 
print(sudoku)
print("Now we search for 7")
place = input(ask_place)
if place == "none" :
   print("Correct! Proceeding to 8")
else :
   print("Oops! This is possibly wrong, wanna try again? ")
   place = input(ask_place)
   if place == "none" :
      print("Yups This one is right!")
   else :
      print("Nopes, This time there is no visible 7")
input("Press any key to continue: ")
temp_variable = os.system("clear")
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
           | 3 |   |   [] 8 | 6 | 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   []   | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 
print(sudoku)
print("Now we search for 8")
place = input(ask_place)
if place=="1,6" :
   print("Correct! ")
else :
   print("Oops! This is possibly wrong, wanna try again? ")
   place=input(ask_place)
   if place=="1,6" :
      print("Yups This one is right!")
   else :
      print("Nopes, This time it is at :")
input("Press any key to continue: ")
print("Position: 1,6")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 |(8)[] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   |   []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 []   | 3 |   []   |   | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   []   | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 
print(sudoku)
print("Again we search for 8")
place=input(ask_place)
if place == "4,7" :
   print("Correct! ")
else :
   print("Oops! This is possibly wrong, wanna try again? ")
   place = input(ask_place)
   if place == "4,7" :
      print("Yups This one is right!")
   else :
      print("Nopes, This time it is at :")
input("Press any key to continue: ")
print("Position: 4,7")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   |   []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 []   | 3 |   [](8)|   | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   []   | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 
print(sudoku)
print("Again we search for 8")
print("Checking for a number again is helpful at the end of checking all 1-9 once , but if you get faster at checking, check for that number again quickly, and you might find out that the number you've filled recently helpout in filling the number in a previously questionable position")
place = input(ask_place)
if place=="3,3" :
   print("Correct! ")
elif place == "none" :
   print("See carefully , the '8' you filled at 1,6 . It helps find a new '8' at a previously checked position")
else :
   print("Oops! This is possibly wrong, wanna try again? ")
   place = input(ask_place)
   if place=="3,3" :
      print("Yups This one is right!")
   else :
      print("Nopes, This time it is at :")
input("Press any key to continue: ")
print("Position: 3,3")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   |(8)[]   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 []   | 3 |   [] 8 |   | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   []   | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 
print(sudoku)
print("Now we search for 9")
place = input(ask_place)
if place=="6,4" :
   print("Correct! ")
else :
   print("Oops! This is possibly wrong, wanna try again? ")
   place = input(ask_place)
   if place=="6,4" :
      print("Yups This one is right!")
   else : 
      print("Nopes, This time it is at :")
input("Press any key to continue: ")
print("Position: 6,4")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 []   | 3 |   [] 8 |   | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   [](9)| 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 
print(sudoku)
print("""
       Okay , so now we go a little faster and I'll ask you which number is visible.
       Remember to answer in ascending order .
       For example, if 2 and 5 both are visible , enter 2 first and then proceed similarly.
      """)
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 []   | 3 |   [] 8 |   | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 
print(sudoku)
number = input("Enter the first number from 1-9 visible to you: ")
if number=="4" :
    print("Correct! Filling it up")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number=="4" :
       print("Correct! Filling it up")
    else :
       print("Oops , that might be wrong. This time answer was 4.")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [](4)| 3 |   [] 8 |   | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 
print(sudoku)
print("""
       A word of advice: 
       If you find a box with all the numbers filled except one.
       That is, if you see that a box has eight numbers filled and
       only one place is vacant , then hurry and fill that one vacant
       box.Since a 3x3 box in sudoku must have all numbers filled from 1-9.
       
       Now enter a number that you find can be filled as described in above situation.""")
number = input("Enter the number: ")
if number == "5" :
    print("Exactly!")
else :
    print("Okay, let's see in the solution what the correct answer is")
input("Press any key to continue: ")
print("The answer was 5 in the 2nd box in 2nd set that is 4,6 one")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 |(5)[] 8 |   | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 
print(sudoku)
input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
number = input("Enter the first number from 1-9 visible to you: ")
if number=="6" :
    print("Correct! Filling it up")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number=="6" :
       print("Correct! Filling it up")
    else :
       print("Oops , that might be wrong. This time answer was 6.")
input("Press any key to continue: ")
print("The answer was 6 in 4,8 ")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 |(6)| 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 []   |   | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 

print(sudoku)
number = input("Enter the first number from 1-9 visible to you: ")
if number=="4" :
    print("Correct! Filling it up")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number=="4" :
       print("Correct! Filling it up")
    else :
       print("Oops , that might be wrong. This time answer was 4.")
input("Press any key to continue: ")
print("The answer was 4 in 5,8 ")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 []   |(4)| 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
""" 
print(sudoku)
print("Alert: Keep in mind the word of advice!")
number = input("Enter the first number from 1-9 visible to you or the number with highest priority: ")
if number == "2" :
    print("Correct! Filling it up")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you or one with the highest priority: ")
    if number=="2" :
       print("Correct! Filling it up")
    else :
       print("Oops , that might be wrong. This time answer was 2.")
input("Press any key to continue: ")
print("The answer was 2 in 5,7 ")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku = """ 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [](2)| 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
number = input("Enter the first number from 1-9 visible to you: ")
if number=="4" :
    print("Correct! Filling it up")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number=="4" :
       print("Correct! Filling it up")
    else :
       print("Oops , that might be wrong. This time answer was 4.")
input("Press any key to continue: ")
print("The answer was 4 in 8,9 ")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |   | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 |(4)|
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
number = input("Enter the first number from 1-9 visible to you: ")
if number=="4" :
    print("Correct! Filling it up")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number=="4" :
       print("Correct! Filling it up")
    else :
       print("Oops , that might be wrong. This time answer was 4.")
input("Press any key to continue: ")
print("The answer was 4 in 7,5 ")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku = """ 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 |(4)| 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |   | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
number = input("Enter the first number from 1-9 visible to you: ")
if number=="4" :
    print("Correct! Filling it up")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number=="4" :
       print("Correct! Filling it up")
    else :
       print("Oops , that might be wrong. This time answer was 4.")
input("Press any key to continue: ")
print("The answer was 4 in 9,2 ")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku = """ 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |   [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 |(4)| 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
number = input("Enter the first number from 1-9 visible to you: ")
if number == "4" :
    print("Correct! Filling it up")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number=="4" :
       print("Correct! Filling it up")
    else :
       print("Oops , that might be wrong. This time answer was 4.")
input("Press any key to continue: ")
print("The answer was 4 in 6,3 ")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku = """ 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |   |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   |(4)[] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print("You Might have already noticed that if you get 2-3 occurences of the same number then the number becomes easier to find and eventually we might end up completing that number in the grid. Like we have done with 4. It's completed in the grid")
print(sudoku)
print("Now let's change the strategy a bit ")
input("Press any key to continue: ")
temp_variable = os.system("clear")
print("Now we'd try out another strategy, checking of rows and columns individualy")
print("This is a good technique and might come in handy at times when number is not easily apparent")
print("So , we'd go checking row wise , for each row I'd suggest check from numbers as we did previously , that is , first check for '1' in row 1 then for '2' in row 2 and upto 9 in row 1")
print("Then proceed to the second row and follow the same procedure")
input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
number = input("Enter the first number from 1-9 visible to you in the first row: ")
if number == "1" :
    print("Correct! Filling it up")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number=="1" :
       print("Correct! Filling it up")
    else :
       print("Oops , that might be wrong. This time answer was 1.")
input("Press any key to continue: ")
print("The answer was 1 in 1,2 ")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku = """ 
           +++++++++++++++++++++++++++++++++++++++
           | 6 |(1)|   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
print("""
	So lets understand what happened .
	if you see above , in the first row , that is , the one having 6,3,2,8,4,7 already filled in.	     Also , remember that row is the horizontal part , vertical ones are columns.
	Now, in first row we are looking for '1' , first block is already filled in.
	second block ( That has (1) now ) has now '1' in that column.
	But , if we look at other empty blocks , in first row , they all have '1' in there row!
	That means if we keep in mind the rule that a row must have all the numbers from 1-9 ,
	this row then has only one place viable for '1' also , it must be filled with '1' considering        the rule stated above! So, there goes the '1' in 1,2 position, now we'll be doing this repeat        -edly.
     """)
input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
number = input("Enter the first number from 1-9 visible to you in the first row: ")
if number == "none" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number=="none" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time there was no number to be filled in row 1.")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku = """ 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |   | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
print("""
	Though this technique is quite good but not much feasible in this case. See, if you 
	try it in the second and third row the numbers aren't easily visible, but , at times
	this comes in handy. 
	Now , we'd be trying another way of filling , that is ,
	fill the rows or columns that are most filled or almost completely filled already.
	example : in the above one, row no. 6 is quite potential , as it has only one vacany,
	so the rule that each row must have numbers from 1-9 is useful here
	""")

input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
number = input("Enter the first number from 1-9 visible to you in the most filled row or column: ")
if number=="6" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number=="6" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time the number was 6 in row no. 6.")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku = """ 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |   |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 |(6)| 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
choice = input("Hint ? (y/n)")
if choice == "y":
     print("Hint: How about the last , that is 9th column ?")
else:
     print("Happy trying! ")
number = input("Enter the first number from 1-9 visible to you in the most filled row or column: ")
if number == "6" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "6" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time the number was 6 in column no. 9.")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku = """ 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 |(6)|
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |   |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
number = input("Enter the first number from 1-9 visible to you in the most filled row or column: ")
if number == "2" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "2" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time the number was 2 in row no. 6 again! .")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku = """ 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   |(2)|
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
choice = input("Hint ? (y/n)")
if choice == "y":
     print("Hint: How about the 1st row ?")
else :
     print("Happy trying! ")
number = input("Enter the first number from 1-9 visible to you in the most filled row or column: ")
if number == "none" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "none" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time there was no easily visible number in the first row , though it was already highly occupied.")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku = """ 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 []   | 8 | 3 []   |   | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print("Let's try the last , that's 9th , row ")
number = input("Enter the first number from 1-9 visible to you in the most filled row or column: ")
if number == "2" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "2" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '2' in 9th row")
print("""
        Did you see that ! While checking for the last row when we reach the 1st empty block
	to check for '2' , that 3x3 box already has a '2' so , even if the 2 was not in the 
	same column as that of the empty block, but in the same 3x3 box , we still couldn't have
	filled '2' there !
	""")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 []   | 8 | 3 []   |(2)| 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print("Let's try the last , that's 9th , row again ")
number = input("Enter the first number from 1-9 visible to you in the most filled row or column: ")
if number == "6" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "6" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '6' in 9th row")
print("Same logic as previous one!!")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 []   | 8 | 3 [](6)| 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
choice = input("Hint ? This time it's easy though. (y/n)") 
if choice=="y":
     print("Hint: How about the last row ?")
else :
     print("Happy trying! ")
number = input("Enter the first number from 1-9 visible to you in the most filled row or column: ")
if number == "7" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "7" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '7' in last row .")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |   |   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [](7)| 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
print("Let's try other similar way now , that is , instead of finding most filled rows or columns we'll now find most filled 3x3 boxes") 
print("For a beginning let's try out 8th 3x3 box , it has only 2 empty ones and is also much potential")
number = input("Enter the first number from 1-9 visible to you in the most filled 3x3 box: ")
if number == "5" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "5" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '5' in 8,5 .")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 |(5)|   []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
number = input("Enter the first number from 1-9 visible to you in the most filled 3x3 box: ")
if number == "9" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "9" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '9' in 8,6 .")
input("Press any key to continue: ")
temp_variable = os.system("clear")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |   [] 2 | 5 |(9)[]   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print(sudoku)
print("Remember if you dont't find any potential block in most filled 3x3 box , jump to the next most fille one you can find")
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Hint: How about the 7th 3x3 box ?")
else :
     print("Happy trying! ")

number = input("Enter the first number from 1-9 visible to you in the most filled box: ")
if number == "6" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "6" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '6' in 8,3 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |   [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 |(6)[] 2 | 5 | 9 []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
print("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
print("Advice: The 3x3 box you recently filled up or the ones having common rows or column with it are most potential , because , they have common rows and columns hence any change in those will increase your chances of filling up")
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Hint: How about the 7th 3x3 box again?")
else:
     print("Happy trying! ")

number = input("Enter the first number from 1-9 visible to you in the most filled box: ")
if number == "3" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "3" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '3' in 7,3 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |   |   |(3)[] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 | 6 [] 2 | 5 | 9 []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Hint: How about the 7th 3x3 box again?")
else :
     print("Happy trying! ")

number = input("Enter the first number from 1-9 visible to you in the most filled box: ")
if number == "2" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "2" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '2' in 7,1 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           |(2)|   | 3 [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 | 6 [] 2 | 5 | 9 []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Hint: How about the 7th 3x3 box again?")
else:
     print("Happy trying! ")
if number == "5" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "5" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '5' in 7,2 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 |(5)| 3 [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 8 | 6 [] 2 | 5 | 9 []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

input("Press any key to continue: ")
temp_variable = os.system("clear")

print(sudoku)
choice = input("Hint ? (y/n)")
if choice=="y":
     print("This one's easy , just see which box is filled the most.")
else:
     print("Happy trying! ")
if number == "7" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "7" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '7' in 8,1 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           |(7)| 8 | 6 [] 2 | 5 | 9 []   | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
input("Press any key to continue: ")
temp_variable = os.system("clear")


print(sudoku)
print("Remember , the boxes you filled recently , and the ones having common rows or columns with them are more potential")
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Check out the 9th 3x3 box")
else:
     print("Happy trying! ")
if number == "3" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "3" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '3' in 8,7 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 []   |   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [](3)| 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
input("Press any key to continue: ")
temp_variable = os.system("clear")


print(sudoku)
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Check out the 9th 3x3 box again")
else:
     print("Happy trying! ")
if number == "7" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "7" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '7' in 7,7 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [](7)|   | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
input("Press any key to continue: ")
temp_variable = os.system("clear")


print(sudoku)
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Check out the 9th 3x3 box again")
else:
     print("Happy trying! ")
number = input("Enter the number : ")
if number == "9" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "9" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '9' in 7,8 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |   [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 |(9)| 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
input("Press any key to continue: ")
temp_variable = os.system("clear")

print(sudoku)
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Check out the 4th 3x3 box ")
else:
     print("Happy trying! ")
number = input("Enter the number : ")
if number == "5" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "5" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '5' in 5,3 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |   |(5)[] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Check out the 4th 3x3 box again")
else:
     print("Happy trying! ")
number = input("Enter the number : ")
if number == "9" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "9" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '9' in 5,2 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |   []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 |(9)| 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""
input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Check out the 1st 3x3 box ")
else:
     print("Happy trying! ")
number = input("Enter the number : ")
if number == "2" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "2" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '2' in 2,3 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |   | 3 |(2)[]   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Check out the 1st 3x3 box ")
else:
     print("Happy trying! ")
number = input("Enter the number : ")
if number == "5" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "5" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '5' in 2,1 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           |(5)| 3 | 2 []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |   | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Check out the 1st 3x3 box ")
else:
     print("Happy trying! ")
number = input("Enter the number : ")
if number == "7" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "7" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '7' in 3,2 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |   [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           | 5 | 3 | 2 []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 |(7)| 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Check out the 1st 3x3 box ")
else:
     print("Happy trying! ")
number = input("Enter the number : ")
if number == "9" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "9" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '9' in 1,3 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 |(9)[] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           | 5 | 3 | 2 []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 | 7 | 8 []   |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
choice = input("Hint ? (y/n)")
if choice=="y":
     print("Check out the 2nd 3x3 box ")
else:
     print("Happy trying! ")
number = input("Enter the number : ")
if number == "5" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "5" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '5' in 3,4 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 | 9 [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           | 5 | 3 | 2 []   |   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 | 7 | 8 [](5)|   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""


input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
print("As it is already visible , that the grid will soon fill up , you can use any technique now that helps you go fast enough")
choice = input("Hint ? (y/n)") 
if choice=="y":
     print("Check out the 2nd 3x3 box ")
else:
     print("Happy trying! ")
number = input("Enter the number : ")
if number == "1" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "1" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '1' in 2,4 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 | 9 [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           | 5 | 3 | 2 [](1)|   | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 | 7 | 8 [] 5 |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
choice = input("Hint ? (y/n)")
if choice=="y":
     print("Check out the 2nd 3x3 box ")
else:
     print("Happy trying! ")
number = input("Enter the number : ")
if number == "7" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "7" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '7' in 2,5 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 | 9 [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           | 5 | 3 | 2 [] 1 |(7)| 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 | 7 | 8 [] 5 |   | 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
number = input("Enter the number : ")
if number == "9" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "9" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '9' in 3,5 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 | 9 [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           | 5 | 3 | 2 [] 1 | 7 | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 | 7 | 8 [] 5 |(9)| 6 []   |   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
number = input("Enter the number : ")
if number == "1" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "1" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '1' in 3,7 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 | 9 [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           | 5 | 3 | 2 [] 1 | 7 | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 | 7 | 8 [] 5 | 9 | 6 [](1)|   | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""


input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
number = input("Enter the number : ")
if number == "3" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "3" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '3' in 3,8 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 | 9 [] 3 | 2 | 8 [] 4 |   | 7 |
	   +---+---+---++---+---+---++---+---+---+
           | 5 | 3 | 2 [] 1 | 7 | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 | 7 | 8 [] 5 | 9 | 6 [] 1 |(3)| 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
number = input("Enter the number : ")
if number == "5" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "5" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '5' in 1,8 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 | 9 [] 3 | 2 | 8 [] 4 |(5)| 7 |
	   +---+---+---++---+---+---++---+---+---+
           | 5 | 3 | 2 [] 1 | 7 | 4 []   | 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 | 7 | 8 [] 5 | 9 | 6 [] 1 | 3 | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

input("Press any key to continue: ")
temp_variable = os.system("clear")
print(sudoku)
print("Great! You've made it to the last number on the GRID ")
number = input("Enter the number : ")
if number == "9" :
    print("Correct! ")
else :
    print("Oops , that might be wrong. Let's try once more.")
    number = input("Enter the first number from 1-9 visible to you: ")
    if number == "9" :
       print("Correct! ")
    else :
       print("Oops , that might be wrong. This time it was '9' in 1,8 .")
sudoku=""" 
           +++++++++++++++++++++++++++++++++++++++
           | 6 | 1 | 9 [] 3 | 2 | 8 [] 4 | 5 | 7 |
	   +---+---+---++---+---+---++---+---+---+
           | 5 | 3 | 2 [] 1 | 7 | 4 [](9)| 8 | 6 |
	   +---+---+---++---+---+---++---+---+---+
	   | 4 | 7 | 8 [] 5 | 9 | 6 [] 1 | 3 | 2 |
           +++++++++++++++++++++++++++++++++++++++
           | 1 | 2 | 7 [] 4 | 3 | 5 [] 8 | 6 | 9 |
	   +---+---+---++---+---+---++---+---+---+
           | 3 | 9 | 5 [] 8 | 6 | 7 [] 2 | 4 | 1 |
	   +---+---+---++---+---+---++---+---+---+
	   | 8 | 6 | 4 [] 9 | 1 | 2 [] 5 | 7 | 3 |
	   +++++++++++++++++++++++++++++++++++++++
           | 2 | 5 | 3 [] 6 | 4 | 1 [] 7 | 9 | 8 |
	   +---+---+---++---+---+---++---+---+---+
           | 7 | 8 | 6 [] 2 | 5 | 9 [] 3 | 1 | 4 |
	   +---+---+---++---+---+---++---+---+---+
	   | 9 | 4 | 1 [] 7 | 8 | 3 [] 6 | 2 | 5 |
	   +++++++++++++++++++++++++++++++++++++++
"""

print(sudoku)
print("""
	Congratulations! You've completed the sudoku!
	I'm sure you'll love this more if you get to mix the techniques , and
	with some of daily practice you'll surely become commendable.
	Good luck for all the future sudokus !
	""")

