from django.conf.urls.defaults import patterns, url, include

from reviews.views import delete as amo_delete
from reviews.feeds import ReviewsRss

from . import views


# These all start with /apps/<app_slug>/reviews/<review_id>/.
detail_patterns = patterns('',
    url('^$', views.review_list, name='ratings.detail'),
    url('^flag$', views.flag, name='ratings.flag'),
    url('^delete$', amo_delete, name='ratings.delete'),
    url('^edit$', views.edit, name='ratings.edit'),
    url('^reply$', views.reply, name='ratings.reply'),
)


review_patterns = patterns('',
    url('^$', views.review_list, name='ratings.list'),
    url('^add$', views.add, name='ratings.add'),
    url('^(?P<review_id>\d+)/', include(detail_patterns)),
    url('^format:rss$', ReviewsRss(), name='ratings.list.rss'),
    url('^user:(?P<user_id>\d+)$', views.review_list, name='ratings.user'),
)
