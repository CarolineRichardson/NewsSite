from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse
from django.template import Context
from news_app.models import Article
from news_app.forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from news_app.forms import BrickoutForm
from news_app.models import Brickout
from news_app.models import Messages
from django.contrib.auth.models import User
#from django.views.generic.edit import UpdateView




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/loggedIn/")
    else:
        form=UserCreationForm()

    return render(request,"registration/register.html",{'form':form})


#welcome page
def welcome(request):
    return render(request, 'welcome.html')




#cover page of site
def main(request):
    return render(request, 'main.html')


	
#about page
def about(request):
    return render(request, 'about.html')



    
    
#@login_required    
#def brickout(request):
#    return render(request, 'brickout.html')    
    
    
    
    
    
#@login_required    
#def ArticleUpdateView(UpdateView):
#    model = Article
#    form_class = ArticleForm      
       
        
    
    
    
    
    
    
    
def logout(request):
  return render(request, 'logout.html')   
                              

    
#messages profile  
@login_required
def loggedIn(request):
    n = Messages.objects.filter(user = request.user.id, viewed=False)
    return render_to_response('loggedIn.html',
                              {'username': request.user.username,
                               'messages':n})










#display all articles
@login_required
def articles(request):
    
    return render_to_response('articles.html', 
                             {'articles' : Article.objects.all() })


							 
#show article 
@login_required
def article(request, article_id=1):
    return render_to_response('article.html',
                             {'article': Article.objects.get(id=article_id) } )





@login_required
def create(request):
   if request.POST:
       form = ArticleForm(request.POST, request.FILES)
       username = request.user.username
       if form.is_valid():
           instance = form.save(commit=False)
           instance.username = request.user
           instance.save()
   	
           #form.save()
           #python manage.py syncdb
           return HttpResponseRedirect('/articles/all')
   else:
      form = ArticleForm()

   args = {}
   args.update(csrf(request))

   args['form'] = form

   return render_to_response('create_article.html', args)




@login_required
def like_article(request, article_id):
   if article_id:
       a = Article.objects.get(id=article_id)
       count = a.likes
       count += 1
       a.likes = count
       a.save() 
       

       return HttpResponseRedirect('/articles/get/%s' % article_id)
   
   
   
   
 
#@login_required
#def add_comment(request, article_id):
#   a = Article.objects.get(id=article_id)
#      
#   
#   if request.method == "POST":
#       f = CommentForm(request.POST)
#       if f.is_valid():
#           c = f.save(commit=False)
#           c.pub_date = time.now()
#           c.article = a
#           c.save()
#       
#           return HttpResponseRedirect('/articles/get/%s' % article_id)  
#   
#   else:
#       f = CommentForm()
#       
#   args = {}
#   args.update(csrf(request))
#   
#   args['article'] = a
#   args['form'] = f
#   
#   
#   return render_to_response('add_comment.html', args) 
   
   
   
   
   






#brickout game works - score does not sync
@login_required
def brickout(request):
    form = BrickoutForm()

    currentScore = 0
    return render(request, 'brickout.html', {'form':form, 'currentScore':currentScore})

    currentScore = sd.getScore()

    return render(request, 'brickout.html', {'form':form, 'currentScore':currentScore})




def addBrickoutData(request):
    if request.method == 'POST':
        form = BrickoutForm(request.POST)

        if (form.is_valid()):
            cd = form.cleaned_data

           #get score
            try:
               sd = Brickout.objects.get(score = cd['score'])

          
            except Brickout.DoesNotExist:
                sd = Brickout(score=cd['score'])
                sd.save()

                return render(request, 'brickout.html', {'form':form, 'currentScore':cd['score']})

            currentScore = sd.getScore()

            #update
	    if (cd['score'] > currentScore):
                sd = Brickout(score=cd['score'])
                sd.save()
		currentScore = cd['score']

            else:
                print("not enough")


    return render(request, 'brickout.html', {'form':form, 'currentScore':currentScore})

    
    
    
    
    
    
def show_messages(request, messages_id):
    n = Messages.objects.get(id=messages_id)
    return render_to_response('messages.html', {'messages':n})
            
    
    
def delete_messages(request, messages_id):
    n = Messages.objects.get(id=messages_id)
    n.viewed = True
    n.save()
    
    return HttpResponseRedirect('/accounts/profile')    
    
    
    
      
    
    
    
    
    
    
    







