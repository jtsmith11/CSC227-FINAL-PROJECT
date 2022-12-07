from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
import random
import json


# Create your views here.
def home(request):
    return render(request, 'trivia/home.html')


def quiz(request, genre, question_total):
    if request.method == 'POST':
        trivia_questions = Trivia.objects.all()
        response_data = request.POST

        percentage = 0
        total = 0
        correct = 0
        results_list = []

        print(request.POST)

        for t in trivia_questions:

            # bool value to keep track of if the question is correct
            correct_status = False

            # Check if the question response is correct or not
            if t.correct == response_data.get(str(t.id)):
                correct += 1
                correct_status = True

            if str(t.id) in response_data:
                total += 1

                # Change status to "Correct" or "Incorrect"
                if correct_status is True:
                    status = "Correct"
                else:
                    status = "Incorrect"

                # Append the results list with question, the user's response,
                # the correct answer, and the status
                results_list.append({"question": t.question,
                                     "yourAnswer": response_data.get(str(t.id)),
                                     "correctAnswer": t.correct,
                                     "status": status})

        # Get the percentage correct
        percentage = round(((correct / total) * 100), 2)

        context = {
            'percentage': percentage,
            'total': total,
            'correct': correct,
            'results': results_list
        }

        return render(request, 'trivia/results.html', context)
    else:
        # Set question_total to 1 if anything lower than that is passed
        # to avoid a divide by zero error
        if question_total < 1:
            question_total = 1

        # Check to make sure the specified genre is in the database. If not,
        # set the genre to a random existing genre as a default.
        if Trivia.objects.filter(genre=genre).exists() is False:
            genre = Trivia.objects.all().order_by('?')[0].genre

        # Grab random questions of the specified genre and quiz size
        questions = Trivia.objects.filter(genre=genre).order_by('?')[:int(question_total)]

        order = list()

        x = 1

        for q in questions:
            order.append(x)
            x += 1

        context = {
            'questions': questions,
            'order': order
        }

        return render(request, 'trivia/quiz.html', context)
