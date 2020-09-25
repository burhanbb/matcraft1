from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from . import  models

curl=settings.CURRENT_URL



def adminhome(request):
	return render(request,"adminhome.html",{'curl':curl,'cunm':request.COOKIES.get('cunm')})

def addpro(request):
	
	if request.method=='GET':
		return render(request,'addpro.html',{'curl':curl,'output':'','cunm':request.COOKIES.get('cunm')})		
	else:
		title=request.POST.get('titlee')
		description=request.POST.get('description')
		price=request.POST.get('price')
	
	
		query1="insert into product values(NULL,'%s','%s','%s')" %(title,description,price)
		models.cursor.execute(query1)
		models.db.commit()
		
		return render(request,'addpro.html',{'curl':curl,'output':'Product Added Successfully....','cunm':request.COOKIES.get('cunm')})
	
    
    
	

def editpro(request):
    
    if request.method=='GET':
        query1="select * from product"
        models.cursor.execute(query1)
        splist=models.cursor.fetchall()
        
        return render(request,'editpro.html',{'curl':curl,'output':'','cunm':request.COOKIES.get('cunm'),'splist':splist})
    else:
        entry=request.POST.get('entry')
        ch=request.POST['drop']
        sl=request.POST['pid']
        int(sl)
        if ch=="Title" :
            query1="update product set title='%s' where pid=%s " %(entry,sl)
            models.cursor.execute(query1)
            models.db.commit()
        if ch=="Price" :
            query1="update product set price=%s where pid=%s " %(entry,sl)
            models.cursor.execute(query1)
            models.db.commit()
        if ch=="Description" :
            query1="update product set description='%s' where pid=%s " %(entry,sl)
            models.cursor.execute(query1)
            models.db.commit()

		
  
        return render(request,'editpro.html',{'curl':curl,'output':'Product Information Changed Successfully....','cunm':request.COOKIES.get('cunm')})
	

def editinfo(request):
    if request.method=='GET':
    		return render(request,'editinfo.html',{'curl':curl,'output':'','cunm':request.COOKIES.get('cunm')})
    else:
        email=request.POST.get('email')
        entry=request.POST.get('entry')
        sl=request.POST['field']
        if sl=="Name" :
            query1="update register set name='%s' where email='%s' " %(entry,email)
            models.cursor.execute(query1)
            models.db.commit()
        if sl=="Address" :
            query1="update register set address='%s' where email='%s' " %(entry,email)
            models.cursor.execute(query1)
            models.db.commit()
        if sl=="Mobile" :
            query1="update register set mobile=%s where email='%s' " %(entry,email)
            models.cursor.execute(query1)
            models.db.commit()
        if sl=="City" :
            query1="update register set city='%s' where email='%s' " %(entry,email)
            models.cursor.execute(query1)
            models.db.commit()
        if sl=="Gender" :
            query1="update register set gender='%s' where email='%s' " %(entry,email)
            models.cursor.execute(query1)
            models.db.commit()
        if sl=="Role" :
            query1="update register set role='%s' where email='%s' " %(entry,email)
            models.cursor.execute(query1)
            models.db.commit()
        if sl=="Status" :
            query1="update register set status=%s where email='%s' " %(entry,email)
            models.cursor.execute(query1)
            models.db.commit()
		
  
        return render(request,'editinfo.html',{'curl':curl,'output':'Information Changed Successfully....','cunm':request.COOKIES.get('cunm')})
	
    
    