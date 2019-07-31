from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Comment
from .forms import CommentForm

def home(request):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.created = timezone.now()
            comment = comment_form.save()

    comment_form = CommentForm()
    comments = Comment.objects.all()

    return render(request, 'mini/home.html', {'comments':comments, 'comment_form':comment_form})

