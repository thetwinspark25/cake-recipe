from django.urls import path
from .import views
urlpatterns=[
    path('userindex/',views.userindex,name='userindex'),
    path('view_rec/',views.view_rec,name='view_rec'),
    path('recipe_detail/<int:id>',views.recipe_detail,name='recipe_detail'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]