from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.


def post_list_view(request):
    post_list = Post.objects.all()

    '''creating paginator'''

    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'post_list': post_list})


def post_details_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    return render(request, 'blog/post_details.html', {'post': post})

from django.core.mail import send_mail
from blog.forms import EmailSendform


def mail_send_view(request, id):
    post = get_object_or_404(Post, id=id, status='published')
    form = EmailSendform()
    return render(request, 'blog/sharebyemail.html', {'form':form, 'post':post})







