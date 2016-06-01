from django.shortcuts import render
# from .models import Message


def home(request):
    # messages = Message.objects.order_by('order')
    messages = ['hello', 'world', "I'm here"]
    context_dict = {
        'messages': messages
    }
    return render(request, 'starter_app/home.html', context_dict)
