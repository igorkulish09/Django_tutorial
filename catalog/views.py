from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from django.shortcuts import render, get_object_or_404, redirect
from .forms import PersonForm
from .models import Person

from .models import Choice, Question

from .forms import TriangleForm

from django.views import View

import math


class IndexView(generic.ListView):
    template_name = "catalog/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return all questions."""
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = "catalog/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "catalog/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "catalog/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("catalog:results", args=(question_id,)))



def triangle(request):
    gip = None

    if request.method == "POST":
        form = TriangleForm(request.POST)
        if form.is_valid():
            cathetus1 = form.cleaned_data["cathetus1"]
            cathetus2 = form.cleaned_data["cathetus2"]
            gip = math.sqrt(cathetus1**2 + cathetus2**2)
    else:
        form = TriangleForm()

    return render(request, "catalog/triangle.html", {"form": form, "gip": gip})


def create_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("person_list")
    else:
        form = PersonForm()
    return render(request, "catalog/person_form.html", {"form": form})


def update_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("person_list")
    else:
        form = PersonForm(instance=person)
    return render(request, "catalog/person_form.html", {"form": form})


class PersonCreateView(View):
    def get(self, request):
        form = PersonForm()
        return render(request, "catalog/person_form.html", {"form": form})

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        return render(request, "catalog/person_form.html", {"form": form})


class PersonUpdateView(View):
    def get(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        form = PersonForm(instance=person)
        return render(
            request, "catalog/person_form.html", {"form": form, "person": person}
        )

    def post(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("catalog:index")
        return render(
            request, "catalog/person_form.html", {"form": form, "person": person}
        )
