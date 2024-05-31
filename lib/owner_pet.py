class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name,pet_type,owner=None):
        self.name =name
        self.owner = owner
        if  not pet_type in Pet.PET_TYPES:
            raise Exception("Invalid pet_type ")
        self.pet_type =pet_type
        Pet.all.append(self)

        

class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all]
    
    def add_pet(self,pet):
        if not isinstance(pet ,Pet):
            raise TypeError('pet is not in Pet')
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key =lambda pet:pet.name) 



            