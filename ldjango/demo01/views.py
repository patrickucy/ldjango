from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from .models import Choice, Question
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'demo01/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    mode = Question
    template_name = "demo01/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "demo01/results.html"


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'demo01/index.html', context)


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'demo01/detail.html', {'question': question})


def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'demo01/results.html', {'question': question})


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'demo01/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('demo01:results', args=(question.id,)))
