from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from .models import Template,Copy,Listitem,Listitemcopy
from django.core.urlresolvers import reverse
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated():
        c = {}
        c.update(csrf(request))
        return render(request,"login.html",c)
    else:
        return HttpResponseRedirect("/accounts/loggedin/")

def auth_view(request):
    if (request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/accounts/loggedin/')
        else:
            return HttpResponseRedirect('/accounts/invalid/')
    else:
        return HttpResponse("Forbidden")


def loggedin_view(request):
    if request.user.is_authenticated():
        user = request.user
        return render(request,"loggedin.html",{'user':user})
    else:
        response="<a href='/accounts/login/'>Click here</a> to login."
        return HttpResponse(response)

def invalid_view(request):
    return render(request,'invalid.html',{})

def logout_view(request):
    auth.logout(request)
    return render(request,"logout.html",{})

def detail_view(request,checklist_id):
    checklist = get_object_or_404(Copy,id=checklist_id)
    c = {'checklist' : checklist}
    c.update(csrf(request))
    return render(request,'detail.html',c)

def change_checklist_view(request,checklist_id):
    checklist = get_object_or_404(Copy,id=checklist_id)
    for listitem in checklist.listitemcopy_set.all():
        if str(listitem.id) in request.POST.getlist('listitem'):
            listitem.value=True
            listitem.save()
        else:
            listitem.value=False
            listitem.save()

    return HttpResponseRedirect('/accounts/loggedin/')

def copy_view(request,checklist_id):
    template = get_object_or_404(Template,pk=checklist_id)
    user = request.user
    c = Copy(template=template,user=user,title=template.title)
    c.save()
    for listitem in template.listitem_set.all():
        q = c.listitemcopy_set.create(text=listitem.text,value=False)
        q.save()

    return HttpResponseRedirect('/accounts/templates/')

def show_templates_view(request):
    templates = Template.objects.all()
    return render(request,'templates.html',{'templates':templates})

def template_detail_view(request,checklist_id):
    template = get_object_or_404(Template,pk=checklist_id)
    listitems = template.listitem_set.all()
    return render(request,'templatedetail.html',{'template':template,'listitems':listitems})

def change_title_view(request,checklist_id):
    checklist = get_object_or_404(Copy,id=checklist_id)
    if request.method=='POST':
        checklist.title = request.POST['title']
        checklist.save()
        return HttpResponseRedirect(reverse('detail_url',kwargs={'checklist_id':checklist.id}))
    else:
        c = {'checklist':checklist}
        c.update(csrf(request))
        return render(request,'change_title.html',c)

def add_listitem_view(request,checklist_id):
    checklist = get_object_or_404(Copy,id=checklist_id)
    if request.method=='POST':
        text = request.POST['text']
        l = checklist.listitemcopy_set.create(text=text,value=False)
        l.save()
        return HttpResponseRedirect(reverse('detail_url',kwargs={'checklist_id':checklist_id}))
    else:
        c = {'checklist':checklist}
        c.update(csrf(request))
        return render(request,'add_item.html',c)

