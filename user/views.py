from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from . import  models
from matcraft import views
curl=settings.CURRENT_URL
import time


def userhome(request):
	return render(request,"userhome.html",{'curl':curl,'cunm':request.COOKIES.get('cunm')})
	
def userblog(request):
    	return render(request,"userblog.html",{'curl':curl,'cunm':request.COOKIES.get('cunm')})

def shop(request):
    query1="select * from product"
    models.cursor.execute(query1)
    sclist=models.cursor.fetchall()
    return render(request,"shop.html",{'curl':curl,'cunm':request.COOKIES.get('cunm'),'sclist':sclist})

def home(request):
    return render(request,"home.html",{'curl':curl})

def uget1(request):
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
    
    
    return render(request,'uget1.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def uget2(request):
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
    return render(request,'uget2.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def uget3(request):
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
    return render(request,'uget3.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def uget4(request):
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
    return render(request,'uget4.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def uget5(request):
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
    return render(request,'uget5.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})
				
def uget6(request):
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
    
    return render(request,'uget6.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def uget7(request):
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
    return render(request,'uget7.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def uget8(request):
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
    return render(request,'uget8.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def uget9(request):
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
    return render(request,'uget9.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def uget10(request):
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
    return render(request,'uget10.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})
			
def uget11(request):
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
    
    return render(request,'uget11.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def uget12(request):
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
    return render(request,'uget12.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def uget13(request):
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
    return render(request,'uget13.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def uget14(request):
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
    return render(request,'uget14.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})

def uget15(request):
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
    return render(request,'uget15.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'title':title,'price':price,'description':description})
			

def umget1(request):
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
    if (request.method=="GET"):
            return render(request,'umget1.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget1.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget1(request):
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
    if (request.method=="GET"):
            return render(request,'umget1.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget1.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget2(request):
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
    if (request.method=="GET"):
            return render(request,'umget2.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget2.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget3(request):
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
    if (request.method=="GET"):
            return render(request,'umget3.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget3.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})
       
def umget1(request):
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
    if (request.method=="GET"):
            return render(request,'umget1.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget1.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget4(request):
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
    if (request.method=="GET"):
            return render(request,'umget4.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget4.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget1(request):
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
    if (request.method=="GET"):
            return render(request,'umget1.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget1.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget5(request):
    query1="select title from product where pid=5"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=5"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=5"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    if (request.method=="GET"):
            return render(request,'umget5.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget5.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget1(request):
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
    if (request.method=="GET"):
            return render(request,'umget1.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget1.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget6(request):
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
    if (request.method=="GET"):
            return render(request,'umget6.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget6.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget1(request):
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
    if (request.method=="GET"):
            return render(request,'umget1.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget1.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget7(request):
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
    if (request.method=="GET"):
            return render(request,'umget7.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget7.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})


def umget8(request):
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
    if (request.method=="GET"):
            return render(request,'umget8.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget8.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget9(request):
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
    if (request.method=="GET"):
            return render(request,'umget9.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget9.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget1(request):
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
    if (request.method=="GET"):
            return render(request,'umget1.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget1.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget10(request):
    query1="select title from product where pid=10"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=10"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=10"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    if (request.method=="GET"):
            return render(request,'umget10.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget10.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget1(request):
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
    if (request.method=="GET"):
            return render(request,'umget1.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget1.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget11(request):
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
    if (request.method=="GET"):
            return render(request,'umget11.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget11.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget1(request):
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
    if (request.method=="GET"):
            return render(request,'umget1.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget1.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget12(request):
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
    if (request.method=="GET"):
            return render(request,'umget12.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget12.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget1(request):
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
    if (request.method=="GET"):
            return render(request,'umget1.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget1.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget13(request):
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
    if (request.method=="GET"):
            return render(request,'umget13.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget13.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget1(request):
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
    if (request.method=="GET"):
            return render(request,'umget1.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget1.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget14(request):
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
    if (request.method=="GET"):
            return render(request,'umget14.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget14.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget1(request):
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
    if (request.method=="GET"):
            return render(request,'umget1.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget1.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})

def umget15(request):
    query1="select title from product where pid=15"
    models.cursor.execute(query1)
    title1=models.cursor.fetchone()
    title=str(title1).strip("(',)")
    query2="select price from product where pid=15"
    models.cursor.execute(query2)
    price1=models.cursor.fetchone()
    price=str(price1).strip("(',)")
    query3="select description from product where pid=15"
    models.cursor.execute(query3)
    description1=models.cursor.fetchone()
    description=str(description1).strip("(',)")
    if (request.method=="GET"):
            return render(request,'umget15.html',{'curl':curl,'output':''})
    else:	
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            dt=time.asctime(time.localtime(time.time()))
            import smtplib 
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            me = "hellomatcraft@gmail.com"
            you = "burhanuddinboot.am@gmail.com"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "To MatCraft Team"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Dear MatCraft Team</h1>
                                <p>Following Person Has Shown Interest In The Following Product</p>
                                <h2>Name : """+name+"""</h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Mobile: """+mobile+"""</h2>
                                <h2>Product Title: """+title+"""</h2>
                                <h2>Product Price: """+price+"""</h2>
                                <h2>Product Description: """+description+"""</h2>
                                <h2>Time : """+dt+"""</h2>
                                <h2>Good Luck</h>				
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
            
            return render(request,'umget15.html',{'curl':curl,'output':'Details Registered Successfully! Our Team Will Contact You Shortly.'})
