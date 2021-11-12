from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from ..models import question
import datetime, random


@login_required(login_url='/login/')
def index(request):
    today = datetime.datetime.date(datetime.datetime.now())
    new_question = None

    try:
        listed_question = question.ListedQuestion.objects.get(date=today)
        new_question = listed_question.question
        print("Re-Fetching")
    except ObjectDoesNotExist:
        all_questions = question.Question.objects.order_by('?')
        new_question = all_questions.filter(done=False)
        if new_question.count() > 0:
            new_question = new_question[0]
            save_list = question.ListedQuestion(question=new_question, date=today)
            save_list.save()
            new_question.done = True
            new_question.save()
            print("New-Question Fetched")
        else:
            rand_id = random.randint(1, question.Question.objects.count())
            new_question = question.Question.objects.get(id=rand_id)
            qs = question.Question.objects.all()
            qs.update(done=False)
            print("All Question Done")

    context = {
        'question': new_question,
    }

    return render(request, 'dsa/dsa.html', context)
