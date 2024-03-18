from django.urls import path
from work.views import NumbersView

app_name = "prueba"

urlpatterns = [path("analyze", NumbersView.as_view())]
