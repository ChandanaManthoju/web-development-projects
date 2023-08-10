questions=[["what is my fav color?","blue","black","red","green",1],["what is my favourite hobby?","music","dance","reading","walking",0],["what is my grade in ssc?",9.0,8.0,8.3,9.5,2],["who is my friend forever?","prani","teja","shravya","ammu",2],["what is the best feel of life?","happiness","sucess","failure","process to success",3],["what will be urself foever?","you","money","sucess","people",0],["what is achievement in life?","be independent","settled life","getting to know about yourself","achieving respect from others",0],["who supports you and plays an important role in your future?","friens","relatives","teachers","parents",3],["what is my main goal present?","to do ms in abroad","to commit marriage","clear all subjects in btech","to get placed at good company",3],["how do u enjoy urself at alone time?","cooking","listening music","watching movies","speaking to some one",1],["what u like about yourself?","doing my things done without bothering about others","ignoring unwanted","without depending on others","handle everything alone",0],["what u dilike about urself?","giving importance","getting angry","depending too much","worrying alot about future","getting tensed for small matters",1],["what is ur favourite climate?","cloudy","sunny","windy","rainy",0],["what is your favourite food?","ice cream","panipuri","noodles","chocolates",2]]
print(len(questions))
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,500000,750000,1000000]
money=0
for i in range(0,len(questions)):
  question= questions[i]
  print(f"{questions[i][0]} for rs.{levels[i]}")
  print(f"0.{questions[i][1]}      1.{questions[i][2]}")
  print(f"2.{questions[i][3]}      3.{questions[i][4]}")
  reply=int(input("enter your answer(1-4)="))
  if(reply==question[-1]):
    print(f"correct answer,you have won rs.{levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
     money = 10000
    elif(i == 14):
     money=1000000
  else:
   print("wrong answer!")
   break
print(f"your take home money is{money}")