from django.shortcuts import render


def index(request):
    return render(request=request, template_name='task_4/index.html')
