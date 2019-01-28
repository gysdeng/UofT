from piece import piece

class room:
    
    # default functions
    def __init__(self, name):
        self.name = name
        self.items = {}
        
    def __str__(self):
        return self.name       
        
    # managing items
    def addItem(self, name, end, related = None):
        self.items[name] = piece(name, self, end, related)
        
        #target = [target] if type(target) == int else target
        #targets = target + [self.end] if target != None else [self.end]
        #self.items.append(piece(name, self.number, targets))
        
    def removeItem(self, name):
        temp = self.items[name]
        del self.items[name]
        return temp
    
    def removeAllItems(self):
        self.items.clear()
    
    def printItems(self):
        print(self)
        for key, val in self.items.items():
            print("     ", val)
        
    
if __name__ == "__main__":
    
    main = room("MAIN")
    
    kitchen = room("KITCHEN")
    print(kitchen)
    
    kitchen.addItem("Microwave", main.name)
    kitchen.printItems()