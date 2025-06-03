from . import db

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    dob = db.Column(db.Date)
    address = db.Column(db.Text)
    gender = db.Column(db.Enum('Male', 'Female'), nullable=False)
    registrations = db.relationship('ClassRegistration', back_populates='student')

class Trainer(db.Model):
    __tablename__ = 'trainers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    dob = db.Column(db.Date)
    expertise = db.Column(db.Text)
    classes = db.relationship(
        'Class',
        back_populates='trainer',
        cascade='all, delete-orphan'   # <-- thêm dòng này
    )

class Class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    schedule = db.Column(db.String(255), nullable=False)
    max_students = db.Column(db.Integer, nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'), nullable=False)
    trainer = db.relationship('Trainer', back_populates='classes')

    registrations = db.relationship(
        'ClassRegistration',
        back_populates='clazz',
        cascade='all, delete-orphan'   # <-- Thêm dòng này
    )

class ClassRegistration(db.Model):
    __tablename__ = 'class_registration'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    registration_date = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    expired_date = db.Column(db.DateTime)  # ➕ Thêm dòng này
    student = db.relationship('Student', back_populates='registrations')
    clazz = db.relationship('Class', back_populates='registrations')
