from rooms import room
from piece import piece
from player import player
import random


class Runner:
    
    def __init__(self):
        
        self.global_target = []
        self.rooms = {}
        self.main = None 
                
        self.generateRooms()      
        self.player = player(self.rooms["MAIN"], self)        
        
    # manage rooms
    def generateRooms(self):
        
        # Generate main room
        self.main = self.addRoom("MAIN")
        
        # Generate side room test
        self.addRoom("KITCHEN")
        
        # Generate side rooms
        self.addRoom("BATHROOM")
        self.addRoom("LIVING")
                
        # Generate items in side room test
        self.rooms["KITCHEN"].addItem("Microwave", self.main)
        self.rooms["KITCHEN"].addItem("Oven", self.main)
        self.rooms["BATHROOM"].addItem("Handle", self.main, [self.rooms["KITCHEN"].items["Oven"]])

        
    def printStatus(self):
        #print(self.player)
        print("============== ROOMS: ===============")
        for rn, room in self.rooms.items():
            room.printItems()
        
        print("============== PLAYER: ==============")  
        print(self.player)
        self.player.printInventory()
        print("*********************************************************")
    
    
    # add room
    def addRoom(self, name):
        r = room(name)
        self.rooms[name] = r
        return r
    
    # remove room
    def removeRoom(self, name):
        r = self.rooms[name]
        self.rooms[name].removeAllItems()
        del self.rooms[name]
        return r
        
        
    def next(self):

        choice = None
        explore = []
        
        if len(self.player.holding) > 0:
            # lead to where items lead to
            for name, item in self.player.holding.items():
                explore.extend(item.getTargets())
                
            print("You can explore...")
            for r in explore:
                print(r)
            
            while choice == None or choice == self.player.curr:
                choice = random.choice(explore)
            return choice
        
        else:
            print("Looking for items to pick up")
            # if there are still more items to explore
            for rname, r in self.rooms.items():
                for name, item in r.items.items():
                    if item.status == "unused" and item.curr != self.player.curr:
                        explore.append(r)

            if len(explore) > 0:
                print("!!!!!!!!!!!! THERE ARE STILL THINGS TO EXPLORE!!!!!!!!!!")
                
                print("You can explore...")
                for r in explore:
                    print(r)
                
                if self.player.curr != self.main: explore.append(self.main)
                
                while choice == None or choice == self.player.curr:
                    choice = random.choice(explore)
                return choice
            
            else: # no more things to explore
                
                print("No where to run, you are locked in!")
                return self.main
            
            
def runActions():
    
    r = Runner()
    
    r.player.enter("BATHROOM")
    r.player.pickUp("Handle")
    r.printStatus()
    
    r.player.enter("KITCHEN")
    r.player.pickUp("Oven")
    
    r.printStatus() # Handle should not direct to KITCHEN here
    
    # Need to test drop as well as if it adds back to target when dropped
    r.player.drop("Oven")
    r.printStatus() # Handle should direct to KITCHEN here
    
    r.player.pickUp("Oven")
    
    r.player.enter("MAIN")
    r.player.use("Oven")
    r.player.use("Handle")
    
    r.printStatus()
    
def runNext():
    
    r = Runner()
    
    print("The choice is: ", r.next())
    
    r.player.enter("KITCHEN")
    print("The choice is: ", r.next())    
    
    r.player.enter("BATHROOM")
    print("The choice is: ", r.next())
    
    r.player.pickUp("Handle")
    print("The choice is: ", r.next())
    
    r.player.enter("KITCHEN")
    r.player.pickUp("Oven")
    print("The choice is: ", r.next())
    
    r.player.enter("MAIN")
    r.player.use("Oven")
    r.player.use("Handle")
    print("The choice is: ", r.next())
    
    r.printStatus()
    
    

if __name__ == "__main__":
    
    print("Hello, World")
    
    #runActions()
    
    runNext()
    
    # NEED TO TEST USE ONE BUT NOT USE OTHER
