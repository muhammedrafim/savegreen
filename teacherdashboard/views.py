from django.shortcuts import render, redirect
from studentdashboard.models import Student,attendance,marks
from .models import teachers
from admindashboard.models import Class,ClassSection,Subject,TimeTable
import datetime
# Create your views here.
def teacher_dashboard(request):
    teacher = teachers.objects.get(username=request.user.username)
    return render(request, "teacher-dashboard.html" , {'teachers' : teacher})


def create_assignment(request):
    teacher = teachers.objects.get(username=request.user.username)
    return render(request, "teacher-create-assignment.html",{'teachers' : teacher})


def download_assignment(request):
    teacher = teachers.objects.get(username=request.user.username)
    return render(request, "teacher-assignment-download.html",{'teachers' : teacher})


def mark_student_attendance(request):
    teacher = request.user
    teach = teachers.objects.get(username=teacher.username)
    section = ClassSection.objects.get(section_teacher=teach)
    clas = Class.objects.all().filter(id=section.class_name.id)
    subject = Subject.objects.all().filter(subject_class__in=clas)
    students = Student.objects.all().filter(class_name__in=clas,class_division=section)
    timetable = TimeTable.objects.all().distinct('time_slot')
    return render(request, "teacher-mark-student-attendence.html", {'students':students,'classes':clas,'sections':section,'subjects':subject,'timetables':timetable,'teachers' : teach})


def view_student_attendace(request):
    teacher = teachers.objects.get(username=request.user.username)
    return render(request,'teacher-attendence-list.html',{'teachers' : teacher})

def add_student_mark(request):
    if request.method == 'GET':
        t = request.user
        teach = teachers.objects.get(username=t.username)
        subjects = Subject.objects.all().filter(teacher=teach)
        section = []
        for subject in subjects:
            clas = Class.objects.get(id=subject.subject_class.id)
            section = ClassSection.objects.filter(id=subject.subject_section.id)
        return render(request , "teacher-mark-select.html", {'subjects' : subjects,'sections' : section,'teachers' : teach})
    if request.method == 'POST' :
        clas = Class.objects.get(id=request.POST['class'])
        section =ClassSection.objects.get(id=request.POST['section'])
        subject = Subject.objects.get(id=request.POST['subject'])
        type = request.POST['type']

        student = Student.objects.all().filter(class_name=clas,class_division=section)
        teacher = teachers.objects.get(username=request.user.username)
        return render(request,"teacher-add-student-marks.html",{'students':student,'subject' : subject,'type' : type ,'teachers' : teacher, 'class':clas,'section':section})



def teacher_timetable(request):
    teacher = teachers.objects.get(username=request.user.username)
    teacher_name = teacher.firstname+' '+teacher.middlename+' '+teacher.lastname
    timetable =TimeTable.objects.all().filter(teacher=teacher_name)
    time_slot = TimeTable.objects.all().distinct('time_slot')
    return render(request, "teacher-timetable.html" , {'timetables':timetable,'time_slots':time_slot,'teachers' : teacher})


def view_student_mark(request):
    if request.method == 'GET':
        t = request.user
        teach = teachers.objects.get(username=t.username)
        subjects = Subject.objects.all().filter(teacher=teach)
        for subject in subjects:
            clas = Class.objects.get(id=subject.subject_class.id)
        section = ClassSection.objects.all().filter(class_name=clas)
        return render(request, "teacher-view-marks-select.html",{'teachers' : teach,'subjects':subjects,"classes":clas,'sections':section})
    if request.method == 'POST' :
        clas = Class.objects.get(id=request.POST['class'])
        section =ClassSection.objects.get(id=request.POST['section'])
        subject = request.POST['subject']
        type = request.POST['type']
        mark = marks.objects.all().filter(class_name=clas,section=section,subject=subject,exam_type=type)
        teacher = teachers.objects.get(username=request.user.username)
        return render(request,"teacher-view-student-marks.html",{'marks':mark,'teachers' : teacher})

def teacher_attendance_report(request):
    teacher = teachers.objects.get(username=request.user.username)
    return render(request, "teacher-attendence-report.html",{'teachers' : teacher})


def teacher_marks_report(request):
    teacher = teachers.objects.get(username=request.user.username)
    return render(request, "teacher-marks-report.html",{'teachers' : teacher})


def mark_attendence(request):
    t = request.user
    teach = teachers.objects.get(username=t.username)
    section = ClassSection.objects.get(section_teacher=teach)
    stud = Student.objects.all().filter(class_name=section.class_name,class_division=section)
    clas = Class.objects.get(id=section.class_name.id)
    datemarked = request.POST.get('datemark')
    dob = datetime.datetime.strptime(datemarked, '%m/%d/%Y').strftime('%Y-%m-%d')
    remarks = request.POST['remarks']
    for s in stud:
        student = Student.objects.get(id=request.POST['student_'+str(s.id)])
        is_present = request.POST['ispresent_'+str(s.id)]
        if is_present == 'Present':
            flag = True
        else:
            flag=False
        att  = attendance(teacher_id=teach,class_details=clas,section=section,student=student,date_marked=dob,remarks=remarks,is_present=flag)
        att.save()
    return redirect('teacher_attendence_list')


def attendence_list(request):
    t = request.user
    teach = teachers.objects.get(username=t.username)
    datemarked = request.POST['date']
    dob = datetime.datetime.strptime(datemarked, '%m/%d/%Y').strftime('%Y-%m-%d')
    att = attendance.objects.all().filter(teacher_id=teach,date_marked=dob)
    return render(request, "teacher-view-student-attendence.html", {'attendence':att,'teachers':teach})


def add_marks(request):
    teach = teachers.objects.get(username=request.user.username)
    subject = Subject.objects.get(id=request.POST['subject'])
    clas =Class.objects.get(id=request.POST['class'])
    section = ClassSection.objects.get(id=request.POST['section'])
    type = request.POST['type']
    student = Student.objects.all().filter(class_name=clas,class_division=section)
    for stud in student:
        mark = request.POST['marks_'+str(stud.id)]
        max_marks = request.POST['max_marks_'+str(stud.id)]
        remarks = request.POST['remarks_'+str(stud.id)]
        m = marks(class_name=clas,section=section,exam_type=type,student=stud,marked_by=teach,subject=subject , marks_obtained=mark,total_marks=max_marks,remarks=remarks)
        m.save()

    return redirect('view-marks')