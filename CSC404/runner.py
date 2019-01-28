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
        
        choice = -1
        explore = 0
        
        # if there are still more items to explore
        for r in self.rooms:
            if len(r.hold) > 0:
                explore = 1
                break
            
        if explore == 0: return choice
        
        while choice == -1 or choice == self.curr:
            choice = random.choice(self.global_target) if len(self.global_target) > 0 else random.randint(0, len(self.rooms))
        
        return choice


if __name__ == "__main__":
    
    print("Hello, World")
    
    r = Runner()
    
    r.player.enter("BATHROOM")
    r.player.pickUp("Handle")
    r.printStatus()
    
    r.player.enter("KITCHEN")
    r.player.pickUp("Oven")
    
    r.player.holding["Handle"].poll()
    r.printStatus()
    
    r.player.enter("MAIN")
    r.player.use("Oven")
    r.player.use("Handle")
    
    # Need to test drop as well as if it adds back to target when dropped