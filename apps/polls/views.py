from django.contrib.auth.models import User, Group
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views import View
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, views
# from django_polls.polls import Question, Choice


#
# def index(request):
#     # 在视图中操作数据库
#     try:
#         man_list = Man_Model.objects.all().filter(age=25)
#         # print(man_list)
#         for man in man_list:
#             print(man.plant_model_set.all)
#         # name = man.name
#     # return HttpResponse(man)
#     except:
#         raise Http404("Man_Model does not exist")
#     # name = get_object_or_404(Man_Model, id=3)
#     # 尝试用 get() 函数获取一个对象，如果不存在就抛出 Http404 错误也是一个普遍的流程
#     return render(request, 'index.html', {"man": man_list})
# 模板渲染
# from django_polls.polls.models import Question, Choice
from apps.polls.models import Question, Choice, Man_Model
from apps.polls.serializers import ManSerializer, UserSerializer, GroupSerializer


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # print(context)
    return render(request, 'index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # selected_choice = question.choice_set.get(pk=request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})


class ManListView(View):
    def get(self, request):
        mans = Man_Model.objects.all()
        serializers = ManSerializer(mans, many=True)
        data = serializers.data
        return render(request, 'man_list.html', {"man_list": data})


class ManView(View):
    def get(self, request):
        mans = Man_Model.objects.all()
        serializers = ManSerializer(mans, many=True)
        data = serializers.data
        print(type(data))
        # JsonResponse在抛出列表的时候需要将safe设置为False safe=False
        return JsonResponse(data=data, safe=False, json_dumps_params={'ensure_ascii': False})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
