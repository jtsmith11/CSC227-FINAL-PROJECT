from django.db import models

# Create your models here.
class Trivia(models.Model):
    question = models.CharField(max_length = 500)
    answer_one = models.CharField(max_length = 200)
    answer_two = models.CharField(max_length = 200)
    answer_three = models.CharField(max_length = 200)
    answer_four = models.CharField(max_length = 200)
    correct = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 50)

    def __str__(self):
        return self.question
