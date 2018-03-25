from django.shortcuts import render, get_object_or_404
#bad way to import post model
from .models import Post
# Create your views here.
def home(request):
	#gets all the post objects and order them by date
	#you can also do a reverse negative
	posts = Post.objects.order_by('dateCreated')
	posts =  posts.reverse()
											#after you get them you passsed
											#to the html through a dictionary
	return render(request,'posts/home.html',{'posts':posts})

def post_details(request, post_id):
	#how to get an object from the database
	post  = get_object_or_404(Post, pk = post_id)
	return render(request,'posts/post_detail.html',{'post':post})
