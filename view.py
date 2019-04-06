from django.db.models import Avg, Count, Sum, Min, Max, Q, F
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.views import View

from Test.models import Student, Score, Teacher, Course

from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_safe

from ormtest import form
from ormtest.form import MessageBoardForm, Myform


@require_http_methods(['GET'])
def my_view(request):
    pass


@require_GET
def my_view1(request):
    pass


@require_POST
def my_view2(request):
    pass


@require_safe
def my_view(request):
    pass


def hello(request):
    context = {}
    # 查询平均成绩大于60分的同学的id和平均成绩；
    # context['names'] = Student.objects.annotate(avg = Avg('score__number')).filter(avg__gte=60).values('id','avg')
    # 查询所有同学的id、姓名、选课的数、总成绩；
    context['names'] = Student.objects.annotate(course_nums=Count('score__course'),
                                                total_score=Sum('score__number')).values('id', 'name', 'course_nums',
                                                                                         'total_score')


    # 查询姓“李”的老师的个数
    # context['name'] = Teacher.objects.filter(name__startswith= '李').count()
    # 查询姓名中有“李”的老师
    # context['name'] = Teacher.objects.filter(name__contains='李').count()
    # 查询没学过“黄老师”课的同学的id、姓名；
    # context['names'] = Student.objects.exclude(score__course__teacher__name='黄老师').values('id','name')
    # 查询学过课程id为1和2的所有同学的id、姓名；
    # context['names'] = Student.objects.filter(score__course__in=[1,2]).distinct().values('id','name')
    # 查询学过“黄老师”所教的所有课的同学的学号、姓名；
    # context['names'] = Student.objects.annotate(num = Count('score__course',filter = Q(score__course__teacher__name = '黄老师'))).filter(num = Course.objects.filter(teacher__name = '黄老师').count()).values('id','name')
    # 查询所有课程成绩小于60分的同学的id和姓名；
    # context['names'] = Student.objects.exclude(score__number__gt = 60)
    # 查询没有学全所有课的同学的id、姓名
    # context['names'] = Student.objects.annotate(num = Count(F('score__course'))).filter(num__lt = Course.objects.count()).values('id','name','num')
    # 查询所有学生的姓名、平均分，并且按照平均分从高到低排序
    # context['names'] = Student.objects.annotate(avg = Avg('score__number')).order_by('-avg').values('name','avg')
    # 查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分：
    # context['names'] = Course.objects.annotate(min = Min('score__number'),max = Max('score__number')).values("id",'nname','min','max')
    # 查询每门课程的平均成绩，按照平均成绩进行排序；
    # context['names'] = Course.objects.annotate(avg = Avg('score__number')).order_by('avg').values('id','name','avg')
    # 统计总共有多少女生，多少男生
    # context['name'] = Student.objects.aggregate(male_num = Count('gender',filter = (Q(gender = 1))),female_num = Count('gender',filter = (Q(gender= 2))))
    # 将“黄老师”的每一门课程都在原来的基础之上加5分；
    # context['name'] = Score.objects.filter(course__teacher__name = '黄老师').update(number = F('number')+5)
    # 查询两门以上不及格的同学的id、姓名、以及不及格课程数；
    # context['names'] = Student.objects.annotate(bad_count = Count('score__number',filter = Q(score__number__lt=60))).filter(bad_count__gte = 1).values('id','name','bad_count')
    # 查询每门课的选课人数
    # context['names'] = Course.objects.annotate(student_num = Count('score__student')).values('id','nname','student_num')
    return render(request, 'hello.html', context)

    # results = Score.objects.all()
    # for result in results:
    #     print(1)
    #     print(result.id,result.student.name,result.course.nname,result.number)
    # return redirect('/listview')


class IndexView(View):
    def get(self, request):
        form = MessageBoardForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = MessageBoardForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            # print(title)
            return HttpResponse('success')
        else:
            # print(form.errors)
            # print(form.errors.get_json_data())
            # print(form.errors.as_json)
            return HttpResponse('fail')

class ModelView(View):
    def get(self,request):
        form = Myform()
        return render(request,'modelform.html',{'form':form})
    def post(self,request):

        form = Myform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            print(form.errors)
            print(form.errors.get_json_data())
            print(form.errors.as_json)
            return HttpResponse('fail')

def ImageView(request):
    return render(request,'image.html')