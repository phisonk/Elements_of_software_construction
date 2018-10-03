from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
from django.views.generic import View
from user_profile.models import User, UserFollower
from tweets.models import Tweet,HashTag
from tweets.forms import TweetForm,SearchForm
from django.template.loader import render_to_string
from django.template.context import Context
from django.http import HttpResponse
import json

def index(request):
    if request.method == 'GET':
        return HttpResponse('I am called from a get Request')
    elif request.method == 'POST':
        return HttpResponse('I am called from a post Request')


class Index(View):
	def get(self, request):
		params = {}
		params["name"] = "Django"
		return render(request, 'base.html', params)
	def post(self, request):
		return HttpResponse('I am called from a post Request')
class Profile(View): 
	"""User Profile page reachable from /user/<username> URL"""
	def get(self, request, username):
		form = TweetForm()
		params = dict()
		user = User.objects.get(username=username) 
		userFollower = UserFollower.objects.get(user=userProfile)
		if userFollower.followers.filter(username=request.user.username).exists():
			params["following"] = True
		else:
			params["following"] = False
			form = TweetForm(initial={'country': 'Global'})
			search_form = SearchForm()
			tweets = Tweet.objects.filter(user=userProfile).order_by('-created_date')
			params["tweets"] = tweets
			params["profile"] = userProfile
			params["form"] = form
			params["search"] = search_form
			return render(request, 'profile.html', params)
	def post(self, request, username):
		follow = request.POST['follow']
		user = User.objects.get(username= request.user.username)
		userProfile = User.objects.get(username=username)
		userFollower, status = UserFollower.objects.get_or_create     (user=userProfile)
		if follow=='true':
			#follow user
			userFollower.followers.add(user)
		else:
			#unfollow user
			userFollower.followers.remove(user)
		return HttpResponse(json.dumps(""),content_type="application/json")
class PostTweet(View):
	"""Tweet Post form available on page /user/<username> URL"""
	def post(self, request, username):
		form = TweetForm(self.request.POST)
		if form.is_valid():
			user = User.objects.get(username=username)
			print(user)
			tweet = Tweet(text=form.cleaned_data['text'],
			user=user)
			#country=form.cleaned_data['country'])
			tweet.save()
			words = form.cleaned_data['text'].split(" ")
			for word in words:
				if word[0] == "#":
					hashtag, created = HashTag.objects.get_or_create(name=word[1:])
					hashtag.tweet.add(tweet)
			return HttpResponseRedirect('/user/'+username)
		print('fuck')
class HashTagCloud(View):
    """Hash Tag  page reachable from /hastag/<hashtag> URL"""
    def get(self, request, hashtag):
        params = dict()
        hashtag = HashTag.objects.get(name=hashtag)
        params["tweets"] = hashtag.tweet
        return render(request, 'hashtag.html', params)

class Search(View):
    """Search all tweets with query /search/?query=<query> URL"""
    def get(self, request):
        form = SearchForm()
        params = dict()
        params["search"] = form
        return render(request, 'search.html', params)
    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            tweets = Tweet.objects.filter(text__icontains=query)
            context = Context({"query": query,"tweets": tweets})
            return_str = render_to_string('a_tweet_search.html', context.pop())
            return HttpResponse(json.dumps(return_str), content_type="application/json")
        else:
            HttpResponseRedirect("/search")
			
class UserRedirect(View):
	def get(self, request):
		return HttpResponseRedirect('/user/'+request.user.username)
		
class MostFollowedUsers(View):
	def get(self, request):
		userFollowers = UserFollower.objects.order_by('-count')
		params = dict()
		params['userFollowers'] = userFollowers
		return render(request, 'users.html', params)
