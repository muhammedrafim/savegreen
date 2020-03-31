from django.shortcuts import render, redirect
from studentdashboard.models import Student,attendance
from .models import teachers
from admindashboard.models import Class,ClassSection,Subject,TimeTable
# Create your views here.
def teacher_dashboard(request):
    return render(request, "teacher-dashboard.html")


def create_assignment(request):
    return render(request, "teacher-create-assignment.html")


def download_assignment(request):
    return render(request, "teacher-assignment-download.html")


def mark_student_attendance(request):
    teacher = request.user
    teach = teachers.objects.get(username=teacher.username)
    clas = Class.objects.filter(class_teacher=teach)
    section = ClassSection.objects.all().filter(class_name__in=clas)
    subject = Subject.objects.all().filter(subject_class__in=clas)
    students = Student.objects.all().filter(class_name__in=clas)
    timetable = TimeTable.objects.all().distinct('time_slot')
    return render(request, "teacher-mark-student-attendence.html", {'students':students,'classes':clas,'sections':section,'subjects':subject,'timetables':timetable})


def view_student_attendace(request):
    t = request.user
    teach = teachers.objects.get(username=t.username)
    att = attendance.objects.all().filter(teacher_id=teach)

    return render(request, "teacher-view-student-attendence.html", {'attendence':att})


def add_student_mark(request):
    return render(request , "teacher-add-student-marks.html")


def teacher_timetable(request):
    return render(request, "teacher-timetable.html")


def view_student_mark(request):
    return render(request, "teacher-view-student-marks.html")


def teacher_attendance_report(request):
    return render(request, "teacher-attendence-report.html")


def teacher_marks_report(request):
    return render(request, "teacher-marks-report.html")


def mark_attendence(request):
    t = request.user
    teach = teachers.objects.get(username=t.username)
    clas = Class.objects.get(class_teacher=teach)
    section = ClassSection.objects.get(class_name=clas)
    stud = Student.objects.all().filter(class_name=clas)
    date = request.POST['date']
    remarks = request.POST['remarks']
    for s in stud:
        student = Student.objects.get(id=request.POST['student_'+str(s.id)])
        is_present = request.POST['ispresent_'+str(s.id)]
        if is_present == 'Present':
            flag = True
        else:
            flag=False
        att  = attendance(teacher_id=teach,class_details=clas,section=section,student=student,date_marked=date,remarks=remarks,is_present=flag)
        att.save()
    return redirect('teacher_attendence_view')