from  django.shortcuts import render, redirect, HttpResponse
from sh.models import ToolsScript
from hostinfo.models import Host
import json
from django.contrib.auth.decorators import permission_required, login_required




from  hostinfo.ansible_runner.runner import AdHocRunner,CommandResultCallback

@login_required(login_url="/login.html", )
def sh(request):  ##首页
    sh = ToolsScript.objects.filter(id__gt=0).order_by('-id')
    return render(request, 'sh/sh.html', {"sh_list":sh, })

@login_required(login_url="/login.html")
# @permission_required('jigui.add_jiguiinfo',login_url='/error.html')
def shadd(request):  #添加
    if request.method == "POST":
        name = request.POST.get('name', None)
        tool_script = request.POST.get('tool_script', None)
        tool_run_type = request.POST.get('tool_run_type', None)
        comment = request.POST.get('comment', None)
        obj = ToolsScript.objects.create(name=name,tool_script=tool_script,tool_run_type=tool_run_type,comment=comment)
        msg = "添加成功"
        return render(request, 'sh/shadd.html', {'msg': msg ,})
    else:
        return render(request, 'sh/shadd.html',)
    
    
    
@login_required(login_url="/login.html")
# @permission_required('jigui.delete_jiguiinfo',login_url='/error.html')
def shedit(request, nid):   #编辑
    if request.method == "GET":
        obj1 = ToolsScript.objects.filter(id=nid)
        return render(request, 'sh/shedit.html',{'obj':obj1})

    elif request.method == "POST":
        
        name = request.POST.get('name', None)
        tool_script = request.POST.get('tool_script', None)
        tool_run_type = request.POST.get('tool_run_type', None)
        comment = request.POST.get('comment', None)

        obj1 = ToolsScript.objects.filter(id=nid).first()
        obj1.name=name
        obj1.tool_script=tool_script
        obj1.tool_run_type=tool_run_type
        obj1.comment = comment
        obj1.save()
        
        return redirect('/sh/sh.html')


@login_required(login_url="/login.html")
# @permission_required('jigui.delete_jiguiinfo',login_url='/error.html')
def shinfo(request, nid):  # 查看
    if request.method == "GET":
        obj1 = ToolsScript.objects.filter(id=nid)

        return render(request, 'sh/shinfo.html', {'obj': obj1})


@login_required(login_url="/login.html")
# @permission_required('jigui.delete_jiguiinfo',login_url='/error.html')
def shdel(request):  # 删除
    ret = {'status': True, 'error': None, 'data': None}
    if request.method == "POST":
        id = request.POST.get('id',None)
        obj1 = ToolsScript.objects.filter(id=id).delete()
        return HttpResponse(json.dumps(ret))

@login_required(login_url="/login.html")
def shdelall(request):##批量删除
    ret = {'status': True, 'error': None, 'data': None}
    if  request.method == "POST":
             ids = request.POST.getlist('id')
             idstring = ','.join(ids)
             ToolsScript.objects.extra(where=['id IN (' + idstring + ')']).delete()
             return HttpResponse(json.dumps(ret))




@login_required(login_url="/login.html")
def shell(request):  ##执行脚本
    ret = {'status': True, 'error': None, 'data': None}
    if request.method == 'GET':
            host_id = request.POST.get('hostid', None)
            sh_id = request.POST.get('sshid', None)
        
            host = Host.objects.filter(id=1)
            sh = ToolsScript.objects.filter(id=1)
            
            
            
            for s in sh:
                with  open('sh/shell/{}.sh'.format(s.id),'w+') as f:
                    f.write(s.tool_script)
                    a = 'sh/shell/{}.sh'.format(s.id)
            
            for h in host:
                assets = [
                    {
                        "hostname": '1',
                        "ip": h.ip,
                        "port": h.port,
                        "username": h.username,
                        "password": h.password,
                    },
                ]
            
            
                task_tuple = (('script', a),)
                hoc = AdHocRunner(hosts=assets)
                hoc.results_callback = CommandResultCallback()
                ret = hoc.run(task_tuple)
                print(ret)
                data = ret['contacted']['1']['stdout']
                print(data)
                return  HttpResponse(json(ret))
            
            import time
            time.sleep(10000)
