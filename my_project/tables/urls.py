from django.urls import path

from . import views

urlpatterns = [

    

    path('', views.prehome, name='prehome'),
    path('home/', views.home, name='home'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.profile_view, name='profile'),

    path('table/', views.new_form, name='create_table'),
    path('table/<int:pk>/', views.table_page, name = 'table_page'),
    path('table/<int:pk>/edit/', views.edit_form, name='edit_form'),

    path('table23/', views.new_form23, name='create_table23'),
    path('table23/<int:pk>/', views.table_page23, name = 'table_page23'),
    path('table23/<int:pk>/edit/', views.edit_form23, name='edit_form23'),

    path('table26/', views.new_form26, name='create_table26'),
    path('table26/<int:pk>/', views.table_page26, name = 'table_page26'),
    path('table26/<int:pk>/edit/', views.edit_form26, name='edit_form26'),  

    path('export/', views.export_data_to_word, name='export_data_to_word'),
    path('export1/', views.export_data_to_word_for_table20, name='export_data_to_word20'),
    path('export2/', views.export_data_to_word_for_table23, name='export_data_to_word23'),
    path('export3/', views.export_data_to_word_for_table26, name='export_data_to_word26')
]