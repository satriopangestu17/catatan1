class karnivora(object):
    def __init__(self):
        self.daging= True

class herbivora(object):
    def __init__(self):
        self.tumbuhan= True

class omnivora(karnivora, herbivora):
    def __init__(self):
        karnivora.__init__(self)
        herbivora.__init__(self)
        self.mcd = True
        self.nama =True

objA = omnivora()
print(vars(objA))
# print(omnivora.__mro__)