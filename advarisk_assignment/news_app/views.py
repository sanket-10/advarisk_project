from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
# Create your views here.
from .models import Keyword, SearchResult
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .news_api import fetch_news
from django.utils import timezone
from datetime import datetime , timedelta


def signup(request):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        conform_password = request.POST['pass2']
        if password != conform_password:
            messages.warning(request,"Password is not matching")
            return render(request,'signup.html')

        try:
            if User.objects.get(username=email):
                messages.info(request,"User already exists")
                return render(request,"signup.html")
        except Exception as identifier:
            pass

        user = User.objects.create_user(email,email,password)
        user.save()
        messages.info(request,"User created successfully!")
        return render(request,"login.html")


    return render(request,'signup.html')

def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        userpassword = request.POST['password']
        myuser = authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successfully")
            return redirect('search_news')

        else:
            messages.warning(request,'Invalid creditials...Try Again!!')
            return render(request,'login.html')

    return render(request,'login.html')


def handlelogout(request):
    logout(request)
    messages.info(request,"log out successfully")
    return redirect('/')



@login_required
def search_news(request):
    if request.method == 'POST':
        keyword_phrase = request.POST.get('keyword')
        user = request.user
        # Check if the user has searched for the same keyword in the last 15 minutes
        threshold_time = timezone.now() - timedelta(minutes=15)
        recent_search = Keyword.objects.filter(user=user, phrase=keyword_phrase, created_date=threshold_time).first()

        if recent_search:
            messages.warning(request, f'You have already searched for "{keyword_phrase}" within the last 15 minutes.')
        else:
            # Check if the keyword already exists for the user
            existing_keyword = Keyword.objects.filter(user=user, phrase=keyword_phrase).first()

            if existing_keyword:
                keyword = existing_keyword
            else:
                keyword = Keyword.objects.create(user=user, phrase=keyword_phrase)
            search_results = fetch_news(keyword_phrase)  # Implement this function to fetch news using News API


            for result in search_results:
                SearchResult.objects.create(keyword=keyword, title=result['title'], url=result['url'], date_published=result['date'])

            messages.success(request, 'Search results saved.')

    keywords = Keyword.objects.filter(user=request.user,)
    return render(request, 'search.html', {'keywords': keywords})

@login_required
def view_results(request, keyword_id):
    keyword = Keyword.objects.get(id=keyword_id)
    search_results = SearchResult.objects.filter(keyword=keyword,is_active=True).order_by('-date_published')
    return render(request, 'results.html', {'keyword': keyword, 'search_results': search_results})
