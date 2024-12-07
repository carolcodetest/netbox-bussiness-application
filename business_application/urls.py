from django.urls import path
from . import views

urlpatterns = [
    path('', views.BusinessApplicationListView.as_view(), name='businessapplication_list'),
    path('<int:pk>/', views.BusinessApplicationDetailView.as_view(), name='businessapplication_detail'),
    path('add/', views.BusinessApplicationCreateView.as_view(), name='businessapplication_add'),
    path('<int:pk>/edit/', views.BusinessApplicationEditView.as_view(), name='businessapplication_edit'),
    path('<int:pk>/delete/', views.BusinessApplicationDeleteView.as_view(), name='businessapplication_delete'),
]
