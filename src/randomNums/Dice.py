#Dice.py
from random import *

class Dice:
    dice = {"d2": (1,2), "d6": (1,6), "d10": (1,10), "d12": (1,12), "d20": (1,20), "d100": (1,100)}
    
    """
    rolls one die of the selected type
    @param string the selected die (must be one of the following: "d2", "d6", "d10", "d12", "d20", "d100")
    @return integer result of roll
    """
    @classmethod
    def basicDieRoll(self,dieType):
        return randint(self.dice[dieType][0],self.dice[dieType][1])
    
    """
    rolls varius types of dice, and adds on modifiers at the end
    @param list a list of strings of the selected die (must be one of the following: "d2", "d6", "d10", "d12", "d20", "d100")
    @param list a list of integers that will modify a die roll
    @return tuple an integer total of all rolls and modifiers, followed by a list of integers of all the numbers rolled, followed by a list of integers of all the modifiers
    """
    @classmethod
    def complexDieRoll(self,dieTypes,modifiers):
        total = 0
        rollList = []
        modifierList = []
        for die in dieTypes:
            roll = self.basicDieRoll(die)
            total += roll
            rollList.append(roll)
        
        for mod in modifiers:
            total += mod
            modifierList.append(mod)
        
        return (total,rollList,modifierList)
