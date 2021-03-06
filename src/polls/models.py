from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
# These are models to be used by a database!
@python_2_unicode_compatible
class Question(models.Model):
    
    def __str__(self):
        return self.question_text
    
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    priority = models.IntegerField('question priority', default=3)
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

@python_2_unicode_compatible    
class Choice(models.Model):
    
    def __str__(self):
        return self.choice_text
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)