from django.urls import path
from app.views import *
app_name='jesus'

urlpatterns=[
    path('jesus/',jesus,name='jesus'),
]