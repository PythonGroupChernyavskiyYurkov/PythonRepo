# Импортируем созданные классы
from Classes.Teacher import Teacher
from Classes.Group import Group
from Classes.Classroom import Classroom
from Classes.Subject import Subject
import json

def create_subjects(subjects_count):
    """
    Создает список предметов
    """
    subjects = []
    for i in range(1, subjects_count + 1):
        subjects.append(Subject(i))
    return subjects

def create_teachers(teachers_data, subjects):
    """
    Создает список преподавателей из входных данных
    """
    teachers = []
    for teacher_id, subject_ids in teachers_data.items():
        # Находим объекты предметов по их ID
        teacher_subjects = [subject for subject in subjects if subject.get_id() in subject_ids]
        teachers.append(Teacher(teacher_id, teacher_subjects))
    return teachers

def create_groups(groups_data, subjects):
    """
    Создает список групп из входных данных
    """
    groups = []
    for group_id, subject_ids in groups_data.items():
        # Находим объекты предметов по их ID
        group_subjects = [subject for subject in subjects if subject.get_id() in subject_ids]
        groups.append(Group(group_id, group_subjects))
    return groups

def create_classrooms(classrooms_count):
    """
    Создает список аудиторий
    """
    classrooms = []
    for i in range(1, classrooms_count + 1):
        classrooms.append(Classroom(i))
    return classrooms

def find_available_teacher(subject, teachers, busy_teachers):
    """
    Находит свободного преподавателя для предмета
    """
    for teacher in teachers:
        if teacher.id not in busy_teachers:
            # Проверяем, может ли преподаватель вести этот предмет
            for teacher_subject in teacher.subjects:
                if teacher_subject.get_id() == subject.get_id():
                    return teacher
    return None

def create_schedule(groups, teachers, classrooms_count, classes_count):
    """
    Создает расписание на день, гарантируя, что каждая группа изучит разные предметы
    """
    # Инициализируем расписание
    schedule = []
    for _ in range(classes_count):
        schedule.append([None] * classrooms_count)
    
    # Создаем аудитории
    classrooms = create_classrooms(classrooms_count)
    
    # Отслеживаем, какие предметы уже изучены каждой группой в течение дня
    studied_subjects = {}
    for group in groups:
        studied_subjects[group.id] = []
    
    # Для каждой пары
    for class_num in range(classes_count):
        busy_teachers = set()
        busy_groups = set()
        
        # Для каждой аудитории в этой паре
        for classroom_idx in range(classrooms_count):
            classroom = classrooms[classroom_idx]
            
            # Пропускаем если аудитория уже занята
            if not classroom.check_availability():
                continue
            
            # Ищем группу и предмет для размещения
            for group in groups:
                if group.id in busy_groups:
                    continue
                
                # Проверяем предметы группы, которые еще не изучались сегодня
                for subject in group.subjects:
                    if subject.get_id() in studied_subjects[group.id]:
                        continue  # Пропускаем предметы, которые уже изучались сегодня
                    
                    # Ищем свободного преподавателя для этого предмета
                    teacher = find_available_teacher(subject, teachers, busy_teachers)
                    
                    if teacher:
                        # Занимаем аудиторию (без вывода сообщений)
                        classroom.is_occupied = True
                        classroom.occupation_info = f"Преподаватель {teacher.id}, Группа {group.id}, Предмет {subject.get_id()}"
                        
                        schedule[class_num][classroom_idx] = {
                            'teacher': teacher.id,
                            'group': group.id,
                            'subject': subject.get_id()
                        }
                        
                        # Помечаем предмет как изученный сегодня этой группой
                        studied_subjects[group.id].append(subject.get_id())
                        
                        # Помечаем преподавателя и группу как занятых на эту пару
                        busy_teachers.add(teacher.id)
                        busy_groups.add(group.id)
                        break
                    
                if group.id in busy_groups:
                    break
        
        # Освобождаем аудитории для следующей пары (без вывода сообщений)
        for classroom in classrooms:
            classroom.is_occupied = False
            classroom.occupation_info = None
    
    return schedule, studied_subjects

def print_schedule(schedule):
    """
    Выводит расписание в виде таблицы
    """
    print("\n" + "="*50)
    print("РАСПИСАНИЕ НА ДЕНЬ")
    print("="*50)
    
    # Заголовок таблицы
    print("\n{:<10}".format("Пара"), end="")
    for i in range(len(schedule[0])):
        print("{:<20}".format(f"Аудитория {i+1}"), end="")
    print()
    
    # Данные таблицы
    for class_num, classrooms in enumerate(schedule):
        print("{:<10}".format(f"{class_num+1}"), end="")
        
        for classroom in classrooms:
            if classroom:
                info = f"П:{classroom['teacher']} Г:{classroom['group']} П:{classroom['subject']}"
                print("{:<20}".format(info), end="")
            else:
                print("{:<20}".format("---"), end="")
        print()

def print_study_progress(studied_subjects, groups):
    """
    Выводит прогресс изучения предметов по группам
    """
    print("\n" + "="*50)
    print("ПРОГРЕСС ИЗУЧЕНИЯ ПРЕДМЕТОВ")
    print("="*50)
    
    for group in groups:
        studied_count = len(studied_subjects[group.id])
        total_count = len(group.subjects)
        print(f"Группа {group.id}: изучено {studied_count}/{total_count} предметов")
        print(f"  Изученные: {studied_subjects[group.id]}")
        remaining = [s.get_id() for s in group.subjects if s.get_id() not in studied_subjects[group.id]]
        if remaining:
            print(f"  Осталось: {remaining}")
        print()

def load_data_from_file(filename):
    """
    Загружает данные из JSON файла
    """
    with open(filename, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    
    # Сначала создаем предметы
    subjects = create_subjects(json_data['Subjects'])
    
    # Затем создаем группы и преподавателей с использованием объектов Subject
    groups = create_groups(json_data['Groups'], subjects)
    teachers = create_teachers(json_data['Teachers'], subjects)
    classrooms_count = json_data['Classrooms']
    classes_count = json_data['Classes']
    
    return groups, teachers, classrooms_count, classes_count, subjects

def print_teacher_info(teacher):
    """
    Выводит информацию о преподавателе
    """
    subject_ids = [subject.get_id() for subject in teacher.subjects]
    print(f"Преподаватель {teacher.id}")
    print(f"Может вести предметы: {subject_ids}")

def print_group_info(group):
    """
    Выводит информацию о группе
    """
    subject_ids = [subject.get_id() for subject in group.subjects]
    print(f"Группа {group.id}")
    print(f"Изучает предметы: {subject_ids}")

# Основная функция
def example():
    """
    Основная функция для составления расписания
    """
    # Загружаем данные из файла data.json
    try:
        groups, teachers, classrooms_count, classes_count, subjects = load_data_from_file('data.json')
        
        # Создаем расписание
        schedule, studied_subjects = create_schedule(groups, teachers, classrooms_count, classes_count)
        
        # Выводим расписание
        print_schedule(schedule)
        
        # Выводим прогресс изучения
        print_study_progress(studied_subjects, groups)
        
        # Дополнительная информация
        print("\n" + "="*50)
        print("ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ")
        print("="*50)
        
        print("\nПредметы:")
        for subject in subjects:
            subject.info()
        
        print("\nПреподаватели:")
        for teacher in teachers:
            print_teacher_info(teacher)
        
        print("\nГруппы:")
        for group in groups:
            print_group_info(group)
            
    except FileNotFoundError:
        print("Файл data.json не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
