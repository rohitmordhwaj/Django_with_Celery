from django.shortcuts import render
from django.http import HttpResponse
from . task import add
from send_mail_app.task import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
from .signal import notification
# Create your views here.
def test(request):
    notification.send(sender=None, request=request, abc = ["abc", "jnwjndw"])
    add.delay(10, 20)
    return HttpResponse("DONE TASK")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 22, minute = 46)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+str(schedule.id), task='send_mail_app.tasks.send_mail_func')
    return HttpResponse("Done")