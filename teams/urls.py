from django.conf.urls import url
from teams import views
from .views import team_view_set

teams_data_list = team_view_set.as_view({
    'get': 'list',
    'post': 'create'
})

teams_data_detail = team_view_set.as_view({
    'get':'retrieve',
    'pit':'update',
    'patch':'partial_update',
    'delete':'destroy'
})

urlpatterns = [
    url(r'^team-data/$', teams_data_list, name='teams-data-list'),
    url(r'^team-data/(?P<pk>[0-9]+)/$', teams_data_detail, name='teams-data-detail')
]