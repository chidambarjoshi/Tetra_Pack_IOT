from django.shortcuts import render, HttpResponseRedirect
import pymongo
from MyProject.settings import db_name
from django.contrib import messages





def db_connect():
    client = pymongo.MongoClient(db_name)
    try:
        client.server_info()
        return client
    except pymongo.errors.ConnectionFailure as err:
        print(err)


client = db_connect()
db = client.get_database('tetrapack')


def home(request):
    uname = False
    if request.COOKIES.get('username'):
        uname = True
    context = {'uname': uname}
    return render(request, 'home_admin.html', context)


def about(request):
    uname = False
    if request.COOKIES.get('username'):
        uname = True
    context = {'uname': uname}
    return render(request, 'about.html', context)


def about_user(request):
    return render(request, 'about_user.html')


def home_user(request):
    return render(request, 'home1.html')


def getdata(request):
    if request.COOKIES.get('username'):
        uname = True
        data = []
        datatemp = db.mfdtemp.find()
        for x in datatemp:
            d1 = db.phdata.find_one({'id': x['id']})
            obj = {'id': x['id'],
                   'mfd': x['mfd'],
                   'phvalue': float(d1['phvalue']),
                   'Lastupdate': d1['Lastupdate'],
                   'selling_status':d1['selling_status'],
                   }
            data.append(obj)
        context = {'disp_data': data,'uname':uname}
        return render(request, 'datadisplay.html', context)
    else:
        return HttpResponseRedirect('/login')


def getdata1(request, pid):
    uname = False
    if request.COOKIES.get('username'):
        x= db.mfdtemp.find_one({'id': pid})
        d1= db.phdata.find_one({'id': pid})

        uname = True

        if x:
            obj = {'id': x['id'],
               'mfd': x['mfd'],
               'phvalue': float(d1['phvalue']),
               'Lastupdate': d1['Lastupdate'],
               'selling_status': d1['selling_status'],
               }
            context = {'data': obj,  'uname': uname}
        else:
            context = {'data': [],  'uname': uname}
            messages.add_message(request, messages.INFO, 'Product Not Found')

        return render(request, 'datadisp.html', context)
    else:
        return HttpResponseRedirect('/login')


def getdata_user(request, pid):
    x= db.mfdtemp.find_one({'id': pid})
    d1= db.phdata.find_one({'id': pid})
    if x:
        obj = {'id': x['id'],
               'mfd': x['mfd'],
               'phvalue': float(d1['phvalue']),
               'Lastupdate': d1['Lastupdate'],
               'selling_status': d1['selling_status'],
               }
        context = {'data': obj}
    else:
        context = {'data': []}
        messages.add_message(request, messages.INFO, 'Product Not Found')

    return render(request, 'datadisp_user.html', context)


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name == 'admin' and password == 'admin':
            response = HttpResponseRedirect('/user-admin')
            response.set_cookie('username', name, 300)
            return response
        else:

            messages.add_message(request, messages.INFO, 'Invalid Credentials')
            return render(request, 'login.html', {})
    uname = False
    if request.COOKIES.get('username'):
        uname=True
        context = {'uname': uname}
        return render(request, 'home_admin.html', context)

    return render(request, 'login.html', {})





def logout(request):
    response = HttpResponseRedirect('/login')
    response.delete_cookie('username')
    return response


def search_pro(request):
    uname = False
    if request.COOKIES.get('username'):
        uname = True
        if request.method == 'POST':

            id = request.POST.get('id')
            return HttpResponseRedirect('/datadisplay1/' + id)
        else:

            context = {'uname': uname}
            return render(request, 'search.html', context)
    else:
        return render(request, 'login.html', {})








