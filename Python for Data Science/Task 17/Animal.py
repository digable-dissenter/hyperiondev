
class Animal(object):
    '''
    Animal superclass as a template to create objects
    '''
    def __init__(self, numteeth, spots, weight):
        self.numteeth = numteeth 
        self.spots = spots
        self.weight = weight
       
    def get_color(self, color):
        self.color = color
        return self.color
       
        
class Lion(Animal):
    '''    
    Lion subclass inherits its constructor and the get_color method from Animal.
    Every instance of Lion is also an instance of Animal.
    Added sound field
    '''
    def __init__(self, numteeth, spots, weight, sound):
        super(Lion, self).__init__(numteeth, spots, weight)
        self.sound = sound
    '''
    __str__ method calculates whether the lion is a cub, male or female based on
    its weight property/field
    '''
    def __str__(self):
        weight = self.weight        
        if weight > 120:
            return "This lion is male"
        elif weight < 120:
            return "This lion is female"
        elif weight < 80:
            return "This lion is a cub"
'''
Creating lion object
'''
lion = Lion(32,False,110,"roar")
'''
Calling __str__ method that prints the result
'''
print(str(lion.__str__()))

class Cheetah(Animal):
    '''
    Cheetah subclass inherits its constructor and the get_color method from Animal.
    Every instance of Cheetah is also an instance of Animal.
    Added sounds field as an array/list
    '''
    def __init__(self, numteeth, spots, weight, sounds):
        super(Cheetah, self).__init__(numteeth, spots, weight)
        self.sounds = []
    '''
    add_sound method adds to the list of sounds Cheetahs make
    '''
    def add_sound(self, sounds):
        self.sounds.append(sounds)
    '''
    display_method prints out each sound the Cheetah makes
    '''
    def display_sounds(self):
        for s in self.sounds:
            print("Cheetahs can " + s)
'''
Created list of sounds outside of class to add later
'''
sounds = ["meow","purr"]
'''
Creating lion object
'''
cheetah = Cheetah(28,True,100,[])
'''
For each sound specified in the list above, the add_sounds method is called to add to cheetah object
'''
for s in sounds:
    cheetah.add_sound(s)
'''
Display output
'''
cheetah.display_sounds()
