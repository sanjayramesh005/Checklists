from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$',views.login_view,name="login_url"),
    url(r'^auth/$',views.auth_view,name="auth_url"),
    url(r'^loggedin/$',views.loggedin_view,name="loggedin_url"),
    url(r'^invalid/$',views.invalid_view,name="invalid_url"),
    url(r'^logout/$',views.logout_view,name="logout_url"),
    url(r'^loggedin/(?P<checklist_id>[0-9]+)/$',views.detail_view,name="detail_url"),
    url(r'^change/(?P<checklist_id>[0-9]+)/$',views.change_checklist_view,name="change_checklist_url"),
    url(r'^copy/(?P<checklist_id>[0-9]+)/$',views.copy_view,name="copy_url"),
    url(r'^templates/$',views.show_templates_view,name='template_url'),
    url(r'^templates/(?P<checklist_id>[0-9])/$',views.template_detail_view,name='template_detail_url'),
    url(r'^change_title/(?P<checklist_id>[0-9])/$',views.change_title_view,name='change_title_url'),
    url(r'^add/(?P<checklist_id>[0-9])/$',views.add_listitem_view,name='add_listitem_url'),
    ]
