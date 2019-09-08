
class Classy(object):
    """You  can use this class to represent 
    how classy someone or something is
    """ 
    
    def __init__(self):
        self.items = []
        self.classiness = 0
        self.calssinessList = {"tophat": 2, "bowtie": 4, "monocle": 5}
    
    def getClassiness(self):
        return self.classiness
    
    def addItem(self, item):
        if item in self.calssinessList:
            self.classiness += self.calssinessList[item]
            
        self.items.append(item)

