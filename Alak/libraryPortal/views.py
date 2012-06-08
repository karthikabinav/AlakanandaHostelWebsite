from django.conf import settings
from django.http import Http404
from Alak.libraryPortal import forms
from Alak.home.models import UserProfile
from Alak.misc.util import *
from Alak.libraryPortal.models import *
import datetime
from dateutil.relativedelta import relativedelta

@needs_authentication
def libraryPortal(request):
    return render_to_response('libraryPortal/library.html', locals(), context_instance=global_context(request))

@needs_authentication
def borrowBooks(request):
    if request.method == "POST":
        data = request.POST.copy()
        form = forms.BorrowForm(data)
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        if form.is_valid():
            book = form.cleaned_data["book"]
            book.isVisible = False
            book.save()
            bookorder = BookOrder(user=userprofile,
                              book=book,
                              dateBorrowed=datetime.datetime.now(),
                              dateReturned=None,
                               dueDate=datetime.datetime.now() + relativedelta(days=10))
            bookorder.save()
        
            return render_to_response("libraryPortal/success.html", locals(), context_instance=global_context(request))
        else:
            form = forms.BorrowForm()
            return render_to_response('libraryPortal/borrow.html', locals(), context_instance=global_context(request))
            
    else:
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        listofBooks = Book.objects.filter(isVisible=True)
        try:
            bookBorrowed = BookOrder.objects.get(user=userprofile, dateReturned=None)
            return render_to_response('libraryPortal/alreadyBorrowed.html', locals(), context_instance=global_context(request))
        except:
            
            form = forms.BorrowForm()
            return render_to_response('libraryPortal/borrow.html', locals(), context_instance=global_context(request))
            
@needs_authentication        
def returnBooks(request):
    if request.method == "GET":
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        
        try:
            bookBorrowed = BookOrder.objects.get(user=userprofile, dateReturned=None)
        except:
           bookBorrowed = None
        
        return render_to_response('libraryPortal/return.html', locals(), context_instance=global_context(request))
    else:
        data = request.POST["book"]
        print data
        book = Book.objects.get(id=data)
        book.isVisible = True
        book.save()
        bookorder = BookOrder.objects.get(book=book, dateReturned=None)
        bookorder.dateReturned = datetime.datetime.now()
        bookorder.save()
        return render_to_response('libraryPortal/successfulReturn.html', locals(), context_instance=global_context(request))
        
        
        
        
        
