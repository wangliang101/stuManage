from django.shortcuts import render,redirect,HttpResponse
import pymysql
from uniti import sqlhelper
import json

# def checkLogin(func):
#     def inner(*args,**kwargs):
#         ret = func(*args,**kwargs)
#         return ret
#     return inner

def classes(request):
    ticket=request.COOKIES.get('ticket')
    if not ticket:
        return redirect('/login/')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,title from class")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request,'classes.html',{'class_list':class_list})


def add_class(request):
    if request.method == "GET":
        return render(request, 'add_class.html')
    else:
        # print(request.POST)
        # v = request.POST.get('title')
        # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute("insert into class(title) values(%s)",v)
        # conn.commit()
        # cursor.close()
        # conn.close()
        # return redirect('/classes/')
        c_title = request.POST.get('class_title')
        # return HttpResponse('ok')
        if len(c_title) > 0:
            sqlhelper.modify("insert into class(title) values(%s)",c_title)
            return HttpResponse('ok')
        else:
            return HttpResponse('输入不能为空')

def del_class(request):
    nid = request.GET.get('nid')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class where id = %s",nid)
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/classes/')

def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class where id=%s",nid)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(request,'edit_class.html',{'result':result})
    else:
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set title=%s where id =%s",[title,nid])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')

def teacher(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("""SELECT teacher.id,teacher.name,class.title FROM teacher LEFT JOIN teacher2class 
                        on teacher2class.teacher_id = teacher.id LEFT JOIN class on class.id = teacher2class.class_id;""",[])
    teacher_list = cursor.fetchall()
    cursor.close()
    conn.close()
    result = {}
    for row in teacher_list:
        if row['id'] in result:
            result[row['id']]['titles'].append(row['title'])
        else:
            result[row['id']] = {'id': row['id'], 'name': row['name'], 'titles': [row['title']]}
    return render(request,'teacher.html',{'teacher_list':result.values()})

def add_teacher(request):
    if request.method == "GET":
        class_list = sqlhelper.get_list("select id,title from class",[])
        return render(request,'add_teacher.html',{'class_list':class_list})
    else:
        t_name = request.POST.get('t_name')
        obj = sqlhelper.SqlHelper()
        teacher_id = obj.creat('INSERT  into teacher (name) value(%s)',[t_name,])
        #更新老师和班级对应表
        cla_ids = request.POST.getlist('class_ids')
        cla_list = []
        for cla_id in cla_ids:
            cla_list.append((teacher_id,cla_id),)
        obj.multiple_modify('insert into teacher2class (teacher_id,class_id) VALUES (%s,%s)',cla_list)
        obj.close()
        return redirect("/teacher/")
def del_teacher(request):
    tid = request.GET.get('tid')
    print(tid)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from teacher WHERE  id=%s",tid)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/teacher/')

def edit_teacher(request):
    if request.method == "GET":
        tid = request.GET.get('tid')
        obj = sqlhelper.SqlHelper()
        teacher_info = obj.get_one('select id,name from teacher WHERE id=%s',[tid])
        class_id_list =obj.get_list('select class_id from teacher2class WHERE teacher_id = %s',[tid,])
        class_list  =obj.get_list('select id,title from class',[])
        obj.close()
        temp = []
        for row in class_id_list:
            temp.append(row['class_id'])
        return render(request,'edit_teacher.html',{"teacher_info":teacher_info,'class_list':class_list,'class_id_list':temp})
    else:
        tid = request.GET.get('tid')
        t_name = request.POST.get('t_name')
        class_ids =request.POST.getlist('class_ids')
        obj = sqlhelper.SqlHelper()
        #在老师表中修改老师信息
        obj.modify('update teacher set NAME =%s WHERE id =%s;',[t_name,tid])
        #在老师和班级关系对应表中修改老师所对应的班级
        obj.modify("delete from teacher2class  WHERE teacher_id=%s",tid)
        print(tid,class_ids,t_name)
        cla_list = []
        for cla_id in class_ids:
            cla_list.append((tid, cla_id), )
        obj.multiple_modify('insert into teacher2class (teacher_id,class_id) VALUES (%s,%s)', cla_list)
        obj.close()
        return redirect("/teacher/")


def student(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select student.id,student.name,class.title,student.class_id from student LEFT JOIN class ON student.class_id = class.id")
    student_list = cursor.fetchall()
    cursor.close()
    conn.close()
    class_list = sqlhelper.get_list("select * from class",[])
    return render(request,'student.html',{'student_list':student_list,'class_list':class_list})


def add_student(request):
    if request.method == "GET":
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class")
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()
        return render(request,'add_student.html',{'class_list':class_list})
    else:
        class_id= request.POST.get("class_id")
        s_name = request.POST.get("s_name")
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='1008')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into student(name,class_id) VALUE(%s,%s)", [s_name,class_id])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/student/')

def del_student(request):
    s_id= request.GET.get("s_id")
    sqlhelper.modify("delete from student WHERE id=%s",s_id)
    return redirect('/student/')

def edit_student(request):
    if request.method == "GET":
        s_id = request.GET.get("s_id")
        current_student_list =sqlhelper.get_one("select id,name,class_id from student WHERE id=%s",s_id)
        class_list =sqlhelper.get_list("select id,title from class",[])
        return render(request,'edit_student.html',{'current_student_list':current_student_list,"class_list":class_list})
    else:
        s_id = request.GET.get('s_id')
        s_name = request.POST.get('s_name')
        c_id = request.POST.get('class_id')
        print(s_id,s_name,c_id )
        sqlhelper.modify("update student set NAME =%s,class_id=%s WHERE id =%s", [s_name,c_id,s_id])
        return redirect('/student/')

def edit_modal_class(request):
    ret = {'status':True,'message':None}
    try:
        editClassId = request.POST.get('editClassId')
        editClassTitle = request.POST.get('editClassTitle')
        sqlhelper.modify("update class set title =%s WHERE id =%s", [editClassTitle,editClassId])
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
    return HttpResponse(json.dumps(ret))

def add_modal_student(requet):
    ret = {'status':True,'message':None}
    try:
        addStuName = requet.POST.get('addStuName')
        classId = requet.POST.get('classId')
        sqlhelper.modify('insert into student(name,class_id) VALUE(%s,%s)',[addStuName,classId])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))

