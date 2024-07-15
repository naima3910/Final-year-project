from django.urls import path, re_path
from .views import Meds, index

app_name = 'patientmeds'

urlpatterns = [
    path('', index, name='index'),
    path('api/meds/', Meds.as_view(), name='meds'),  # Ensure the correct path here
    re_path(r'^api/meds/(?P<patientmeds_id>[0-9a-fA-F]{24})/$', Meds.as_view(), name='meds_detail'),
]
