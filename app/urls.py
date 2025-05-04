from django.urls import path
from .views import RegisterView,PatientListCreateView,PatientDetailView,DoctorListCreateView,DoctorDetailView,MappingListCreateView,MappingByPatientView,MappingDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #authentication
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #patients
    path('patients/', PatientListCreateView.as_view(),name="patient_list_create"),
    path('patients/<int:pk>/', PatientDetailView.as_view(),name="patient_delete"),

    #doctors
    path('doctors/', DoctorListCreateView.as_view(),name="doctor_list_create"),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(),name="doctor_detail"),

    #mapping
    path('mappings/', MappingListCreateView.as_view()),
    path('mappings/<int:patient_id>/', MappingByPatientView.as_view()),
    path('mappings/delete/<int:pk>/', MappingDeleteView.as_view()),


]
