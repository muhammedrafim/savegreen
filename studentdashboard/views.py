from django.shortcuts import render

# Create your views here.
def studnet_dashboard(request):
    return render(request, "student-dashboard.html")


def student_assignmnet_download(request):
    return render(request, "student-assignment-download.html")


def student_assignmnet_upload(request):
    return render(request, "student-assignment-upload.html")


def student_attendance(request):
    return render(request, "student-attendence.html")


def student_attendance_detailed(request):
    return render(request, "student-attendence-detailed.html")


def student_marks(request):
    return render(request, "student-marks.html")


def student_examination_seating(request):
    return render(request, "student-exam-plan.html")


def student_examination_schedule(request):
    return render(request, "student-exam-schedule.html")


def student_fees_details(request):
    return render(request, "student-fees.html")