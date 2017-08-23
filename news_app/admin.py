from django.contrib import admin



from news_app.models import Article
admin.site.register(Article)


from news_app.models import Brickout
admin.site.register(Brickout)


from news_app.models import Messages
admin.site.register(Messages) 
