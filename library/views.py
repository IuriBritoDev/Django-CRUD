from django.shortcuts import render, redirect
from .models import Book
from .forms import BookRegistration


def home(request):
    books = Book.objects.all()
    
    return render(request, 'library/home.html', {'books': books})


def create(request):
    form = BookRegistration(request.POST)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'library/home.html', {'books': books})


def read(request):
    books = book.objects.all()

    return render(request, 'library/home.html', {'books': books})


def update(request, id):
    book = Book.objects.get(pk = id)
    form = BookRegistration(request.POST, instance=book)
    
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'library/home.html', {'books': books})


def delete(required, id):
    delBock = Book.objects.get(pk = id)
    delBook.delete()

    return redirect('home')