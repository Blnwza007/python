Gryffindor = 0 
Ravenclaw = 0 
Hufflepuff = 0 
Slytherin = 0
print("Q1) Do you like Dawn or Dusk?")
print("1)Dawn" , "\n2)Dusk")
q1 = int(input("Enter you answer q1 (1 or 2):"))

if q1 == 1:
  Gryffindor +=1
  Ravenclaw +=1
  print("\nGryffindor + 1 =",Gryffindor," \nRavenclaw + 1 =",Ravenclaw)
elif q1 == 2:
  Hufflepuff +=1
  Slytherin +=1
  print("\nHufflepuff + 1 =",Hufflepuff," \nSlytherin + 1 =",Slytherin)
else:
  print("Wrong input")

print("\nQ2) When I’m dead, I want people to remember me as:")
print("1) The Good" , "\n2) The Great" , "\n3) The Wise" , "\n4) The Bold")
q2 = int(input("Enter you answer q2 (1,2,3,4):"))

if q2 == 1:
  Hufflepuff +=2
  print("\nHufflepuff + 2 = " , Hufflepuff)
elif q2 == 2:
  Slytherin +=2
  print("\nSlytherin + 2 =",Slytherin)
elif q2 == 3:
  Ravenclaw +=2
  print("\nRavenclaw + 2 =",Ravenclaw)
elif q2 == 4:
  Gryffindor +=2
  print("\nGryffindor + 2 =",Gryffindor)
else:
  print("Wrong input")

print("\nQ3) Which kind of instrument most pleases your ear?")
print("\n1) The violin","\n2) The trumpet","\n3) The piano","\n4) The drum")
q3 = int(input("Enter you answer q3 (1,2,3,4):"))

if q3 == 1:
  Slytherin +=4
  print("\nSlytherin + 4 =",Slytherin)
elif q3 == 2:
  Hufflepuff +=4
  print("\nHufflepuff + 4 =",Hufflepuff)
elif q3 == 3:
  Ravenclaw +=4
  print("\nRavenclaw + 4 =",Ravenclaw)
elif q3 == 4:
  Gryffindor +=4
  print("\nGryffindor + 4 =",Gryffindor)
else:
  print("Wrong input")
  
houses = {
    "Gryffindor": Gryffindor,
    "Ravenclaw": Ravenclaw,
    "Hufflepuff": Hufflepuff,
    "Slytherin": Slytherin
}
winner = max(houses, key=houses.get)
print("\n🏆 You belong in:", winner, "🏆")
print("Most points:")
for house, score in houses.items():
    print(house, ":", score)


