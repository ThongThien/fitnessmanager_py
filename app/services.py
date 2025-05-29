from .repositories import *

# Students
def list_students():
    return get_all_students()

def add_student(data):
    # validate có thể thêm ở đây
    return create_student(data)

def edit_student(student_id, data):
    student = get_student_by_id(student_id)
    if not student:
        return None
    return update_student(student, data)

def remove_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return False

    # Xóa tất cả đăng ký liên quan
    ClassRegistration.query.filter_by(student_id=student_id).delete()

    # Xóa student
    db.session.delete(student)
    db.session.commit()
    return True


# Trainers
def list_trainers():
    return get_all_trainers()

def add_trainer(data):
    return create_trainer(data)

def edit_trainer(trainer_id, data):
    trainer = get_trainer_by_id(trainer_id)
    if not trainer:
        return None
    return update_trainer(trainer, data)

def remove_trainer(trainer_id):
    trainer = get_trainer_by_id(trainer_id)
    if not trainer:
        return False
    delete_trainer(trainer)
    return True

# Classes
def list_classes():
    return get_all_classes()

def add_class(data):
    return create_class(data)

def edit_class(class_id, data):
    clazz = get_class_by_id(class_id)
    if not clazz:
        return None
    return update_class(clazz, data)

def remove_class(class_id):
    clazz = get_class_by_id(class_id)
    if not clazz:
        return False
    delete_class(clazz)
    return True

# Registrations
def list_registrations():
    return get_all_registrations()

def add_registration(data):
    return create_registration(data)

def remove_registration(reg_id):
    reg = get_registration_by_id(reg_id)
    if not reg:
        return False
    delete_registration(reg)
    return True
