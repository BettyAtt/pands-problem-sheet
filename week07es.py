# This program reads in a file MobyDick.txt
# and outputs the combined numbers of lower and upper case e's.
# Utilises The Gutenberg Press Etext of Moby Dick
# by Herman Melville. Chapter 1 - epilogue included 
# in calculations. 
# Text from: https://www.gutenberg.org/files/2701/old/moby10b.txt

# Author: Betty Attwood

# get the user to enter the file
#  to count the frequency of the letter e in the text
txtfile = str(input("Insert .txt File Name: "))
# read in the file
with open (txtfile, "r") as f:
    data = f.read()
    freq = data.count("e") #first count for lowercase e
    freq2 = data.count("E") # then count for upper case E
    combo=int(freq + freq2) # creat variable adding the int frequencies together
    print("The combined number of uppercase and lowercase e's in Moby Dick: ", combo)
# answer 114114 for "e"; answer 906 for "E" (total is 115020)