import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
#Numbers are based on ASCII
upper1=chr(random.randint(65,90))
upper2=chr(random.randint(65,90))
lower1=chr(random.randint(97,122))
lower2=chr(random.randint(97,122))
dig1=chr(random.randint(48,57))
dig2=chr(random.randint(48,57))
specChar1=chr(random.randint(32,47))
specChar2=chr(random.randint(65,90))


#Generate password using all the characters, in random order
password = [upper1 , specChar1, dig1 +  lower1 , specChar2 , upper1 , upper2 , dig1 , dig2 , specChar1 , specChar2]
password = shuffle(password)

#Ouput
print(password)
