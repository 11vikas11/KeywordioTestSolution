from django.shortcuts import render,get_object_or_404
from .models import Book
from django.contrib.auth import get_user_model, authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import AdminUserSerializer,BookSerializer

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/BookList.html', {'books': books})

AdminUser = get_user_model()

# Admin Signup
@api_view(['POST'])
@permission_classes([AllowAny])
def adminSignup(request):
    serializer = AdminUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Admin registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def adminLogin(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = AdminUser.objects.filter(email=email).first()  

    if user and user.username:
        user = authenticate(request, username=user.username, password=password)  

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {"id": user.id, "email": user.email, "username": user.username}
            }, status=status.HTTP_200_OK)

    return Response({"error": "Invalid"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Only logged in admins can add books
def addBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateBook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    serializer = BookSerializer(book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteBook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return Response({"message": "Book deleted successfully"}, status=status.HTTP_200_OK)
