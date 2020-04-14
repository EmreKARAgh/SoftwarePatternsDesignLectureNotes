# -*- coding: utf-8 -*-
import copy

class Scene:
    def __init__(self,name):
        self.name = name
        self.Obstacles = []
    def shallowCopy(self):
        return copy.copy(self)
    def deepCopy(self):
        return copy.deepcopy(self)
    def addObstacle(self,obs):
        self.Obstacles.append(obs)
    def getInfo(self):
        print(self.name+':' ,'id:',id(self))
        for i in self.Obstacles:
            i.getInfo()
        print()
class Obstacle:
    def __init__(self,name):
        self.name = name
    def getInfo(self):
        print(self.name)
    

sc1 = Scene('Scene-0')
for i in range(1,3):
    sc1.addObstacle(Obstacle('Obstacle-'+str(i)))

sc2=sc1.shallowCopy()
sc3=sc1.deepCopy()
sc4 = sc1

print('Original Object')
sc1.getInfo()
print('Shallow Copy')
sc2.getInfo()
print('Deep Copy')
sc3.getInfo()
print('Assignment')
sc4.getInfo()

print('*********************   After Changes   *********************\n')
sc1.addObstacle(Obstacle('Obstacle-3'))
sc1.name='Scene 1'
sc2.name='Scene 2'
sc3.name='Scene 3'
sc4.name='Scene 4'

print('Original Object')
sc1.getInfo()
print('Shallow Copy')
sc2.getInfo()
print('Deep Copy')
sc3.getInfo()
print('Assignment')
sc4.getInfo()