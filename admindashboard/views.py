from django.shortcuts import render
from django.http import HttpResponse
from studentdashboard.models import Student,parent
from teacherdashboard.models import teachers
import datetime
from .models import Class,ClassSection,Subject,TimeTable
from django.contrib.auth.models import User,auth
# Create your views here.
def admindashboard(request):
    return render(request, 'admin-dashboard.html')


def add_student(request):
    fathername = request.POST['father_name']
    mothername = request.POST['mother_name']
    parent_occupation = request.POST['parent_occupation']
    parent_contact = request.POST['parent_contact']
    parent_alternate_contact = request.POST['parent_alternate_contact']
    parent_email = request.POST['parent_email']
    parent_religion = request.POST.get('parent_religion')
    parent_nationality = request.POST['parent_nationality']
    address = request.POST['address']
    parent_country = request.POST['parent_country']
    parent_state = request.POST['parent_state']
    pincode = request.POST['pincode']
    parent_photo = request.FILES['parent_photo']

    p = parent(father_name=fathername, mothers_name=mothername, occupation=parent_occupation,contact_info=parent_contact,
               alternate_contact_info=parent_alternate_contact,country=parent_country ,nationality=parent_nationality,pincode=pincode,
               address=address, email=parent_email, state=parent_state, image=parent_photo, religion=parent_religion)
    p.save()

    firstname = request.POST['firstname_student']
    middlename = request.POST['middlename_student']
    lastname = request.POST['lastname_student']
    gender_student = request.POST['gender_student']
    student_dob = request.POST.get('student_dob')
    student_phone = request.POST['student_phone']
    student_email = request.POST['student_email']
    student_religion = request.POST['student_religion']
    student_photo = request.FILES['student_photo']
    student_registration = request.POST['registration_number']
    student_class = request.POST['student_class']
    student_division = request.POST['student_division']
    student_roll_no = request.POST['student_roll_no']
    last_school = request.POST['last_school']
    last_class = request.POST.get('last_std')
    last_mark = request.POST['last_mark']
    sports = request.POST['sports']

    dob = datetime.datetime.strptime(student_dob, '%d/%m/%Y').strftime('%Y-%m-%d')

    s = Student(firstname=firstname, middlename=middlename,lastname=lastname,gender=gender_student, dateofbirth=dob,phone_number=student_phone,
               email=student_email,religion=student_religion,image=student_photo,registration_id=student_registration, class_name=student_class,
               class_division=student_division, roll_number=student_roll_no, last_std=last_class, last_school=last_school, last_marks_obtained=last_mark,
                sports_intreseted=sports,parent=p)
    s.save()
    return HttpResponse(content="document.alert('ok')")


def edit_student(request, student_id):
    firstname = request.POST['firstname_student']
    middlename = request.POST['middlename_student']
    lastname = request.POST['lastname_student']
    student_class = request.POST['class']
    division = request.POST['class_division']
    roll_no = request.POST['roll_no']
    phone  = request.POST['contact']
    email = request.POST['email']
    s = Student.objects.get(id=student_id)
    s.firstname=firstname
    s.middlename = middlename
    s.lastname = lastname
    s.class_name = student_class
    s.class_division = division
    s.roll_number = roll_no
    s.email = email
    s.phone_number=phone

    s.save()
    student = Student.objects.all()
    return render(request,'admin-student-list.html',{"students" : student})


def admin_add_student(request):
    return render(request, 'admin-add-student.html')


def admin_studentlist(request):
    student = Student.objects.all()
    return render(request, 'admin-student-list.html', {'students' : student})


def admin_add_teacher(request):
    return render(request, 'admin-add-teacher.html')


def admin_teacherlist(request):
    teacher = teachers.objects.all()
    return render(request, 'admin-teacher-list.html', {'teachers' : teacher})


def admin_messages(request):
    return render(request, 'message.html')


def admin_add_announcement(request):
    return render(request, 'admin-add-announcement.html')


def admin_add_class(request):
    teacher = teachers.objects.all()
    clas = Class.objects.all()
    return render(request, 'admin-add-class.html', {'teachers' : teacher , 'classes' : clas})


