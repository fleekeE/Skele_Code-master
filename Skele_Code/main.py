# This is a starter for a text based game in python.
# fill it in and tell a story that would be fun to play

from expand import *
# I use multiple modules as an example for you to try and replicate to keep your
# story neat and get used to using them

# Basic control flow is what this file mostly deals with and the end goal is
# to let others use it. Try to make your code so it doesn’t break easily.


def main():
   # end story is the variable I will use to end the program.
   endStory = 2
   # The while loop will keep repeating until the break of set by endStory is
   # triggered
   while(endStory > 1):
       # terminal prints can be over multiple lines using """ print """ format,
       # instead of the regular  "print" give it a try
       print("""Lets begin!
            Do you know what 2+2 is?""")
       # this is how your story can take input and read it back out
       userInput = input("""Is it:
                        69
                        37
                        64
                        4""")
       print("Your response was: ", userInput)
       # notice input can output to terminal. Look up the input function for python
       # to see why.

       # there are many ways to break this and you should try to write code that
       # catches common cases and check the user for options other than what
       # asked for.
       if(userInput == "4"):
           print("""!Correct!
                ..Decision Internallized into Expand..""")
           moduleReturns = newFunction(userInput)

# This ends the story

       elif(userInput == "69"):
           print("Is this your confession to being 13 :|")
       elif(userInput == "37"):
           print("Nice try..I guess?")
       elif(userInput == "64"):
           print("Where in this equation do you see 4x4..Should I contact someone?")

           print("Nice try, choose an listed option buster!")


# Remove this and try to run your code to try and understand what it does so
# if you write a main module and its not working you can tell why.
if __name__ == '__main__':
    main()
