class Teacher:
    def __init__(self, id, subjects):
        self.id = id
        self.subjects = subjects
    
    def info(self):
        print(f"Преподаватель {self.id}")
        print(f"Может вести предметы: {self.subjects}")
    
    def check_subject(self, subject_id):
        return subject_id in self.subjects
