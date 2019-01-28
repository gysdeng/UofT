class piece:
    
    """
    Name: Name of the object
    
    Start: Starting room of the object
    Prev: Room that the object was previously in
    Curr: Room that the object is currently in
    
    Status: unused, inuse, used
    
    Targets: All the targetted rooms that the object wants to direct player to
    Related: All related objects this one watches for
    """
    def __init__(self, name, start, end, related = None, status = "unused"):
        
        self.name = name
        self.start = start
        self.prev = start
        self.curr = start
        self.status = status
        
        self.targets = []
        self.targets.append(end)        
        
        self.related = {}
        
        # Convert a list of related items in to related dict    
        if related != None:
            for i in related:
                self.related[i.name] = i
                self.targets.append(i.curr)
    
    
    def __str__(self):
        s = "{0}: Status: {1}, Placed in {2}, Currently In: {3}, Directing to: ".format(
            self.name, self.status, self.start, self.curr)
        for target in self.targets:
            s = s + str(target) + " "
        return s.strip()
    
    
    def updateRoom(self, nxt):
        self.prev = self.curr
        self.curr = nxt
        

    # watch for complementary items
    def poll(self):
        
        if self.status != "used":
            
            print("Polling!")
            
            for key, val in self.related.items():
                if val.status == "used":
                    self.targets.remove(val.curr)
                elif val.status == "holding":
                    self.targets.remove(val.curr)
                elif val.status == "holding":
                    self.targets.remove(val.prev)
                    self.targets.append(val.curr)