"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .import views

urlpatterns = [
    # path('',views.trail,name='tr'),
    path('',views.homeview,name='hm'),
    path('hrln',views.hr_login,name='hrln'),
    path('empln',views.emp_login,name='empln'),
    path('hrvw',views.hrview,name='hrvw'),
    path('empvw', views.empview, name='empvw'),
    path('add',views.add_employe,name='add'),
    path('rem',views.emp_remove,name='rem'),
    path('psd',views.change_password,name='psd'),
    path('register',views.register,name='register'),
    path('update',views.password_change,name='update'),
    path('drop',views.delete_employee,name='drop'),
    path('leave',views.leave_form,name='leave'),
    path('psv', views.empl_psd, name='psv'),
    path('upd', views.ps_change, name='upd'),
    path('home',views.home,name="home"),
    path('logoutx',views.logoutx,name="logoutx"),
    path('leaveregister',views.leaveregister,name="leaveregister"),
    path('edata',views.edata,name="edata"),
    path('leaveview',views.leaveview,name="leaveview"),
    path('Approve/<int:lidx>/',views.Approve,name="Approve"),
    path('Deny/<int:lidx>/',views.Deny,name="Deny")

]
