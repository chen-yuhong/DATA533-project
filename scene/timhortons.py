from .level import level

#inheritance from class level
class timHortons(level):

    #initialize
    def __init__(self, location, lines, alien, inventory):
        level.__init__(self, location, lines, alien)
        self.visit()
        self.unlock()
        self.__inventory = inventory

    #update item amount when the item is sold 
    def sell(self, item):
        item.setamount(item.getamount()-1)

    #check item stock
    def checkStock(self, name):
        for r in self.getInv():
            if r.getname() == name and r.getamount() > 0:
                return r
            elif r.getname() == name and r.getamount() == 0:
                return 1
            elif name == "turkey bacon club":
                return 3
        return 2

    #return inventory
    def getInv(self):
        return self.__inventory

