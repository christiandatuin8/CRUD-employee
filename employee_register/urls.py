from django.urls import path, include
from . import views

urlpatterns = [


    # get and post request for insert opr
    path('', views.employee_form, name='employee_insert'),

    # get and post request for update opr
    path('<int:id>/', views.employee_form, name='employee_update'),

    # get request to retrieve and display all records
    path('list/', views.employee_list, name='employee_list'),

    # delete
    path('delete/<int:id>/', views.employee_delete, name='employee_delete')

]
