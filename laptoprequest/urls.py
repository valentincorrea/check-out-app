
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('computers/', views.computers, name='computers'),
    path('computers/<int:id>/', views.computer_detail, name='computer_details'),
    path('request/', views.request_form, name='request'),
    path('search_request/', views.search_request, name='search_request'),
    path('student_request_view/', views.student_view, name='student_view'),
    path('teacher_view/', views.teacher_view, name='teacher_view'),
    path('approve_request/<int:id>/', views.approve_request, name='approve_request'),
]


