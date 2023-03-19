from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

# Create your views here.


def home(request):
    """Function responds to website root HTTP requests

        :returns: home.html template
    """
    return render(request, 'climate/home.html')


def about(request):
    """Function responds to website root HTTP requests

        :returns: about.html template
    """
    return render(request, 'climate/about.html')


def survey(request):
    """Function responds to website root HTTP requests

        :returns: survey.html template that shows the list of questions from database
    """
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'climate/survey.html', context)


def detail(request, question_id):
    """Function responds to website root HTTP requests

        :param int question_id: id number and primary key of each question
        :returns: detail.html template that shows the requested question and its options from database
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'climate/detail.html', {'question': question})


def result(request, question_id):
    """Function responds to website root HTTP requests

       :param int question_id: id number and primary key of each question
       :returns: result.html template that shows the result of the survey of voted question from database
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'climate/result.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )

    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form
        return render(request, 'climate/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice!"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        #Return an HttpResponseRedirect after successfully dealing with POST data to prevent data from being
        #posted twice if a user hits the Back button.
        return HttpResponseRedirect(
            reverse('climate:result', args=(question_id,))
        )


