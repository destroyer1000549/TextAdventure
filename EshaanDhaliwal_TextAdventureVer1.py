#Loading Function
def loading():
  print("Loading...")
#Time Import
import time

loading()
time.sleep(5)
#5 Second Delay after loading function

#Asking Whether they want to play
answer = input("Do you want to play? (yes/no)")

if answer.lower().strip() == "yes":
  #Setting the Scene
  answer = input("You have been sent on a mission to rescue lost files from the Horizon Space Station. Your spaceship has been sent to the Horizon, which recently went communications dark due to unknown reasons, to find and retrive the missing documents. As your ship approaches the Horizon, out of nowhere, a piece of debris hits your spaceship, destroying the engines. Luckily, you are still able to dock on the Horizon. As you exit the airlock, you see two long hallways. They go out in two directions, left and right. Which direction do you go? (left/right)")
  if answer == "left":
    #first decision: running or staying
    answer = input("As you go down the hallway, you hear something unexpected. Someone is running from something. Do you run with them or stay? (run/stay)")
    if answer == "run":
      #2nd decision: hiding from alien in the vents or in locker
       answer = input("As you retreat, you see something black following you. It's about 9 to 10 feet tall, and looks like a bloodthirsty alien. Do you jump into a vent or into a locker? (vent/locker)")
       if answer == "vent":
         #3rd decision: going deeper into vents or going back outside
          answer = input("You survived, and the alien ran past you, but you can either go further into the vent system, or go outside of the vent system (outside/deeper)")
          if answer == "outside":
            #4th decision: Looking through boxes or continuing down hallway
             answer = input("As get out of the vents and walk back down the hall, you see a large room. There are boxes scattered everywhere. Do you look through the boxes or turn and make a right turn and follow the hallway? (right/boxes)")
             if answer == "boxes":
                answer = input("As you look through the boxes you find some C4 and a pistol. Once you find the weapons, you hear something. It's the alien. You see some kind of door on the ground that leads down to some kind of ventilation system and quickly hop in. The alien saw you go in, and follows you. Do you try to shoot the alien with your pistol, or use the C4 and detonate it when the alien comes down into the ventilation system (pistol/c4")
                #5th decision: Using the pistol or c4 to attack the alien
                if answer.lower().strip() == "c4":
                  print("You place the c4 on the ground and wait for the alien to come down. It bashes through the roof of the ventilation system, and jumps down. You quickly detonate the c4, and the alien explodes, sending its body into pieces. At the same time, you opened a hole in the station. Detonating the C4 opened a hole into space. You and the dead alien are sucked into the void.")
                elif answer == "pistol":
                  print("You shoot the alien with the pistol, but it does next to nothing. The alien picks you up and kills you.")
              #Branching Decision if player chooses to go right down hallway: Choosing between two rooms
             elif answer == "right":
               answer = input("Once you reach the end of the hallway, there are two rooms, each blocked off with a large metal door, that you can't see through. There is a button to open each door, but you only have time to open one and see what is inside, otherwise the alien could catch up to you. (1/2)")
               #Finding the control room and the documents option
               if answer.strip() == "2":
                answer == input("Fortunately for you, this is the control room of the horizon, so the documents were probably stored here. You open a cabinet and look through files until you find the documents. There is an escape pod connected to the control room, allowing you to escape the alien. You eject with the escape pod, and radio for assistance. Mission Completed.")
               #Going into the armor room option
               elif answer.strip() == "1":
                 answer = input("You walk into the room and see lots of sets of some kind of armor. You also see some kind of superpowered space laser. You put on the armor just in case, and as you are almost done, you hear something coming to you. Do you attack it with the laser weapon or run? (attack/run)")
                  #Choosing whether to attack or run from the alien and whether to leave or stay in station if alien is killed
                 if answer == "attack":
                    answer = input("It turns out that it was the alien that you had been running from earlier. You blast the alien with the laser and kill it. You can now either leave the ship using the last escape pod you can see, or keep looking for the documents. (look/leave)")
                    #Choosing whether to go back through hallway after killing alien or looking in other room
                    if answer == "look":
                       answer = input("Do you want to go into the other room that you saw earlier, or go back down the hallway you came from? (hallway/room)")
                       #Deciding whether to power on the station or look for documents
                       if answer == "room":
                          answer = input("You push the button to open the door to the room, and it appears to be some kind of command room. Do you try to power the space station on, or look through the cabinets in the room for the documents? (on/documents)")
                          if answer == "documents":
                             print("You look through some cabinets until you find something that appears to be the missing documents. There is one escape pod left on the ship, and you enter it and detach from the station. Mission completed.")                         
                          #If you decide to power on the station
                          elif answer == "on":
                            print("Once you press the button, you hear some kind of powering on sound. After about 10 seconds it stops. It's dead silent. All of a sudden, you hear a huge bang. Warning signals start flashing. 'Reactor Meltdown,' they say. With no other option, you jump into an escape pod and detach from the ship. You watch as the entire Horizon Space Station is engulfed in a massive explosion.")
                       #If you decide to go down the hallway instead of look through the other room
                       elif answer == "hallway":
                         print("You walk back down the hallway, but as you make it to the large room, you feel the ground shaking. You remember that you are on a space station, and look outside. You see that you have been caught in the gravitational pull of a black hole. As you approach the event horizon, you wonder what could be on the other side.")
                    #If you decide to leave the station instead of staying
                    elif answer == "leave":
                       print("You enter the escape pod and pull away from the Horizon. Unfortunately you weren't able to complete your mission and find the document.")
                        
                        
                        
                    


                  #If you decide to run from alien when you have armor
                 elif answer == "run":
                   print("The armor you were wearing was really heavy, and it turns out the alien was faster than you with it on. He catches up to you and eats you alive.")
                 
          #If you decide to go deeper into vent system
          elif answer == "deeper":
            print("The only thing that was in the vent system was small chute that led to an airlock with an escape pod. There was nothing else in the vents, and you leave the space station in the escape pod.")
       #If you decide to hide in locker
       elif answer == "locker":
         print("Unfortunately, the locker has some small openings along the upper part of the locker, and the alien smells you through them. The alien bashes the locker open, and kills you.")
      
    #If you decide to stay instead of running from alien   
    elif answer == "stay":
        print("It turns out what the person was running from was an alien. The alien catches you and kills you.")
        
    
  #If you go to the right hallway during the first decision
  elif answer == "right":
    print("This hallway was a dead end. Unlucky")









































































































