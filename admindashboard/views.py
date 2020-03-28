from django.shortcuts import render
from django.http import HttpResponse
from studentdashboard.models import Student,parent
import datetime
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

    return HttpResponse(content="ok")
def admin_add_student(request):
    s = Student.objects.all()
    return render(request, 'admin-add-student.html',{'student' : s[1]})


def admin_studentlist(request):
    student = Student.objects.all()
    return render(request, 'admin-student-list.html', {'students' : student})


def admin_add_teacher(request):
    return render(request, 'admin-add-teacher.html')


def admin_teacherlist(request):
    return render(request, 'admin-teacher-list.html')


def admin_messages(request):
    return render(request, 'message.html')


def admin_add_announcement(request):
    return render(request, 'admin-add-announcement.html')


def admin_add_class(request):
    return render(request, 'admin-add-class.html')


def admin_add_section(request):
    return render(request, 'admin-add-section.html')


def admin_add_subject(request):
    return render(request, 'admin-add-subject.html')


def admin_create_timetable(request):
    return render(request, 'admin-create-timetable.html')


def admin_class_tintetable(request):
    return render(request, 'admin-class-timetable.html')


def admin_attendace(request):
    return render(request, 'teacher-attendence-report.html')


def admin_marks(request):
    return render(request, 'teacher-marks-report.html')


def delete_student(request, student_id):
    s = Student.objects.get(id=student_id)
    s.delete()
    student = Student.objects.all()
    return render(request, 'admin-student-list.html', {'students': student} )