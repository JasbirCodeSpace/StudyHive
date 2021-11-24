from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from ..models import question
import datetime, random
import requests

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

    codechef_data = fetch_codechef_data()
    codeforces_data = fetch_codeforces_data()
    context = {
        'question': new_question,
        'codechef': codechef_data,
        'codeforces': codeforces_data,
    }

    return render(request, 'dsa/dsa.html', context)


def fetch_codechef_data():
    
    api_data = requests.get("https://www.codechef.com/api/list/contests/all?sort_by=START&sorting_order=asc&offset=0&mode=premium").json()

    context = {
        'present_contests': api_data['present_contests'],
        'future_contests': api_data['future_contests'],
    }

    return context

def fetch_codeforces_data():
    api_data = requests.get("https://codeforces.com/api/contest.list?gym=false").json()
    context = [contest for contest in api_data['result'] if contest['phase'] == 'BEFORE']
    return context