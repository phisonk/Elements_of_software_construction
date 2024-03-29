"""mytweets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import  include, url 
from django.contrib import admin
from tweets.views import Index, Profile , PostTweet , HashTagCloud ,Search, UserRedirect , MostFollowedUsers
from django.contrib.auth import views as auth_views
admin.autodiscover()


urlpatterns =  [
url(r'^$', Index.as_view()), 
url(r'^user/(\w+)/$', Profile.as_view()),
url(r'^admin/', admin.site.urls),
url(r'^user/(\w+)/post/$', PostTweet.as_view()),
url(r'^hashTag/(\w+)/$', HashTagCloud.as_view()),
url(r'^search/$', Search.as_view()),
url(r'^login/$', auth_views.LoginView.as_view()),
url(r'^logout/$', auth_views.LogoutView.as_view()),
url(r'^profile/$', UserRedirect.as_view()),
url(r'^mostFollowed/$', MostFollowedUsers.as_view())
#url(r'^AJAX/tag/autocomplete/$', AJAX_tag_autocomplete)
]
