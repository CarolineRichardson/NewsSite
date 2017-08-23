from django import forms
from models import Article
from models import Brickout


class ArticleForm(forms.ModelForm):
   
   class Meta:
      model = Article
      fields = ('title', 'body')
      

class BrickoutForm(forms.Form):
   score = forms.DecimalField(decimal_places=None, label="score") 
