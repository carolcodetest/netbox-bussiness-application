from django.urls import path, include
from utilities.urls import get_model_urls

from . import views

urlpatterns = [
    path('business-application/', views.BusinessApplicationListView.as_view(), name='businessapplication_list'),
    path('business-application/<int:pk>/', views.BusinessApplicationDetailView.as_view(), name='businessapplication_detail'),
    path('business-application/add/', views.BusinessApplicationCreateView.as_view(), name='businessapplication_add'),
    path('business-application/<int:pk>/edit/', views.BusinessApplicationEditView.as_view(), name='businessapplication_edit'),
    path('business-application/<int:pk>/delete/', views.BusinessApplicationDeleteView.as_view(), name='businessapplication_delete'),
    path('business-application/<int:pk>/', include(get_model_urls('business_application', 'businessapplication')))
]
