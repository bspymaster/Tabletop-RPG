#Dice.py
from random import *

class Dice:
    dice = {"d2": (1,2), "d6": (1,6), "d10": (1,10), "d12": (1,12), "d20": (1,20), "d100": (1,100)}
    
    #rolls one die of the selected type
    #RETURN int result of roll
    @classmethod
    def basicDieRoll(self,dieType):
        return randint(self.dice[dieType][0],self.dice[dieType][1])
    
    #rolls varius types of dice, and adds on modifiers at the end
    #RETURN tuple (total of all rolls and modifiers,list of all numbers rolled,list of all modifiers)
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
