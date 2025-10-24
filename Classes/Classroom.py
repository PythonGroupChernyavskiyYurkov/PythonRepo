class Classroom:
    def __init__(self, id):
        self.id = id
        self.is_occupied = False
        self.occupation_info = None
    
    def info(self):
        print(f"Аудитория {self.id}")
        if self.is_occupied:
            print("Статус: занята")
            if self.occupation_info:
                print(f"Занятие: {self.occupation_info}")
        else:
            print("Статус: свободна")
    
    def occupy(self, teacher, group, subject):
        if not self.is_occupied:
            self.is_occupied = True
            self.occupation_info = f"Преподаватель {teacher}, Группа {group}, Предмет {subject}"
            print(f"Аудитория {self.id} теперь занята")
            return True
        else:
            print(f"Аудитория {self.id} уже занята!")
            return False
    
    def free(self):
        if self.is_occupied:
            self.is_occupied = False
            self.occupation_info = None
            print(f"Аудитория {self.id} теперь свободна")
            return True
        else:
            print(f"Аудитория {self.id} и так свободна")
            return False
    
    def check_availability(self):
        return not self.is_occupied
