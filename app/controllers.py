from flask import Blueprint, flash, render_template, request, redirect, url_for, abort
from .services import *
from .repositories import get_student_by_id, get_trainer_by_id, get_class_by_id, get_registration_by_id
from datetime import datetime, timedelta
  

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

# --- Students ---
@main_bp.route('/students')
def students_index():
    students = list_students()
    return render_template('students/index.html', students=students)

@main_bp.route('/students/create', methods=['GET', 'POST'])
def students_create():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form.get('phone'),
            'dob': request.form.get('dob'),
            'address': request.form.get('address'),
            'gender': request.form['gender']
        }
        add_student(data)
        return redirect(url_for('main.students_index'))
    return render_template('students/create.html')

@main_bp.route('/students/edit/<int:id>', methods=['GET', 'POST'])
def students_edit(id):
    student = get_student_by_id(id)
    if not student:
        abort(404)
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form.get('phone'),
            'dob': request.form.get('dob'),
            'address': request.form.get('address'),
            'gender': request.form['gender']
        }
        edit_student(id, data)
        return redirect(url_for('main.students_index'))
    return render_template('students/edit.html', student=student)

@main_bp.route('/students/delete/<int:id>', methods=['POST'])
def students_delete(id):
    if not remove_student(id):
        abort(404)
    return redirect(url_for('main.students_index'))

@main_bp.route('/students/<int:id>')
def students_detail(id):
    student = get_student_by_id(id)
    if not student:
        abort(404)
    return render_template('students/details.html', student=student)

# --- Registrations ---
@main_bp.route('/registrations')
def registrations_index():
    registrations = list_registrations()
    return render_template('registrations/index.html', registrations=registrations)

@main_bp.route('/registrations/create', methods=['GET', 'POST'])
def registrations_create():
    students = list_students()
    classes = list_classes()
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        class_id = request.form.get('class_id')
        if not student_id or not class_id:
            abort(400, description="Thiếu thông tin học viên hoặc lớp học")

        student_id = int(student_id)
        class_id = int(class_id)

        # 1. Kiểm tra học viên đã đăng ký lớp chưa
        existing = get_registration_by_student_and_class(student_id, class_id)
        if existing:
            flash('Học viên này đã đăng ký lớp học rồi.', 'warning')
            return redirect(url_for('main.registrations_create'))

        # 2. Lấy lớp học bằng hàm get_class_by_id
        clazz = get_class_by_id(class_id)
        if clazz is None:
            flash('Lớp học không tồn tại.', 'danger')
            return redirect(url_for('main.registrations_create'))

        # 3. Kiểm tra số lượng học viên đã đăng ký
        current_count = count_registrations_by_class(class_id)
        if current_count >= clazz.max_students:
            flash(f'Lớp học "{clazz.class_name}" đã đạt số lượng học viên tối đa ({clazz.max_students}).', 'danger')
            return redirect(url_for('main.registrations_create'))

        # Nếu tất cả ok thì thêm đăng ký
        data = {
            'student_id': student_id,
            'class_id': class_id,
        }
        add_registration(data)
        flash('Đăng ký thành công!', 'success')

    return render_template('registrations/create.html', students=students, classes=classes)

@main_bp.route('/registrations/extend/<int:reg_id>', methods=['POST'])
def registrations_extend(reg_id):
    reg = ClassRegistration.query.get_or_404(reg_id)
    extend_type = request.form.get('extend_type')

    days = 0
    if extend_type == '15d':
        days = 15
    elif extend_type == '1m':
        days = 30
    elif extend_type == '2m':
        days = 60

    if reg.expired_date is None:
        reg.expired_date = datetime.utcnow() + timedelta(days=days)
    else:
        reg.expired_date += timedelta(days=days)

    db.session.commit()
    flash('Gia hạn thành công!', 'success')
    return redirect(url_for('main.registrations_index'))

