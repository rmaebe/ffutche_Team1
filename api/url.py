from django.urls import path
from . import views

app_name = 'ffutche'
urlpatterns = [
    path('school/', views.SchoolListView.as_view(), name='school_list'),
    path('school/<pk>/', views.SchoolDetailView.as_view(), name='school_detail'),
    path('school/<pk>/', views.SchoolDestroyView.as_view(), name='school_destroy'),
    path('school/<pk>/', views.SchoolUpdateView.as_view(), name='school_update'),

    path('scholarship/', views.ScholarshipListView.as_view(), name='scholarship_list'),
    path('scholarship/<pk>/', views.ScholarshipDetailView.as_view(), name='scholarship_detail'),
    path('scholarship/<pk>/', views.ScholarshipDestroyView.as_view(), name='scholarship_destroy'),
    path('scholarship/<pk>/', views.ScholarshipUpdateView.as_view(), name='scholarship_update'),

    path('tuition/', views.TuitionFeeListView.as_view(), name='tuition_list'),
    path('tuition/<pk>/', views.TuitionFeeDetailView.as_view(), name='tuition_detail'),
    path('tuition/<pk>/', views.TuitionFeeDestroyView.as_view(), name='tuition_destroy'),
    path('tuition/<pk>/', views.TuitionFeeUpdateView.as_view(), name='tuition_update'),
]
