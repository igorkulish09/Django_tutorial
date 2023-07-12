from django.urls import path, include
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("triangle/", views.triangle, name="triangle"),
    path("person/", views.PersonCreateView.as_view(), name="create_person"),
    path("person/<int:pk>/", views.PersonUpdateView.as_view(), name="update_person"),
]
