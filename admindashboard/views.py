from django.shortcuts import render

# Create your views here.
def admindashboard(request):
    return render(request, 'admin-dashboard.html')


def admin_add_student(request):
    return render(request, 'admin-add-student.html')


def admin_studentlist(request):
    return render(request, 'admin-student-list.html')


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