def admin_add_section(request):
    classes = Class.objects.all()
    sections = ClassSection.objects.all()
    return render(request, 'admin-add-section.html', {'classes': classes,'sections' : sections})


def admin_add_subject(request):
    subject = Subject.objects.all()
    teach = teachers.objects.all()
    clas = Class.objects.all()
    return render(request, "admin-add-subject.html",{"subjects" : subject,"teachers" : teach, "classes": clas})


def admin_create_timetable(request):
    teacher = teachers.objects.all()
    subjects = Subject.objects.all()
    clas = Class.objects.all()
    section = ClassSection.objects.all().distinct('section_name')
    timetable = TimeTable.objects.all()
    return render(request, 'admin-create-timetable.html', {'teachers' : teacher, 'subjects':subjects , 'classes' : clas, 'sections' : section, 'timetables' : timetable})


def admin_class_tintetable(request):
    teacher = teachers.objects.all()
    subjects = Subject.objects.all()
    clas = Class.objects.all()
    section = ClassSection.objects.all().distinct('section_name')
    timetable = TimeTable.objects.all()
    time_slot = TimeTable.objects.all().distinct('time_slot')
    return render(request, 'admin-class-timetable.html', {'teachers' : teacher, 'subjects':subjects , 'classes' : clas,'time_slots':time_slot, 'sections' : section, 'timetables' : timetable})



def admin_attendace(request):
    return render(request, 'teacher-attendence-report.html')


def admin_marks(request):
    return render(request, 'teacher-marks-report.html')


def delete_student(request, student_id):
    s = Student.objects.get(id=student_id)
    s.delete()
    student = Student.objects.all()
    return render(request, 'admin-student-list.html', {'students': student} )

def add_teacher(request):
    firstname = request.POST['firstname']
    middlename = request.POST['middlename']
    lastname = request.POST['lastname']
    gender = request.POST['gender']
    dob = request.POST.get('dob')
    phone = request.POST['phone']
    email = request.POST['email']
    religion = request.POST['religion']
    photo = request.FILES['photo']
    alternate_phone = request.POST['alternate_phone']
    address = request.POST['address']
    address_alternate = request.POST['address_alternate']
    country = request.POST['country']
    state = request.POST['state']
    pincode = request.POST['pincode']
    highest_degree = request.POST['highest_degree']
    highest_college = request.POST['highest_college']
    highest_year = request.POST['highest_year']
    highest_cgpa = request.POST['highest_cgpa']
    degree = request.POST['degree']
    college = request.POST['college']
    year = request.POST['year']
    cgpa = request.POST['cgpa']
    username = request.POST['username']
    password = request.POST['password']


    dob_ = datetime.datetime.strptime(dob, '%d/%m/%Y').strftime('%Y-%m-%d')
    t = teachers(firstname=firstname, middlename= middlename, lastname=lastname, gender=gender, email=email,dateofbirth=dob_, religion=religion,
                 phone_number=phone, alternate_phone=alternate_phone, address=address, address_alternate=address_alternate, image=photo,
                 country=country, state=state, pincode=pincode, highest_degree=highest_degree, highest_degree_university=highest_college,
                 highest_degree_cgpa=highest_cgpa, highest_degree_yearpassed=highest_year,degree=degree,university=college,
                 yearpassed=year,cgpa=cgpa,username=username)
    t.save()
    last_name = middlename+" "+lastname
    user = User.objects.create_user(username=username,password=password,email=email, first_name= firstname,last_name=last_name)
    user.save()

    teacher = teachers.objects.all()
    return render(request, "admin-teacher-list.html", {'teachers':teacher})

