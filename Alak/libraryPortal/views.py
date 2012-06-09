from django.conf import settings
from django.http import Http404
from django.core.mail import EmailMultiAlternatives
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
                              dueDate=datetime.datetime.now() + relativedelta(days=10),
                              shipped=False)
            bookorder.save()
            """subject, from_email, to = 'Book Borrowed', 'noreply.alakananda@gmail.com', 'raymond.joseph.7@gmail.com'
            text_content = userprofile.user.first_name + " from " + userprofile.room_number + " has borrowed the book " + book.name + " written by " + book.author + ".\n Please deliver the same to him as soon as possible." 
            html_content = "<p>" + userprofile.user.first_name + " from " + userprofile.room_number + " has borrowed the book " + book.name + " written by " + book.author + ".<br/> Please deliver the same to him as soon as possible.</p>"
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()"""
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
        book = Book.objects.get(id=data)
        book.isVisible = True
        book.save()
        bookorder = BookOrder.objects.get(book=book, dateReturned=None)
        bookorder.dateReturned = datetime.datetime.now()
        bookorder.shipped = False
        bookorder.save()
        """subject, from_email, to = 'Book Returned', 'noreply.alakananda@gmail.com', 'raymond.joseph.7@gmail.com'
        text_content = userprofile.user.first_name + " from " + userprofile.room_number + " has returned the book " + book.name + " written by " + book.author + ".\n Please collect the same from him as soon as possible." 
        html_content = "<p>" + userprofile.user.first_name + " from " + userprofile.room_number + " has returned the book " + book.name + " written by " + book.author + ".<br/> Please collect the same from him as soon as possible.</p>"
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()"""
        return render_to_response('libraryPortal/successfulReturn.html', locals(), context_instance=global_context(request))

@needs_authentication
def manageShipping(request):
    querySet = ShippingKey.objects.all()
    for emails in querySet:
        email = emails.email
    
    if request.user.email == email:
        if request.method == "POST":
            data = request.POST["book"]
            book = Book.objects.get(id=data)
            bookorder = BookOrder.objects.get(book=book)
            if bookorder.dateReturned == None:
                type = "borrow"
            else:
                type = "return"
            bookorder.shipped = True
            bookorder.save()
            shippingDetails = Shipping(order=bookorder,
                                       type=type,
                                       shippedOn=datetime.datetime.now(),
                                       shippedBy=UserProfile.objects.get(user=request.user))
            shippingDetails.save()
            return HttpResponseRedirect ("%slibraryPortal/manageShipping" % settings.SITE_URL)
        
        else:
            orderedBooks = BookOrder.objects.filter(shipped=False, dateReturned=None)
            returnedBooks = BookOrder.objects.filter(shipped=False).exclude(dateReturned=None)
            return render_to_response('libraryPortal/shippingDashboard.html', locals(), context_instance=global_context(request))
        
    else:
        raise Http404
