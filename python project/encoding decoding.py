# SECRET CODING LANGUAGE -TRANSLATE NORMAL ENGLISH INTO SECRET CODING LANGUAGE
# HARRY
# ABCARRYHABC
#IF IT IS CODING THEN WORD CONTAINS ATLEAST THREE CHARACTERS,REMOVE THE FIRST LETTER AND APPEND IT IN THE END NOW APPEND THREE RANDOM CHARACTERS AT THE START AND END ELSE: SIMPLY REVERSE THE STRING
# IF IT IS DECODING IF THE WORD CONTAINS LESS THAN 3 CHARACTERS,REVERSE IT ELSE REMOVE 3 RANDOM CHARACTERS FROM START AND END.NOW REMOVE THE LAST LETTER AND APPEND IT IN THE START

s=input("enter your message")
w=s.split(" ")
coding=input("1 for coding and 2 for decoding")
coding=True if(coding=="1") else False
print(coding)
if(coding):
  w1=[]
  for word in w:
    if(len(word)>=3):
      r1="abc"
      r2="xyz"
      s1=r1+word[1:]+word[0]+r2
      w1.append(s1)
    else:  
      w1.append(word[::-1]) #it is one of the method to reverse a string
  print(" ".join(w1))
 #decoding  abchandhucxyz abcadbxyz abcirlgxyz
else:
  w1=[]
  for word in w:
    if(len(word)>=3):
      s1=word[3:-3]
      s1=s1[-1]+ s1[:-1]
      w1.append(s1)
    else:
      w1.append(word[::-1])
  print(" ".join(w1))
    