from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view),
    path('api/courses/', views.CourseListView.as_view()),
    path('api/courses/<int:pk>/', views.CourseDetailView.as_view()),
    path('api/teachers/', views.TeacherListView.as_view()),
    path('api/lessons/', views.LessonsListView.as_view()),
]
