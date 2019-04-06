from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView

from Test.models import Score


def delete(request, score_id):
    score = Score.objects.get(id=score_id)
    score.delete()
    return redirect(reverse('list'))


def add(request):
    if request.POST:
        # score = Score(studnet_id = request.POST['student_id'],course=request.POST['course_id'],number=request.POST['number'])
        score = Score(student_id=request.POST['student_id'], course_id=request.POST['course_id'],
                      number=request.POST['number'])
        score.save()
        return redirect(reverse('list'))
    else:
        return render(request, 'add.html')


def edit(request, score_id):
    if request.POST:
        score = Score.objects.get(id=request.POST['id'])
        score.number = request.POST['number']
        score.save()
        # return HttpResponse('修改成功')
        return redirect(reverse('list'))
    else:
        lists = Score.objects.filter(id=score_id).first()
        return render(request, 'edit.html', {'lists': lists})
        # return HttpResponse('修改失败')


def test2(request, score_id):
    lists = Score.objects.filter(id=score_id).first()
    return render(request, 'edit.html', {'lists': lists})


class ScoreListView(ListView):
    model = Score
    template_name = 'list.html'
    paginate_by = 8
    context_object_name = 'scores'
    ordering = 'create_time'
    page_kwarg = 'page'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ScoreListView, self).get_context_data(**kwargs)
        print(context)
        return context

    def get_queryset(self):
        return Score.objects.all().order_by('student_id')

    # def get_pate(self):
    #     page_obj = Paginator()
