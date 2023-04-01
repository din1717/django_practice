from django.urls import URLPattern,path
from .views import StudentView

urlpatterns = [
    path('studentapi',StudentView.as_view())]



