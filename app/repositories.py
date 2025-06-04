from datetime import datetime, timedelta
from .models import Student, Trainer, Class, ClassRegistration
from . import db

# Student
def get_all_students():
    return Student.query.all()

def get_student_by_id(student_id):
    return Student.query.get(student_id)

def create_student(data):
    student = Student(**data)
    db.session.add(student)
    db.session.commit()
    return student

def update_student(student, data):
    for key, value in data.items():
        setattr(student, key, value)
    db.session.commit()
    return student

def delete_student(student):
    db.session.delete(student)
    db.session.commit()

# Trainer
def get_all_trainers():
    return Trainer.query.all()

def get_trainer_by_id(trainer_id):
    return Trainer.query.get(trainer_id)

def create_trainer(data):
    trainer = Trainer(**data)
    db.session.add(trainer)
    db.session.commit()
    return trainer

def update_trainer(trainer, data):
    for key, value in data.items():
        setattr(trainer, key, value)
    db.session.commit()
    return trainer

def delete_trainer(trainer):
    db.session.delete(trainer)
    db.session.commit()

# Class
def get_all_classes():
    return Class.query.all()

def get_class_by_id(class_id):
    return Class.query.get(class_id)

def create_class(data):
    clazz = Class(**data)
    db.session.add(clazz)
    db.session.commit()
    return clazz

def update_class(clazz, data):
    for key, value in data.items():
        setattr(clazz, key, value)
    db.session.commit()
    return clazz

def delete_class(clazz):
    db.session.delete(clazz)
    db.session.commit()

# Registration
def get_all_registrations():
    return ClassRegistration.query.all()

def get_registration_by_id(reg_id):
    return ClassRegistration.query.get(reg_id)

def create_registration(data):
    now = datetime.utcnow()
    reg = ClassRegistration(
        student_id=data['student_id'],
        class_id=data['class_id'],
        registration_date=now,
        expired_date=now + timedelta(days=30)
    )
    db.session.add(reg)
    db.session.commit()
    return reg

def get_registration_by_student_and_class(student_id, class_id):
    return ClassRegistration.query.filter_by(student_id=student_id, class_id=class_id).first()

def count_registrations_by_class(class_id):
    return ClassRegistration.query.filter_by(class_id=class_id).count()

def delete_registration(reg):
    db.session.delete(reg)
    db.session.commit()
