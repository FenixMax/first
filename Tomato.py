class Tomato:
    def __init__(self,index):
        states = {1: "small", 2: "medium", 3: "high"}
        keys = list(states.keys())
        m = 0
        self._index=index
        self._state=states[keys[m]]
    def grow(self):
        self._state=states[keys[m+1]]
    def is_ripe(self):
        if self._state==states[keys[-1]]:
            print("Томат созрел")
        else:
            print("Томат еще не созрел")
class TomatoBush:
    def __init__(self,skolko):
        self.skolko=skolko
        self.tomatoes=[]
        for i in range(skolko):
            a=Tomato(input())
            self.tomatoes.append(a)
    def grow_all(self):
        self.tomatoes=[x.grow() for x in self.tomatoes]
    def all_are_ripe(self):
        k=0
        for h in self.tomatoes:
            if self._state==states[keys[-1]]:
                k+=1
        if k==len(self.tomatoes):
            True
    def give_away_all(self):
        for h in self.tomatoes:
            if self._state==states[keys[-1]]:
                self.tomatoes.remove(h)
class Gardener:
    def __init__(self,name):
        self.name=name
        self._plant=TomatoBush(int(input()))
    def work(self):
        self._plant.grow_all()
    def harvest(self):
        if self._plant.all_are_ripe()==True:
            self._plant.give_away_all
        else:
            print("Не все плоды созрели")
    staticmethod
    def knowledge_base(self):
        print("консоль-справка по садоводству")
if __name__=="__main__":
    a=Gardener(input())
    a.knowledge_base()
    t=TomatoBush(2)
    h=Gardener("Nursultan")
    h.work()
    h.harvest()







