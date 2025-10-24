class Subject:
    def __init__(self, id, name=None):
        self.id = id
        self.name = name
    
    def info(self):
        if self.name:
            print(f"Предмет {self.id}: {self.name}")
        else:
            print(f"Предмет {self.id}")
    
    def get_id(self):
        return self.id
    
    def set_name(self, new_name):
        self.name = new_name
        print(f"Название предмета {self.id} изменено на: {new_name}")
