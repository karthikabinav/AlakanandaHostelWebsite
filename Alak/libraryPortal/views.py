from django.conf import settings
from Alak.home.models import *
from Alak.home.views import *
from Alak.libraryPortal import *
import datetime
from dateutil.relativedelta import relativedelta

def getAllBooks():
    book = Book.objects.all()
    return book

@needs_authentication
def borrowBooks(request):
    if request.method == "POST":
        user = request.user
        userprofile = Userprofile.objects.get(user=user)
        bookBorrowed = BookOrder.objects.get(user=userprofile)
        bookBorrowed.book = request.POST['book']
        bookBorrowed.dateBorrowed = datetime.datetime.now()
        bookBorrowed.dueDate = datetime.datetime.now() + relativedelta(days=10)
        
        bookBorrowed.save()
        
        return render_to_response("libraryPortal/success.html")
    else:
        user = request.user
        userprofile = Userprofile.objects.get(user=user)
        listofBooks = getAllBooks()
        bookBorrowed = BookOrder.objects.get(user=userprofile)
        if bookBorrowed.book is None:
            return render_to_response('libraryPortal/borrow.html', locals(), context_instance=global_context(request))
        else:
            return render_to_response('libraryPortal/alreadyBorrowed.html', locals(), context_instance=global_context(request))
