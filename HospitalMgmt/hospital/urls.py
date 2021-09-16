from django.urls import path
from hospital.views import *

urlpatterns = [
    
    path('home/', Index,name='home'),
    path('',Index,name='home'),
    path('admin_login/',Login,name='login')

    
    

]
