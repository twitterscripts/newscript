from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .models import BugReport
from .forms import PostForm
from .forms import ReportForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def report_list(request):
    reports = BugReport.objects.filter(published_dater__lte=timezone.now()).order_by('published_dater')
    return render(request, 'blog/report_list.html', {'reports': reports})

# Create your views here.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def the_script(request):
    return render(request, 'blog/script.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def report_new(request):
    if request.method == "POST":
        report = ReportForm(request.POST)
        if report.is_valid():
            report = report.save(commit=False)
            report.published_dater = timezone.now()
            report.save()
            return redirect('report_list')
    else:
        report = ReportForm()
    return render(request, 'blog/report_edit.html', {'report': report})