from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/student-dashboard.html', views.studnet_dashboard),
    path('dashboard/student-assignment-download.html', views.student_assignmnet_download),
    path('dashboard/student-assignment-upload.html', views.student_assignmnet_upload),
    path('dashboard/student-attendence.html', views.student_attendance),
    path('dashboard/student-attendence-detailed.html', views.student_attendance_detailed),
    path('dashboard/student-marks.html', views.student_marks),
    path('dashboard/student-exam-plan.html', views.student_examination_seating),
    path('dashboard/student-exam-schedule.html', views.student_examination_schedule),
    path('dashboard/student-fees.html', views.student_fees_details)
]