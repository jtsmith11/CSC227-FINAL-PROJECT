from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'trivia/home.html')


def quiz(request, genre = 'history', question_total = '20'):
    if request.method == 'POST':
        trivia_questions = Trivia.objects.all()
        response_data = request.POST

        percentage = 0
        total = 0
        correct = 0

        for t in trivia_questions:

            if t.correct ==  response_data.get(str(t.id)):
                correct+=1

            if str(t.id) in response_data:
                total+=1

        percentage = round(((correct / total) * 100), 2)

        context = {
            'percentage':percentage,
            'total':total,
            'correct':correct,
        }

        return render(request, 'trivia/results.html', context)
    else:
        questions = Trivia.objects.filter(genre=genre).order_by('?')[:int(question_total)]

        order = list()

        x = 1

        for q in questions:
            order.append(x)
            x += 1

        context = {
            'questions':questions,
            'order':order
        }

        return render(request, 'trivia/quiz.html', context)
