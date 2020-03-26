from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/teacher-dashboard.html', views.teacher_dashboard),
    path('dashboard/teacher-create-assignment.html', views.create_assignment),
    path('dashboard/teacher-assignment-download.html', views.download_assignment),
    path('dashboard/teacher-mark-student-attendence.html', views.mark_student_attendance),
    path('dashboard/teacher-view-student-attendence.html', views.view_student_attendace),
    path('dashboard/teacher-add-student-marks.html', views.add_student_mark),
    path('dashboard/teacher-timetable.html', views.teacher_timetable),
    path('dashboard/teacher-view-student-marks.html', views.view_student_mark),
    path('dashboard/teacher-attendence-report.html', views.teacher_attendance_report),
    path('dashboard/teacher-marks-report.html', views.teacher_marks_report)
]