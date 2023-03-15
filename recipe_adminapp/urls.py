from django.urls import path
from .import views
# Create your views here.
urlpatterns=[
    path('adminindex/',views.adminindex,name='adminindex'),
    path('addrecipe/',views.addrecipe,name='addrecipe'),
    path('sample/',views.sample,name='sample'),
    path('demo/',views.demo,name='demo'),
    path('view_recipe/',views.view_recipe,name='view_recipe'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('adlogin/',views.adlogin,name='adlogin'),
    path('view_contact/',views.contact,name='contact'),
    path('adlogout/',views.adlogout,name='adlogout')
   
]
