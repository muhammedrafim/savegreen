from django.shortcuts import render

# Create your views here.
def teacher_dashboard(request):
    return render(request, "teacher-dashboard.html")


def create_assignment(request):
    return render(request, "teacher-create-assignment.html")


def download_assignment(request):
    return render(request, "teacher-assignment-download.html")


def mark_student_attendance(request):
    return render(request, "teacher-mark-student-attendence.html")


def view_student_attendace(request):
    return render(request, "teacher-view-student-attendence.html")


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