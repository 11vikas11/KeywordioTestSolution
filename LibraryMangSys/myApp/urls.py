from django.urls import path
from . import views

urlpatterns = [
    path('booklist/',views.book_list),
    path('signup/', views.adminSignup),
    path('login/', views.adminLogin),
    path('add/', views.addBook),
    path('update/<int:book_id>/', views.updateBook),
    path('delete/<int:book_id>/', views.deleteBook),
   

]