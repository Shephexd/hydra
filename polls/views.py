from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context= {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context=context,request=request))

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    q_date = question.pub_date

    return render(request=request, template_name='polls/detail.html',context={'question':question,'question_date':q_date})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)