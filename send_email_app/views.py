from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, User


def home(request):
    return render(request, 'send_email_app/home.html')


def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False)
    except User.DoesNotExist:
        raise Http404("User does not exist or is already verified")
 
    user.is_verified = True
    user.save()
 
    return redirect('home')


class PostDetailView(generic.View):

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        post.view_count += 1
        post.save()

        context = {'post': post}
        return render(request, 'send_email_app/post_detail.html', context)