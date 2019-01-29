class player:
    
    def __init__(self, main, runner):
        self.curr = main
        self.holding = {}
        self.runner = runner
        
    def __str__(self):
        return "The player (you) is in the {}!".format(self.curr)
    
    def pickUp(self, name):
        if(len(self.holding) < 2):
            self.curr.items[name].status = "holding"
            self.holding[name] = self.curr.items[name]
            return "You picked up {}!".format(name)
        return "Your hands are full!"
    
    def drop(self, name):
        
        self.holding[name].status = "unused"
        
        # change the room that the item is in
        if self.holding[name].curr != self.curr:
            self.holding[name].updateRoom(self.curr)
        
        del self.holding[name]
        
        return "You dropped {} in {}!".format(name, self.curr)
    
    def use(self, name):
        self.holding[name].status = "used"
        
        if self.holding[name].curr != self.curr:
            self.holding[name].updateRoom(self.curr)
        
        
        
        return "You used {} in {}!".format(name, self.curr)
    
    #def pickUpItem(self, name):
        #self.items[name].status = "holding"
        
    #def useItem(self, name):
        #self.items[name].status = "used"    
    
    def enter(self, rname):
        room = self.runner.rooms[rname]
        self.curr = room
        for name, item in self.holding.items():
            item.updateRoom(room)
            
            # ??? Where does this go in? Room change right
            del self.holding[name].prev.items[name]
            self.curr.items[name] = item
            
        return "You have entered {}!".format(room)
    
    def printInventory(self):
        s = "You are holding "
        
        if(len(self.holding) > 0):
            for key in self.holding.keys():
                s = s + key + ", "
            print(s[0:-2])
        else:
            print(s + "nothing.")    