def edit_modal_student(request):
    ret = {'status': True, 'message': None}
    try:
        studentId = request.POST.get('studentId')
        stuName = request.POST.get('stuName')
        classId = request.POST.get('classId')
        print(stuName)
        sqlhelper.modify('update student set NAME = %s ,class_id = %s WHERE id = %s', [stuName,classId,studentId])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))

import time
def get_class_list(request):
    time.sleep(1)
    obj = sqlhelper.SqlHelper()
    class_list = obj.get_list('select id,title from class',[])
    obj.close()

    return HttpResponse(json.dumps(class_list))
def add_modal_teacher(request):
    ret={"status":True,"message":None}
    try:
        t_name = request.POST.get("t_name")
        class_id_list = request.POST.getlist("class_id_list")
        print(t_name,class_id_list)
        obj = sqlhelper.SqlHelper()
        teacher_id = obj.creat('INSERT  into teacher (name) value(%s)', [t_name, ])
        cla_list = []
        for cla_id in class_id_list:
            cla_list.append((teacher_id, cla_id), )
        obj.multiple_modify('insert into teacher2class (teacher_id,class_id) VALUES (%s,%s)', cla_list)
        obj.close()
    except Exception as e:
        ret["status"] = False
        ret["message"] = str(e)
    return HttpResponse(json.dumps(ret))

def layout(request):
    return render(request,"layout.html")

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "wl" and password == "123":
            obj = redirect("/classes/")
            obj.set_cookie('ticket','adpjfisjfi')
            return obj
        else:
            return render(request, 'login.html')
