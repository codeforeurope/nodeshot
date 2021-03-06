from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns


from nodeshot.community.participation import views


urlpatterns = patterns('nodeshot.community.participation.views',
    #url(r'^/comments/add/$', views.CommentCreate.as_view(), name='api_comments_add'),
    url(r'^/layers/(?P<slug>[-\w]+)/comments/$', 'layer_nodes_comments', name='api_layer_nodes_comments'),
    url(r'^/layers/(?P<slug>[-\w]+)/participation/$', 'layer_nodes_participation', name='api_layer_nodes_participation'),
    url(r'^/comments/$', 'all_nodes_comments', name='api_all_nodes_comments'),
    url(r'^/participation/$','all_nodes_participation', name='api_all_nodes_participation'),
    url(r'^/nodes/(?P<slug>[-\w]+)/comments/$', 'node_comments',name='api_node_comments'),
    url(r'^/nodes/(?P<slug>[-\w]+)/ratings/$', 'node_ratings',name='api_node_ratings'),
    url(r'^/nodes/(?P<slug>[-\w]+)/votes/$', 'node_votes',name='api_node_votes'),
    url(r'^/nodes/(?P<slug>[-\w]+)/participation/$', 'node_participation', name= 'api_node_participation'),
)

#urlpatterns = format_suffix_patterns(urlpatterns)