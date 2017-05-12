from django.shortcuts import render
from django.views import generic 
from .models import Student, Book, Tag
"""
Adding list and detail pages for books and authors - URL maps, views and templates are still required. 
Extract information from the URL --> and pass it into the view
"""
#class BookListView(generic.ListView):
#    model = Book
#    context_object_name = 'my_book_list'
#    queryset = Book. 
def homepage(request):
    """
    True home page 
    """
    tag_list = Tag.objects.all()
    html_output = "<html\n"
    html_output = "<head>\n"
    html_output = "<title>"

def index(request):
    """
    View function for home page of site
    """
    # Some of the main models we want to work with in the views webpage
    
    num_books = Book.objects.all() # The number of books in the database
    num_students = Student.objects.all() # The number of students in the database 

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',    
        context = {'num_books':num_books, 'num_students':num_students},
    )

#def science(request):
#    """
#    Talking about science 
#    """
#    return render (
#        request,
#        'science.html',
#        context = {},
#)
