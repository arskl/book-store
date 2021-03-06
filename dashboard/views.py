from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
import logging
import os

logger = logging.getLogger(__file__)
logger.debug("This logs a debug message.")
logger.info("This logs an info message.")
logger.warn("This logs a warning message.")
logger.error("This logs an error message.")

def parser():
    file = open("debug.log", "r")
    log_list = []
    for line in file:
        if line.startswith('20'):
            log_list.append(str(line))
    for line in log_list:
        check = '302'
        Logger(log=line).save()
        if check in line:
            CrudLogger(crud_log=line).save()

# Create your views here.
class Dashboard(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'dashboard/dashboard.html'

class Admin(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'dashboard/admin.html'

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('admin')

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('admin')

class BookDelete(DeleteView):
    model = Book
    context_object_name = 'books'
    template_name = 'dashboard/book_delete.html'
    success_url = reverse_lazy('admin')

def bookManipulationLog(request):
    CrudLogger.objects.all().delete()
    parser()
    logs = CrudLogger.objects.all().order_by('crud_log')
    context = {'logs': logs}
    return render (request, 'dashboard/books-manipulation-log.html', context)


def httpRequestLog(request):
    Logger.objects.all().delete()
    parser()
    logs = Logger.objects.all().order_by('-log')[:10]
    context = {'logs': logs}
    return render (request, 'dashboard/http-request-log.html', context)
