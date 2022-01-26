#Loading Function
def loading():
  print("Loading...")
#Time Import
import time

loading()
time.sleep(5)
#5 Second Delay after loading function
#The functions are defined in reverse of the actual order in the story due to python not being able to call a function before it has been defined
#Sorry for the long number of lines, when I was converting my code into functions it became longer than before, and taking out parts of my story would make it not make sense.
#I also only commented on every line of code in the first function, due to the other functions being more or less the same thing as the first but with slight variation

#Function with outcomes for whether player turns ship on or searches for documents
def FindOrPower():
    answer = input("You push the button to open the door to the room, and it appears to be some kind of command room. Do you try to power the space station on, or look through the cabinets in the room for the documents? (on/documents)")
    if answer.lower().strip() == "documents":
        print("You look through some cabinets until you find something that appears to be the missing documents. There is one escape pod left on the ship, and you enter it and detach from the station. Mission completed.")
    if answer.lower().strip() == "on":
        print("Once you press the button, you hear some kind of powering on sound. After about 10 seconds it stops. It's dead silent. All of a sudden, you hear a huge bang. Warning signals start flashing. 'Reactor Meltdown,' they say. With no other option, you jump into an escape pod and detach from the ship. You watch as the entire Horizon Space Station is engulfed in a massive explosion.")
#Function asking whether the player wants to to enter the other room or go back down the hall
def HallwayOrRoom():
    answer = input("Do you want to go into the other room that you saw earlier, or go back down the hallway you came from? (hallway/room)")
    if answer.lower().strip() == "room":
        FindOrPower()
    if answer.lower().strip() == "hallway":
        print("You walk back down the hallway, but as you make it to the large room, you feel the ground shaking. You remember that you are on a space station, and look outside. You see that you have been caught in the gravitational pull of a black hole. As you approach the event horizon, you wonder what could be on the other side.")
#Function asking whether player wants to continue looking for documents or leave the ship
def LookOrLeave():
    answer = input("It turns out that it was the alien that you had been running from earlier. You blast the alien with the laser and kill it. You can now either leave the ship using the last escape pod you can see, or keep looking for the documents. (look/leave)")
    if answer.lower().strip() == "look":
        HallwayOrRoom()
    if answer.lower().strip() == "leave":
        print("You enter the escape pod and pull away from the Horizon. Unfortunately you weren't able to complete your mission and find the document.")
#Function for whether player chooses to enter room 2
def Room2():
    print("Fortunately for you, this is the control room of the horizon, so the documents were probably stored here. You open a cabinet and look through files until you find the documents. There is an escape pod connected to the control room, allowing you to escape the alien. You eject with the escape pod, and radio for assistance. Mission Completed.")
#Function for if player chooses to enter room 1
def Room1():
    answer = input("You walk into the room and see lots of sets of some kind of armor. You also see some kind of superpowered space laser. You put on the armor just in case, and as you are almost done, you hear something coming to you. Do you attack it with the laser weapon or run? (attack/run)")
    if answer.lower().strip() == "attack":
        LookOrLeave()
    if answer.lower().strip() == "run":
        print("The armor you were wearing was really heavy, and it turns out the alien was faster than you with it on. He catches up to you and eats you alive.")
#Function asking which room the player will go in
def TwoRooms():
    answer = input("Once you reach the end of the hallway, there are two rooms, each blocked off with a large metal door, that you can't see through. There is a button to open each door, but you only have time to open one and see what is inside, otherwise the alien could catch up to you. (1/2)")
    if answer.lower().strip() == "1":
        Room1()
    if answer.lower().strip() == "2":
        Room2()
#Function for if the player attacks the alien with explosives
def C4():
    print("You place the c4 on the ground and wait for the alien to come down. It bashes through the roof of the ventilation system, and jumps down. You quickly detonate the c4, and the alien explodes, sending its body into pieces. At the same time, you opened a hole in the station. Detonating the C4 opened a hole into space. You and the dead alien are sucked into the void.")
#Outcome if player attacks alien with pistol
def Pistol():
    print("You shoot the alien with the pistol, but it does next to nothing. The alien picks you up and kills you.")\
#Function asking player what to attack alien with
def PistolAndC4():
    answer = input("As you look through the boxes you find some C4 and a pistol. Once you find the weapons, you hear something. It's the alien. You see some kind of door on the ground that leads down to some kind of ventilation system and quickly hop in. The alien saw you go in, and follows you. Do you try to shoot the alien with your pistol, or use the C4 and detonate it when the alien comes down into the ventilation system (pistol/c4)")
    if answer.lower().strip() == "c4":
        C4()
    if answer.lower().strip() == "pistol":
        Pistol()
#Function asking the player whether to continue down hallway or search boxes
def SearchOrHallway():
    answer = input("As get out of the vents and walk back down the hall, you see a large room. There are boxes scattered everywhere. Do you look through the boxes or turn and make a right turn and follow the hallway? (right/boxes)")
    if answer.lower().strip() == "boxes":
        PistolAndC4()
    if answer.lower().strip() == "right":
        TwoRooms()
#Function asking where player wants to go after hiding in the vent system
def Vent():
    answer = input("You survived, and the alien ran past you, but you can either go further into the vent system, or go outside of the vent system (outside/deeper)")
    if answer.lower().strip() == "outside":
        SearchOrHallway()
    if answer.lower().strip() == "deeper":
        print("The only thing that was in the vent system was small chute that led to an airlock with an escape pod. There was nothing else in the vents, and you decide to leave the space station in the escape pod in fear of the alien coming back.")        
#Function asking where the player will hide from the alien
def Hide():
    answer = input("As you retreat, you see something black following you. It's about 9 to 10 feet tall, and looks like a bloodthirsty alien. Do you jump into a vent or into a locker? (vent/locker)")
    if answer.lower().strip() == "vent":
        Vent()
    if answer.lower().strip() == "locker":
        print("Unfortunately, the locker has some small openings along the upper part of the locker, and the alien smells you through them. The alien bashes the locker open, and kills you.")
#Function asking player whether to run or stay from unknown entity
def RunOrStay():
    answer = input("As you go down the hallway, you hear something unexpected. Someone is running from something. Do you run with them or stay? (run/stay)")
    if answer.lower().strip() == "run":
        Hide()
    if answer.lower().strip() == "stay":
        print("It turns out what the person was running from was an alien. The alien catches you and kills you.")
#Function setting the scene
def Scene():
    answer = input("You have been sent on a mission to rescue lost files from the Horizon Space Station. Your spaceship has been sent to the Horizon, which recently went communications dark due to unknown reasons, to find and retrive the missing documents. As your ship approaches the Horizon, out of nowhere, a piece of debris hits your spaceship, destroying the engines. Luckily, you are still able to dock on the Horizon. As you exit the airlock, you see two long hallways. They go out in two directions, left and right. Which direction do you go? (left/right)")
    if answer.lower().strip() == "left":
        RunOrStay()
    if answer.lower().strip() == "right":
        print("The hallway was unfortunately a dead end.")
#First Function asking whether play wants to play
def DoYouWantToPlay():
#Line prompting the player to say yes/no to start game
    answer = input("Do you want to play? (yes/no)")
#Outcome for if player answers yes
    if answer.lower().strip() == "yes":
#Calling of next function
        Scene()
#Outcome if player answers no
    if answer.lower().strip() == "no":
        print("Ok, if you don't want to play, you can watch this video in the meantime: https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#Calling first function
DoYouWantToPlay()



                    
        









    
    
