print("Let's play a game!")
print("Answer only with yes or no. Please do not use capitilization.")
apple = input("You find an apple. pick it up?")
if apple == "yes":
    print("You pick up an apple.")
else:
  print("You ignore the apple and carry on.")
print("You pass a long river to your right.\n A forest of pine trees appear at your left.")
fr = input("You walk over to the river, a fish jumps out and bites you. It's teeth are caught on your jeans. Leave it there?")
if fr == "yes":
  print("You leave the fish hanging on your jeans.")
else:
  print("You remove the fish from your jeans and throw it back into the water. It leaves a small bite mark on your leg.")
fw = input("You make your way to the pine forest. Walking through the trees, you see a snake on the ground. you almost stood on it! The snake looks irritated. Leave it alone and contine?")
if fw == "yes":
  print("You leave the snake alone and walk away.")
else:
  print("You stomp the snake to death so it dosnt bite you. Leaving the dead snake behind, a wild cat sneaks from the bush to feast on its remains.")
time.sleep(5)
print("After a few minutes you reach the other side of the pines. A big city looms ahead, you make your way over the rough landscape towards the city.")
eb = input("You feel thirsty, a bar isnt too far away. Enter?")
if eb == "yes":
  print("You open the door, it creaks as you close it behind you. A group of older men are singing along terribly to a song. You make your way to the counter and order a beer. After you pay, \n you walk over to an empty table and sit down to drink your beer. When you finish, \n you exit the bar and ponder of where to go next.")
else:
  print("You decide to skip the bar and sit down on a bench.")