@main_bp.route('/registrations/delete/<int:id>', methods=['POST'])
def registrations_delete(id):
    if not remove_registration(id):
        abort(404)
    return redirect(url_for('main.registrations_index'))

# --- Trainers ---
@main_bp.route('/trainers')
def trainers_index():
    trainers = list_trainers()
    return render_template('trainers/index.html', trainers=trainers)

@main_bp.route('/trainers/create', methods=['GET', 'POST'])
def trainers_create():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form.get('phone'),
            'dob': request.form.get('dob'),
            'expertise': request.form.get('expertise')
        }
        add_trainer(data)
        return redirect(url_for('main.trainers_index'))
    return render_template('trainers/create.html')

@main_bp.route('/trainers/edit/<int:id>', methods=['GET', 'POST'])
def trainers_edit(id):
    trainer = get_trainer_by_id(id)
    if not trainer:
        abort(404)
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form.get('phone'),
            'dob': request.form.get('dob'),
            'expertise': request.form.get('expertise')
        }
        edit_trainer(id, data)
        return redirect(url_for('main.trainers_index'))
    return render_template('trainers/edit.html', trainer=trainer)

@main_bp.route('/trainers/delete/<int:id>', methods=['POST'])
def trainers_delete(id):
    if not remove_trainer(id):
        abort(404)
    return redirect(url_for('main.trainers_index'))

@main_bp.route('/trainers/<int:id>')
def trainers_detail(id):
    trainer = get_trainer_by_id(id)
    if not trainer:
        abort(404)
    return render_template('trainers/detail.html', trainer=trainer)

# --- Classes ---
@main_bp.route('/classes')
def classes_index():
    classes = list_classes()
    return render_template('classes/index.html', classes=classes)

@main_bp.route('/classes/<int:id>')
def classes_detail(id):
    cls = get_class_by_id(id)
    if not cls:
        abort(404)
    return render_template('classes/details.html', cls=cls)

@main_bp.route('/classes/create', methods=['GET', 'POST'])
def classes_create():
    trainers = list_trainers()
    if request.method == 'POST':
        data = {
            'class_name': request.form['class_name'],
            'description': request.form.get('description'),
            'schedule': request.form['schedule'],
            'max_students': int(request.form['max_students']),
            'trainer_id': int(request.form['trainer_id'])
        }
        add_class(data)
        return redirect(url_for('main.classes_index'))
    return render_template('classes/create.html', trainers=trainers)

@main_bp.route('/classes/edit/<int:id>', methods=['GET', 'POST'])
def classes_edit(id):
    cls = get_class_by_id(id)
    if not cls:
        abort(404)
    trainers = list_trainers()
    if request.method == 'POST':
        data = {
            'class_name': request.form['class_name'],
            'description': request.form.get('description'),
            'schedule': request.form['schedule'],
            'max_students': int(request.form['max_students']),
            'trainer_id': int(request.form['trainer_id'])
        }
        edit_class(id, data)
        return redirect(url_for('main.classes_index'))
    return render_template('classes/edit.html', cls=cls, trainers=trainers)

@main_bp.route('/classes/delete/<int:id>', methods=['POST'])
def classes_delete(id):
    if not remove_class(id):
        abort(404)
    return redirect(url_for('main.classes_index'))

# --- Statistics ---
@main_bp.route('/statistics')
def statistics():
    total_students = len(list_students())
    total_trainers = len(list_trainers())
    total_classes = len(list_classes())
    total_registrations = len(list_registrations())

    student_ids_registered = {r.student_id for r in list_registrations()}
    ratio_registered = 0
    if total_students > 0:
        ratio_registered = len(student_ids_registered) / total_students * 100

    stats = {
        'total_students': total_students,
        'total_trainers': total_trainers,
        'total_classes': total_classes,
        'total_registrations': total_registrations,
        'ratio_registered': round(ratio_registered, 2),
    }

    return render_template('statistics.html', stats=stats)
