from django.db import models


# Create your models here.
class Question(models.Model):
    """This class used to represent question objects
    Attributes:
        question_text(str): Description of the question
        pub_date: Published date of the question
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """This is the documentation for the __str__ method.
            :returns: question_text
        """
        return self.question_text


class Choice(models.Model):
    """This class used to represent choice of the questions
    Attributes:
        question(str): Description of the question, it is foreign key
        choice_text(str): Choice of the question
        votes(int): posted vote number, default to 0
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """This is the documentation for the __str__ method.
            :returns: choice_text
        """
        return self.choice_text
