from django.conf import settings
from Alak.libraryPortal import forms
from Alak.home.models import UserProfile
from Alak.misc.util import *
from Alak.libraryPortal.models import *
import datetime
from dateutil.relativedelta import relativedelta

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
                               dueDate=datetime.datetime.now() + relativedelta(days=10))
            bookorder.save()
        
            return render_to_response("libraryPortal/success.html")
        else:
            form = forms.BorrowForm()
            return render_to_response('libraryPortal/borrow.html', locals(), context_instance=global_context(request))
            
    else:
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        listofBooks = Book.objects.filter(isVisible=True)
        try:
            bookBorrowed = BookOrder.objects.get(user=userprofile)
            return render_to_response('libraryPortal/alreadyBorrowed.html', locals(), context_instance=global_context(request))
        except:
            
            form = forms.BorrowForm()
            return render_to_response('libraryPortal/borrow.html', locals(), context_instance=global_context(request))
            
