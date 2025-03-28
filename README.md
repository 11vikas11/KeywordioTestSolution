#  Library Management System.
library management system where admin perform CRUD operations and user are able to see the list of book avalability.


## Features
- **Admin operations**
- perform CRUD operations
- admin authentication

- **Authentication**
- Token authontication (JWT)


## project 

- create virtual env.
-- py -m venv myve

- install djngo
--pip install django    :django version :- 5.1.7

- create project
-- django-admin startproject LibraMangSys
-- cd LibraMangSys

- create app
-- py manage.py startapp myApp


- view function created
-- def book_list(request):
      pass

- api functions   : api functions are created using @api_view
--def adminSignup(request):
      pass

--def adminLogin(request):
      pass

--def add_book(request):
      pass
    
--def getBooks(request):
      pass

--def deleteBook(request, book_id):
      pass

--def updateBook(request, book_id):
      pass

- create model class in model.py file
model class define us structure of our schema in database.


- register model class for admin in admin.py file
through which admi can perform crud operation on database

- serializer

- create urls.py file
 add urls for view functions and api functions

- changes in setting.py file
add your app in installed app 
make changes in database

- makemigration
-- py manage.py makemigrations
which analyze the model.py file and create bluprint for migrate command.

- migrate
-- py manage.py migrate
which make changes in databses.


- requirede modules:
from django.shortcuts import render,get_object_or_404
from .models import Book
from django.contrib.auth import get_user_model, authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import AdminUserSerializer,BookSerializer


- run project
-- py manage.py runserver
