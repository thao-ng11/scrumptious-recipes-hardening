# from django.shortcuts import render
from distutils.log import Log
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


from meal_plans.models import MealPlan

# Create your views here.


class MealPlansListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "meal_plans/list.html"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlansDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "meal_plans/detail.html"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlansCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "meal_plans/create.html"
    fields = ["name", "recipes", "date"]
    success_url = reverse_lazy("meal_plans_list")

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()
        return redirect("meal_plans_detail", pk=plan.id)


class MealPlansUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "meal_plans/edit.html"
    fields = ["name", "recipes", "date"]
    success_url = reverse_lazy("meal_plans_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlansDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "meal_plans/delete.html"
    success_url = reverse_lazy("meal_plans_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)
