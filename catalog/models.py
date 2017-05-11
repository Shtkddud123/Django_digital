from __future__ import unicode_literals
from django.db import models
from django.urls import reverse 
import uuid

#class POST(models.model):
#    A = A
#    B = B
#    C = C

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

class Tag(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField()

class Student(models.Model):
    """
    Database for a student database
    """
    FRESHMAN = "FR"
    SOPHOMORE = "SO"
    JUNIOR = "JR"
    SENIOR = "SR"
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length = 2,
        choices = YEAR_IN_SCHOOL_CHOICES,
        default = FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)


class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction)
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    
class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book)
    """
    title = models.CharField(max_length=200)
#    author = models.ForeignKey('Author', on_delete= models.SET_NULL, null=True)
    isbn = models.CharField('ISBN', max_length=13, help_text = '13 Character <a href "https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre,help_text="Select a genre for this book")

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.title

    
class BookInstance(models.Model):
    """
    Model representing a book (but not a specific copy of a book)
    """
    # Universally unique identifiers 
    title = models.CharField(max_length=200)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('d', 'Maintenence'),
        ('o', 'On Loan'),
        ('a', 'Avaliable'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices = LOAN_STATUS, blank=True, default='d', help_text = 'Book avaliability')

# We need to look at a specific copy of a book

    
class Question(models.Model):
    """
    Question model choice for the sqlite 
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
class Paper_database(models.Model):
    title = models.CharField(max_length=200) # CharField - short-to-mid sized fixed-length strings 
    slug = models.SlugField() # can only contain lowercase alphanumeric characters 
    text = models.TextField() # large arbirtrary length strings 
    pub_date = models.DateField() # DD/MM/YY/ 
    email = models.EmailField()
    def get_absolute_url(self):
        """
        Returns the url access a particular instance of the model 
        """
        return reverse('model-detail-view', args=[str(self.id)])
    
class MyModelName(models.Model):
    """
    A typical class defining a model, derived from the Model class 
    """
    # Fields
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")

    # Metadata

    # Model-level data for your model by declaring class Meta
    # order by my field name field of the data 
    class Meta:
        ordering = ["-my_field_name"]
    #Methods:
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName 
        """
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name 
