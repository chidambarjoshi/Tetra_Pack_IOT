from django.urls import path
from . import views


urlpatterns = [
	path('',views.home,name="home"),
	path('datadisplay',views.getdata,name="datadisplay"),
	path('datadisplay1/<pid>',views.getdata1,name="datadisplay1"),
	path('login', views.login, name='login'),
	path('logout',views.logout,name='logout'),
	path('admin_dash',views.admin_dash,name='admin_dash'),
	path('search_pro',views.search_pro,name='search_pro')
]