def edit_teacher(request):
    firstname = request.POST['firstname']
    middlename = request.POST['middlename']
    lastname = request.POST['lastname']
    address = request.POST['address']
    degree = request.POST['degree']
    college = request.POST['college']
    email = request.POST['email']
    phone = request.POST['contact']
    teacer_id = request.POST['teacherid']

    t = teachers.objects.get(id=teacer_id)
    t.firstname = firstname
    t.middlename = middlename
    t.lastname = lastname
    t.address=address
    t.highest_degree = degree
    t.highest_degree_university = college
    t.email = email
    t.phone_number =phone
    t.save()

    teacher = teachers.objects.all()
    return render(request, "admin-teacher-list.html", {"teachers" : teacher})


def delete_teacher(request):
    teacher_id = request.POST.get('teacher_id')

    t = teachers.objects.get(id=teacher_id)
    t.delete()
    teacher = teachers.objects.all()
    return render(request, "admin-teacher-list.html", {"teachers" : teacher})


def add_class(request):
    class_name = request.POST['class']
    class_code = request.POST['code']
    class_teacher = request.POST['teacher']
    description = request.POST['description']


    teach = teachers.objects.get(id=class_teacher)
    c = Class(class_name=class_name,class_code=class_code,class_teacher=teach,description=description)
    c.save()
    classes = Class.objects.all()
    teacher = teachers.objects.all()
    return render(request, "admin-add-class.html", {'classes' : classes , 'teachers' : teacher})


def edit_class(request):
    class_name = request.POST['class']
    class_code = request.POST['code']
    class_teacher = request.POST['teacher']
    description = request.POST['description']
    class_id = request.POST['class_id']

    teach = teachers.objects.get(id=class_teacher)
    c = Class.objects.get(id=class_id)
    c.class_name = class_name
    c.class_code = class_code
    c.class_teacher = teach
    if description != "":
        c.description = description
    c.save()

    classes = Class.objects.all()
    teacher = teachers.objects.all()
    return render(request, "admin-add-class.html", {'classes' : classes , 'teachers' : teacher})

def delete_class(request):
    class_id = request.POST['class_id']
    c = Class.objects.get(id=class_id)
    c.delete()

    classes = Class.objects.all()
    teacher = teachers.objects.all()
    return render(request, "admin-add-class.html", {'classes': classes, 'teachers': teacher})


def add_section(request):
    class_name = request.POST['class']
    code = request.POST['code']
    section = request.POST['section']
    description = request.POST['description']

    cl_id = Class.objects.get(id=class_name)
    c = ClassSection(description=description,section_name=section,section_code=code,class_name=cl_id)
    c.save()
    classes = Class.objects.all()
    sections = ClassSection.objects.all()
    return render(request, "admin-add-section.html", {'classes' : classes , 'sections' : sections})

def edit_section(request):
    class_name = request.POST['class']
    code = request.POST['code']
    section  = request.POST['section']
    description = request.POST['description']
    section_id = request.POST['section_id']

    cl_id = Class.objects.get(id=class_name)
    c = ClassSection.objects.get(id=section_id)
    c.class_name = cl_id
    c.section_code = code
    c.section_name = section
    if description != "":
        c.description = description
    c.save()

    classes = Class.objects.all()
    sections = ClassSection.objects.all()
    return render(request, "admin-add-section.html", {'classes' : classes , 'sections' : sections})


def delete_section(request):
    section_id = request.POST['section_id']
    c = ClassSection.objects.get(id=section_id)
    c.delete()

    classes = Class.objects.all()
    sections = ClassSection.objects.all()
    return render(request, "admin-add-section.html", {'classes' : classes , 'sections' : sections})


def add_subject(request):
    name = request.POST['name']
    code = request.POST['code']
    subject_class = request.POST['class']
    teacher = request.POST['teacher']
    description = request.POST['description']

    teach = teachers.objects.get(id=teacher)
    class_obj = Class.objects.get(id=subject_class)

    s = Subject(name=name,code=code,subject_class=class_obj,teacher=teach,description=description)
    s.save()

    subject = Subject.objects.all()
    teach = teachers.objects.all()
    clas = Class.objects.all()
    return render(request, "admin-add-subject.html",{"subjects" : subject,"teachers" : teach, "classes": clas})

