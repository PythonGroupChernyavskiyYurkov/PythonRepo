class Group:
    def __init__(self, id, subjects):
        self.id = id
        self.subjects = subjects
    
    def info(self):
        print(f"Группа {self.id}")
        print(f"Изучает предметы: {self.subjects}")
    
    def check_subject(self, subject_id):
        for subject in self.subjects:
            if subject == subject_id:
                return True
        return False
    
    def add_subject(self, subject_id):
        if subject_id not in self.subjects:
            self.subjects.append(subject_id)
            print(f"Добавлен предмет {subject_id} в группу {self.id}")
        else:
            print(f"Предмет {subject_id} уже есть в группе {self.id}")
    
    def remove_subject(self, subject_id):
        if subject_id in self.subjects:
            self.subjects.remove(subject_id)
            print(f"Удален предмет {subject_id} из группы {self.id}")
        else:
            print(f"Предмета {subject_id} нет в группе {self.id}")
