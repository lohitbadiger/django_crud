from django.urls import path 

from . import views
urlpatterns = [
    path('',views.home, name='home-all-items'),
    path('create',views.create_info, name='create_info'),
    path('update/<int:id>',views.update_info, name='update_info'),
    path('delete/<int:id>',views.delete_info, name='delete_info'),
    
    
]