def edit_subject(request):
    name = request.POST['name']
    code = request.POST['code']
    subject_class = request.POST['class']
    teacher = request.POST['teacher']
    description = request.POST['description']
    subject_id = request.POST['subject_id']


    teach = teachers.objects.get(id=teacher)
    class_obj = Class.objects.get(id=subject_class)
    s =Subject.objects.get(id=subject_id)
    s.name = name
    s.subject_class = class_obj
    s.teacher = teach
    s.code = code
    if description != '' :
        s.description=description
    s.save()


    subject = Subject.objects.all()
    teach = teachers.objects.all()
    clas = Class.objects.all()
    return render(request, "admin-add-subject.html",{"subjects" : subject,"teachers" : teach, "classes": clas})

def delete_subject(request):
    subject_id = request.POST['subject_id']
    s = Subject.objects.get(id=subject_id)
    s.delete()

    subject = Subject.objects.all()
    teach = teachers.objects.all()
    clas = Class.objects.all()
    return render(request, "admin-add-subject.html",{"subjects" : subject,"teachers" : teach, "classes": clas})


def add_timetable(request):
    day = request.POST['day']
    slot = request.POST['slot']
    class_name = request.POST['class']
    section = request.POST['section']
    room = request.POST['room']
    teacher = request.POST['teacher']
    subject = request.POST['subject']

    t = TimeTable(day=day, time_slot=slot,class_name=class_name,class_section=section,classroom=room,teacher=teacher,subject_name=subject)
    t.save()


    teacher = teachers.objects.all()
    subjects = Subject.objects.all()
    clas = Class.objects.all()
    section = ClassSection.objects.all()
    timetable = TimeTable.objects.all()
    return render(request, 'admin-create-timetable.html', {'teachers' : teacher, 'subjects':subjects , 'classes' : clas, 'sections' : section, 'timetables' : timetable})


def edit_timetable(request):
    timetable_id = request.POST['timetable_id']
    day = request.POST['day']
    slot = request.POST['slot']
    class_name = request.POST['class']
    section = request.POST['section']
    room = request.POST['room']
    teacher = request.POST['teacher']
    subject = request.POST['subject']

    t = TimeTable.objects.get(id=timetable_id)
    t.day=day
    t.time_slot=slot
    t.class_name=class_name
    t.class_section=section
    t.teacher=teacher
    t.classroom = room
    t.subject_name = subject
    t.save()

    teacher = teachers.objects.all()
    subjects = Subject.objects.all()
    clas = Class.objects.all()
    section = ClassSection.objects.all()
    timetable = TimeTable.objects.all()
    return render(request, 'admin-create-timetable.html',
                  {'teachers': teacher, 'subjects': subjects, 'classes': clas, 'sections': section,
                   'timetables': timetable})

def delete_timetable(request):
    _id = request.POST['timetable_id']
    s = TimeTable.objects.get(id=_id)
    s.delete()

    teacher = teachers.objects.all()
    subjects = Subject.objects.all()
    clas = Class.objects.all()
    section = ClassSection.objects.all()
    timetable = TimeTable.objects.all()
    return render(request, 'admin-create-timetable.html',
                  {'teachers': teacher, 'subjects': subjects, 'classes': clas, 'sections': section,
                   'timetables': timetable})


def search_timetable(request):
    class_name = request.POST['class']
    section = request.POST['section']
    if class_name == 'All' :
            if section == 'All':
                timetable = TimeTable.objects.all()
            else :
                timetable = TimeTable.objects.all().filter(class_section=section)
    else :
        if section == 'All':
            timetable = TimeTable.objects.all().filter(class_name=class_name)
        else:
            timetable = TimeTable.objects.all().filter(class_name=class_name,class_section=section)
    teacher = teachers.objects.all()
    subjects = Subject.objects.all()
    clas = Class.objects.all()
    section = ClassSection.objects.all()
    time_slot = TimeTable.objects.all().distinct('time_slot')
    return render(request, 'admin-class-timetable.html', {'teachers' : teacher, 'subjects':subjects , 'classes' : clas,'time_slots':time_slot, 'sections' : section, 'timetables' : timetable})


