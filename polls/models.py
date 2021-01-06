from django.db import models

# Create your models here.
class Question(models.Model):
    #any model u create is going to be a class
    question_text = models.CharField(max_length=200)
    #it will also create an id automatically which will be 
    #our primary key and will be auto incremented by default
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #foreign key to link to the above primary key
    #on_delete=models.CASCADE means if a question is deleted then all its choices will also be deleted
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text