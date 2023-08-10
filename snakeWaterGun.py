#SNAKE WATER GUN
import random
def check(comp,user):
  valid = {0,1,2}
  if user not in valid:
    raise ValueError("random must be one of %r." % valid)
  if comp==user:
    return 0
  if(comp==0 and user==1):
    return -1
  if(comp==1 and user==2):
    return -1
  if(comp==2 and user==0):
    return -1
  return 1
  valid = {0,1,2}
  if user not in valid:
    raise ValueError("random must be one of %r." % valid)
comp=random.randint(0,2) 
for i in range(10):
  user = int(input("0 for snake,1 for water,2 for gun\n"))
  print("only 0,1,2 numbers are accepted")
  score= check(comp,user)
  print("you:", user)
  print("computer:",comp)
  if(score==0):
    print("its a draw")
  elif score==-1:
    print("you loss")
  else:
   print("you won")

  