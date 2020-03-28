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
    return render(request, 'home.html', context)



def getdata(request):
    if request.COOKIES.get('username'):
        uname = True
        data = []
        datatemp = db.mfdtemp.find()
        for x in datatemp:
            d1 = db.tempdata.find_one({'id': x['id']})
            obj = {'id': x['id'],
                   'mfd': x['mfd'],
                   'temp': d1['temp'],
                   'humi': d1['humi'],
                   'Lastupdate': d1['Lastdate']
                   }
            data.append(obj)
        context = {'disp_data': data,'uname':uname}
        return render(request, 'datadisplay.html', context)
    else:
        return HttpResponseRedirect('/login')


def getdata1(request, pid):
    datatemp = db.mfdtemp.find_one({'id': pid})
    datatemp1 = db.tempdata.find_one({'id': pid})
    uname = False
    if request.COOKIES.get('username'):
        uname = True

    if datatemp:
        context = {'disp_data': datatemp, 'tem_data': datatemp1, 'uname': uname}
    else:
        context = {'disp_data': [], 'tem_data': [], 'uname': uname}
        messages.add_message(request, messages.INFO, 'Product Not Found')

    return render(request, 'datadisplay1.html', context)


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name == 'admin' and password == 'admin':



            response = HttpResponseRedirect('/admin_dash')
            response.set_cookie('username', name,420)
            return response
        else:

            messages.add_message(request, messages.INFO, 'Invalid Credentials')
            return render(request, 'Login.html', {})
    uname = False
    if request.COOKIES.get('username'):
        uname=True
        context = {'uname': uname}
        return render(request, 'home.html', context)

    return render(request, 'Login.html', {})


def admin_dash(request):
    if request.COOKIES.get('username'):
        name = request.COOKIES.get('username')
        context = {' uname ': name}
        return render(request, 'admin_dash.html', context)
    else:
        return HttpResponseRedirect('/login')


def logout(request):
    response = HttpResponseRedirect('/login')
    response.delete_cookie('username')
    return response


def search_pro(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        return HttpResponseRedirect('/datadisplay1/' + id)
    else:
        return render(request, 'search.html', {})
