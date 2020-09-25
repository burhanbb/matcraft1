from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from . import models
import time
from django.core.mail import send_mail

em='hello'
curl=settings.CURRENT_URL

def home(request):
    return render(request,'home.html',{'curl':curl})

def blog(request):
    return render(request,'blog.html',{'curl':curl})

def register(request):
        if (request.method=="GET"):
            return render(request,'register.html',{'curl':curl,'output':''})
        else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            mobile=request.POST.get('mobile')
            city=request.POST.get('city')
            gender=request.POST.get('gender')
            dt=time.asctime(time.localtime(time.time()))	
            query="insert into register values(NULL,'%s','%s','%s','%s','%s','%s','%s','user',0,'%s')" %(name,email,password,address,mobile,city,gender,dt)
            models.cursor.execute(query)
            models.db.commit()
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = email
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Verification Mail MatCraft"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Welcome to MatCraft</h1>
                                <p>You have successfully registered , please click on the link below to verify your account</p>
                                <h2>Username : """+email+"""</h2>
                                <h2>Password : """+str(password)+"""</h2>
                                <br>
                                <a href='http://localhost:8000/verify?vemail="""+email+"""' >Click here to verify account</a>		
                            </body>
                        </html>
                    """
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls() 
            s.login("hellomatcraft@gmail.com", "esdcxyiyjwmuglow") 

            part2 = MIMEText(html, 'html')

            msg.attach(part2)

            s.sendmail(me,you, str(msg)) 
            s.quit() 
            print("mail send successfully....")
            
            return render(request,'register.html',{'curl':curl,'output':'Registration successfully done....'})
        
def verify(request):
    vemail=request.GET.get('vemail')
    query="update register set status=1 where email='%s' " %(vemail)
    models.cursor.execute(query)
    models.db.commit()
    return redirect(curl+'login/')


def login(request):
    if (request.method=="GET"): 
        return render(request,'login.html',{'curl':curl,'output':''})
    else:
        email=request.POST.get('email')	
        password=request.POST.get('password')	
        query="select * from register where email='%s' and password='%s' and status=1" %(email,password)
        models.cursor.execute(query)
        userDetails=models.cursor.fetchall()
        if len(userDetails)>0:
            if userDetails[0][8]=='user':
                response=redirect(curl+'user/')
                return response
            else:	
                response=redirect(curl+'myadmin/')
                response.set_cookie('cunm',email,3600)
                return response	
        else:
            return render(request,'login.html',{'curl':curl,'output':'Login failed invalid user or verify your account',})
    
    
                
def mainshop(request):
    query1="select * from product"
    models.cursor.execute(query1)
    splist=models.cursor.fetchall()
    
    return render(request,"mainshop.html",{'curl':curl,'cunm':request.COOKIES.get('cunm'),'splist':splist})
    
def get1(request):
    query1="select title from product where pid=1"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=1"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=1"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    
    return render(request,'get1.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def get2(request):
    query1="select title from product where pid=2"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=2"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=2"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    return render(request,'get2.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def get3(request):
    query1="select title from product where pid=3"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=3"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=3"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    return render(request,'get3.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def get4(request):
    query1="select title from product where pid=4"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=4"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=4"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    return render(request,'get4.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def get5(request):
    query1="select title from product where pid=5"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=5"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(,)")
    query3="select description from product where pid=5"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    return render(request,'get5.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})
			
def get6(request):
    query1="select title from product where pid=6"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=6"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=6"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    
    return render(request,'get6.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def get7(request):
    query1="select title from product where pid=7"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=7"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=7"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    return render(request,'get7.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def get8(request):
    query1="select title from product where pid=8"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=8"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=8"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    return render(request,'get8.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def get9(request):
    query1="select title from product where pid=9"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=9"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=9"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    return render(request,'get9.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def get10(request):
    query1="select title from product where pid=10"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=10"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(,)")
    query3="select description from product where pid=10"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    return render(request,'get10.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})
			
def get11(request):
    query1="select title from product where pid=11"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=11"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=11"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    
    return render(request,'get11.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def get12(request):
    query1="select title from product where pid=12"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=12"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=12"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    return render(request,'get12.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def get13(request):
    query1="select title from product where pid=13"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=13"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=13"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    return render(request,'get13.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def get14(request):
    query1="select title from product where pid=14"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=14"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=14"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    return render(request,'get14.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def get15(request):
    query1="select title from product where pid=15"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=15"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(,)")
    query3="select description from product where pid=15"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    return render(request,'get15.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})
			
