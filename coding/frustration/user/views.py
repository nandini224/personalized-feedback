from urllib import request
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from mindsparkadmin.models import NotificationModel
from user.forms import RegistrationForm
from user.models import RegistrationModel, AnswerModel, FeedbackModel


def index(request):
    if request.method=="POST":
        usid=request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = RegistrationModel.objects.get(userid=usid,password=pswd)
            request.session['userid']=check.id
            return redirect('userpage')
        except:
            pass
    return render(request,'user/index.html')
def register(request):
    if request.method == "POST":
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms = RegistrationForm()

    return render(request, 'user/register.html', {'form': forms})

def userpage(request):
    request.session['total'] = 0
    request.session['name1']  = 0
    request.session['name2'] = 0
    request.session['name3']= 0
    request.session['name4']= 0
    return render(request,'user/userpage.html')
def motivationalmegpage(request,pk,select):
    userid = request.session['userid']
    uobj = RegistrationModel.objects.get(id=userid)
    tot=request.session['total']
    nam1=request.session['name1']
    nam2=request.session['name2']
    nam3=request.session['name3']
    nam4=request.session['name4']
    se='sessionone'
    if request.method == "POST":
        out=request.POST.get('val')
        if out=="correct":
            if select=="sessionone":
                tot=tot+1
                request.session['total']=tot
            elif select=="sessiontwo":
                nam1=nam1+1
                request.session['name1']=nam1
            elif select=="sessionthree":
                nam2=nam2+1
                request.session['name2']=nam2
            elif select=="sessionfour":
                nam3=nam3+1
                request.session['name3']=nam3
            elif select=="sessionfive":
                nam4=nam4+1
                request.session['name4']=nam4

    data={}
    ch=int(pk)
    next=ch+1
    question,options1,options2,options3,answer='','','','',''
    if select=="sessionone":
        se = 'sessionone'
        if ch==1:
            question = "1)The radius of a circle is 3 inches. What is the area?"
            options1 ="a)9.25 inches squared "
            options2 ="b)20.28 inches squared "
            options3 ="c)28.26 inches squared"
            answer="c)28.26 inches squared"
        elif ch==2:
            question = "2)The diameter of a circle is 8 centimeters. What is the area?"
            options1 ="a)50.24 centimeters squared"
            options2 ="b)64 centimeters squared"
            options3 ="c)16.24 centimeters squared"
            answer = "a)50.24 centimeters squared"
        elif ch==3:
            question ="3))A circle has a radius of 12 inches.  What is the area of the circle?"
            options1 = "a)400.14 inches squared"
            options2 = "b)452.16 inches squared"
            options3 = "c)75.36 inches squared"
            answer = "b)452.16 inches squared"

        elif ch==4:
            question =" 4Mark has a circular swimming pool with are radius of 7 feet. If he wants a cover to go over the pool what is the least amount of material needed to cover the pool?"
            options1 = "a)43.96 feet squared"
            options2 = "b)21.98 feet squared"
            options3 = "c)153.86 feet squared"
            answer = "c)153.86 feet squared"


        elif ch==5:
            question ="5)The chord is the longest diameter in a circle."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "b)False"

        elif ch==6:
            question ="6)Molly is making pizza for supper and wants to cover the top of the pizza with sauce.She has measured the radius of the pizza to be 5 inches, how many square inches will the sauce cover?"
            options1 = "a)31.4 inches squared"
            options2 = "b)78.5 inches squared"
            options3 = "c)15.7 inches squared"
            answer = "b)78.5 inches squared"

        elif ch==7:
            question ="7)Pam's mom is fixing cookies for her class.  She wants to put icing on the cookies.The radius of the cookies is 2 inches.She is making 20 cookies, what is the area that the icing will cover if she icings all 20 cookies?"
            options1 = "a)251.2 inches squared"
            options2 = "b)125.6 inches squared"
            options3 = "c)12.56 inches squared"
            answer = "a)251.2 inches squared"

        elif ch==8:
            question ="8)A cicular stool needs to be covered with new fabric.  If the diameter of the stool is 2 feet, how much material is needed to cover the stool"
            options1 = "a)12.56 feet squared"
            options2 = "b)6.28 feet squared "
            options3 = "c)3.14 feet squared"
            answer = "c)3.14 feet squared"

        elif ch==9:
            question ="9)The radius is always half of the diameter."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "a)True"

        elif ch==10:
            question ="10)Sam has baked a circular cake.  The cake has a diameter of 10 inches.  Sam needs to know how much icing it will take to cover the top of the cake,which of the following was does Sam need to use to figure this out?"
            options1 = "a)10 x 3.14"
            options2 = "b)5 x 2 x 3.14"
            options3 = "c)5 x 5 x 3.14"
            answer = "c)5 x 5 x 3.14"
        elif ch >= 11:
            total = request.session['total']
            AnswerModel.objects.create(userId=uobj,catagory="motivationalmessage",sessionone=total)
            return redirect('selectsessionpage')

        else:
            question="none"
            options1="none"
            options2="none"
            options3="none"
            answer="none"
    elif select=="sessiontwo":
        se = 'sessiontwo'
        if ch==1:
            question = "1)The average of three numbers is 77.The first number is twice the second and the second number is twice the third. Find the first number."
            options1 = "a)33"
            options2 = "b)66"
            options3 = "c)132"
            answer = "c)132"
        elif ch==2:
            question = "2)The average of 10 numbers is calculated as 15.It is discovered later on that while calculating the average one number, namely 36 was wrongly read as 26.The correct average is "
            options1 = "a)16"
            options2 = "b)14"
            options3 = "c)18.6"
            answer = "a)16"
        elif ch==3:
            question ="3)The chord is the longest diameter in a circle."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "b)False"

        elif ch==4:
            question ="4)Molly is making pizza for supper and wants to cover the top of the pizza with sauce.She has measured the radius of the pizza to be 5 inches, how many square inches will the sauce cover?"
            options1 = "a)31.4 inches squared"
            options2 = "b)78.5 inches squared"
            options3 = "c)15.7 inches squared"
            answer = "b)78.5 inches squared"

        elif ch==5:
            question ="5)Pam's mom is fixing cookies for her class.  She wants to put icing on the cookies.The radius of the cookies is 2 inches.She is making 20 cookies, what is the area that the icing will cover if she icings all 20 cookies?"
            options1 = "a)251.2 inches squared"
            options2 = "b)125.6 inches squared"
            options3 = "c)12.56 inches squared"
            answer = "a)251.2 inches squared"
        elif ch==6:
            question ="6)The radius is always half of the diameter."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "a)True"

        elif ch==7:
            question ="7)Sam has baked a circular cake.  The cake has a diameter of 10 inches.  Sam needs to know how much icing it will take to cover the top of the cake,which of the following was does Sam need to use to figure this out?"
            options1 = "a)10 x 3.14"
            options2 = "b)5 x 2 x 3.14"
            options3 = "c)5 x 5 x 3.14"
            answer = "c)5 x 5 x 3.14"
        elif ch == 8:
            question = "8)The radius of a circle is 3 inches. What is the area?"
            options1 = "a)9.25 inches squared "
            options2 = "b)20.28 inches squared "
            options3 = "c)28.26 inches squared"
            answer = "c)28.26 inches squared"
        elif ch == 9:
            question = "9)The diameter of a circle is 8 centimeters. What is the area?"
            options1 = "a)50.24 centimeters squared"
            options2 = "b)64 centimeters squared"
            options3 = "c)16.24 centimeters squared"
            answer = "a)50.24 centimeters squared"
        elif ch == 10:
            question = "10))A circle has a radius of 12 inches.  What is the area of the circle?"
            options1 = "a)400.14 inches squared"
            options2 = "b)452.16 inches squared"
            options3 = "c)75.36 inches squared"
            answer = "b)452.16 inches squared"
        elif ch>=11:
            name1 = request.session['name1']
            obj = get_object_or_404(AnswerModel,userId=uobj)
            obj.sessiontwo=name1
            obj.save(update_fields=["sessiontwo"])

            return redirect('selectsessionpage')

        else:
            question = "none"
            options1 = "none"
            options2 = "none"
            options3 = "none"
            answer = "none"
    elif select=="sessionthree":
        se = 'sessionthree'
        if ch==1:
            question = "1)The radius of a circle is 3 inches. What is the area?"
            options1 ="a)9.25 inches squared "
            options2 ="b)20.28 inches squared "
            options3 ="c)28.26 inches squared"
            answer="c)28.26 inches squared"
        elif ch==2:
            question = "2)The diameter of a circle is 8 centimeters. What is the area?"
            options1 ="a)50.24 centimeters squared"
            options2 ="b)64 centimeters squared"
            options3 ="c)16.24 centimeters squared"
            answer = "a)50.24 centimeters squared"
        elif ch==3:
            question ="3))A circle has a radius of 12 inches.  What is the area of the circle?"
            options1 = "a)400.14 inches squared"
            options2 = "b)452.16 inches squared"
            options3 = "c)75.36 inches squared"
            answer = "b)452.16 inches squared"

        elif ch==4:
            question =" 4Mark has a circular swimming pool with are radius of 7 feet. If he wants a cover to go over the pool what is the least amount of material needed to cover the pool?"
            options1 = "a)43.96 feet squared"
            options2 = "b)21.98 feet squared"
            options3 = "c)153.86 feet squared"
            answer = "c)153.86 feet squared"


        elif ch==5:
            question ="5)The chord is the longest diameter in a circle."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "b)False"

        elif ch==6:
            question ="6)Molly is making pizza for supper and wants to cover the top of the pizza with sauce.She has measured the radius of the pizza to be 5 inches, how many square inches will the sauce cover?"
            options1 = "a)31.4 inches squared"
            options2 = "b)78.5 inches squared"
            options3 = "c)15.7 inches squared"
            answer = "b)78.5 inches squared"

        elif ch==7:
            question ="7)Pam's mom is fixing cookies for her class.  She wants to put icing on the cookies.The radius of the cookies is 2 inches.She is making 20 cookies, what is the area that the icing will cover if she icings all 20 cookies?"
            options1 = "a)251.2 inches squared"
            options2 = "b)125.6 inches squared"
            options3 = "c)12.56 inches squared"
            answer = "a)251.2 inches squared"

        elif ch==8:
            question ="8)A cicular stool needs to be covered with new fabric.  If the diameter of the stool is 2 feet, how much material is needed to cover the stool"
            options1 = "a)12.56 feet squared"
            options2 = "b)6.28 feet squared "
            options3 = "c)3.14 feet squared"
            answer = "c)3.14 feet squared"

        elif ch==9:
            question ="9)The radius is always half of the diameter."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "a)True"

        elif ch==10:
            question ="10)Sam has baked a circular cake.  The cake has a diameter of 10 inches.  Sam needs to know how much icing it will take to cover the top of the cake,which of the following was does Sam need to use to figure this out?"
            options1 = "a)10 x 3.14"
            options2 = "b)5 x 2 x 3.14"
            options3 = "c)5 x 5 x 3.14"
            answer = "c)5 x 5 x 3.14"
        elif ch >= 11:
            name2 = request.session['name2']
            obj = get_object_or_404(AnswerModel, userId=uobj)
            obj.sessionthree = name2
            obj.save(update_fields=["sessionthree"])

            return redirect('selectsessionpage')

        else:
            question="none"
            options1="none"
            options2="none"
            options3="none"
            answer="none"
    elif select=="sessionfour":
        se = 'sessionfour'
        if ch==1:
            question = "1)The average of three numbers is 77.The first number is twice the second and the second number is twice the third. Find the first number."
            options1 = "a)33"
            options2 = "b)66"
            options3 = "c)132"
            answer = "c)132"
        elif ch==2:
            question = "2)The average of 10 numbers is calculated as 15.It is discovered later on that while calculating the average one number, namely 36 was wrongly read as 26.The correct average is "
            options1 = "a)16"
            options2 = "b)14"
            options3 = "c)18.6"
            answer = "a)16"
        elif ch==3:
            question ="3)The chord is the longest diameter in a circle."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "b)False"

        elif ch==4:
            question ="4)Molly is making pizza for supper and wants to cover the top of the pizza with sauce.She has measured the radius of the pizza to be 5 inches, how many square inches will the sauce cover?"
            options1 = "a)31.4 inches squared"
            options2 = "b)78.5 inches squared"
            options3 = "c)15.7 inches squared"
            answer = "b)78.5 inches squared"

        elif ch==5:
            question ="5)Pam's mom is fixing cookies for her class.  She wants to put icing on the cookies.The radius of the cookies is 2 inches.She is making 20 cookies, what is the area that the icing will cover if she icings all 20 cookies?"
            options1 = "a)251.2 inches squared"
            options2 = "b)125.6 inches squared"
            options3 = "c)12.56 inches squared"
            answer = "a)251.2 inches squared"
        elif ch==6:
            question ="6)The radius is always half of the diameter."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "a)True"

        elif ch==7:
            question ="7)Sam has baked a circular cake.  The cake has a diameter of 10 inches.  Sam needs to know how much icing it will take to cover the top of the cake,which of the following was does Sam need to use to figure this out?"
            options1 = "a)10 x 3.14"
            options2 = "b)5 x 2 x 3.14"
            options3 = "c)5 x 5 x 3.14"
            answer = "c)5 x 5 x 3.14"
        elif ch == 8:
            question = "8)The radius of a circle is 3 inches. What is the area?"
            options1 = "a)9.25 inches squared "
            options2 = "b)20.28 inches squared "
            options3 = "c)28.26 inches squared"
            answer = "c)28.26 inches squared"
        elif ch == 9:
            question = "9)The diameter of a circle is 8 centimeters. What is the area?"
            options1 = "a)50.24 centimeters squared"
            options2 = "b)64 centimeters squared"
            options3 = "c)16.24 centimeters squared"
            answer = "a)50.24 centimeters squared"
        elif ch == 10:
            question = "10))A circle has a radius of 12 inches.  What is the area of the circle?"
            options1 = "a)400.14 inches squared"
            options2 = "b)452.16 inches squared"
            options3 = "c)75.36 inches squared"
            answer = "b)452.16 inches squared"
        elif ch>=11:
            name3 = request.session['name3']
            obj = get_object_or_404(AnswerModel, userId=uobj)
            obj.sessionfour = name3
            obj.save(update_fields=["sessionfour"])

            return redirect('selectsessionpage')


        else:
            question = "none"
            options1 = "none"
            options2 = "none"
            options3 = "none"
            answer = "none"
    elif select == "sessionfive":
        se = 'sessionfive'
        if ch == 1:
            question = "1)The radius of a circle is 3 inches. What is the area?"
            options1 = "a)9.25 inches squared "
            options2 = "b)20.28 inches squared "
            options3 = "c)28.26 inches squared"
            answer = "c)28.26 inches squared"
        elif ch == 2:
            question = "2)The diameter of a circle is 8 centimeters. What is the area?"
            options1 = "a)50.24 centimeters squared"
            options2 = "b)64 centimeters squared"
            options3 = "c)16.24 centimeters squared"
            answer = "a)50.24 centimeters squared"
        elif ch == 3:
            question = "3))A circle has a radius of 12 inches.  What is the area of the circle?"
            options1 = "a)400.14 inches squared"
            options2 = "b)452.16 inches squared"
            options3 = "c)75.36 inches squared"
            answer = "b)452.16 inches squared"

        elif ch == 4:
            question = " 4Mark has a circular swimming pool with are radius of 7 feet. If he wants a cover to go over the pool what is the least amount of material needed to cover the pool?"
            options1 = "a)43.96 feet squared"
            options2 = "b)21.98 feet squared"
            options3 = "c)153.86 feet squared"
            answer = "c)153.86 feet squared"


        elif ch == 5:
            question = "5)The chord is the longest diameter in a circle."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "b)False"

        elif ch == 6:
            question = "6)Molly is making pizza for supper and wants to cover the top of the pizza with sauce.She has measured the radius of the pizza to be 5 inches, how many square inches will the sauce cover?"
            options1 = "a)31.4 inches squared"
            options2 = "b)78.5 inches squared"
            options3 = "c)15.7 inches squared"
            answer = "b)78.5 inches squared"

        elif ch == 7:
            question = "7)Pam's mom is fixing cookies for her class.  She wants to put icing on the cookies.The radius of the cookies is 2 inches.She is making 20 cookies, what is the area that the icing will cover if she icings all 20 cookies?"
            options1 = "a)251.2 inches squared"
            options2 = "b)125.6 inches squared"
            options3 = "c)12.56 inches squared"
            answer = "a)251.2 inches squared"

        elif ch == 8:
            question = "8)A cicular stool needs to be covered with new fabric.  If the diameter of the stool is 2 feet, how much material is needed to cover the stool"
            options1 = "a)12.56 feet squared"
            options2 = "b)6.28 feet squared "
            options3 = "c)3.14 feet squared"
            answer = "c)3.14 feet squared"

        elif ch == 9:
            question = "9)The radius is always half of the diameter."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "a)True"

        elif ch == 10:
            question = "10)Sam has baked a circular cake.  The cake has a diameter of 10 inches.  Sam needs to know how much icing it will take to cover the top of the cake,which of the following was does Sam need to use to figure this out?"
            options1 = "a)10 x 3.14"
            options2 = "b)5 x 2 x 3.14"
            options3 = "c)5 x 5 x 3.14"
            answer = "c)5 x 5 x 3.14"
        elif ch == 11:
            name4 = request.session['name4']
            obj = get_object_or_404(AnswerModel, userId=uobj)
            obj.sessionfive = name4
            obj.save(update_fields=["sessionfive"])

            return redirect('selectsessionpage')

        else:
            question = "none"
            options1 = "none"
            options2 = "none"
            options3 = "none"
            answer = "none"

    data=[question,options1,options2,options3,answer]

    return render(request,'user/motivationalmegpage.html',{'view':data,'next':next,'se':se})
def notmotivationalmegpage(request,pk,session):
    userid = request.session['userid']
    uobj = RegistrationModel.objects.get(id=userid)
    tot = request.session['total']
    nam1 = request.session['name1']
    nam2 = request.session['name2']
    nam3 = request.session['name3']
    nam4 = request.session['name4']
    se = 'sessionone'
    if request.method == "POST":
        out = request.POST.get('val')
        if out == "correct":
            if session == "sessionone":
                tot = tot + 1
                request.session['total'] = tot
            elif session == "sessiontwo":
                nam1 = nam1 + 1
                request.session['name1'] = nam1
            elif session == "sessionthree":
                nam2 = nam2 + 1
                request.session['name2'] = nam2
            elif session == "sessionfour":
                nam3 = nam3 + 1
                request.session['name3'] = nam3
            elif session == "sessionfive":
                nam4 = nam4 + 1
                request.session['name4'] = nam4


    data = {}
    ch = int(pk)
    next = ch + 1
    question, options1, options2, options3, answer = '', '', '', '', ''
    if session=="sessionone":
        se = 'sessionone'
        if ch == 1:
            question = "1)If a population of yeast cells grows from 10 to 320 in a period of five hours, what is the rate of growth?"
            options1 = "a)It doubles its numbers every hour. "
            options2 = "b)It triples its numbers every hour "
            options3 = "c)It doubles its numbers every two hours."
            answer = "a)It doubles its numbers every hour."
        elif ch == 2:
            question = "2)The number of red blood corpuscles in one cubic millimeter is about 5,000,000, and the number of white blood corpuscles in one cubic millimeter is about 8,000. What, then, is the ratio of white blood corpuscles to red blood corpuscles?"
            options1 = "a)1:625"
            options2 = "b)1:40"
            options3 = "c)4:10"
            answer = "a)1:625"
        elif ch == 3:
            question = "3)Which of the following numbers can be divided evenly by 19?"
            options1 = "a)54"
            options2 = "b)63"
            options3 = "c)76"
            answer = "c)76"

        elif ch == 4:
            question = " 4)A rectangular tract of land measures 860 feet by 560 feet. Approximately how many acres is this? (one acre = 43,560 square feet)"
            options1 = "a)12.8 acres"
            options2 = "b)11.06 acres"
            options3 = "c)10.5 acres"
            answer = "b)11.06 acres"


        elif ch == 5:
            question = "5)On a particular morning the temperature went up 1 ° every two hours. If the temperature was 53° at 5 A.M., at what time was it 57°?"
            options1 = "a)1 p.m"
            options2 = "b)8 a.m"
            options3 = "c)7 a.m"
            answer = "a)1 p.m"

        elif ch == 6:
            question = "6)For health reasons, Amir wants to drink eight glasses of water a day. He has already had six glasses. What fraction is Amir left with?"
            options1 = "a)1/8"
            options2 = "b)1/6"
            options3 = "c)1/4"
            answer = "c)1/4"

        elif ch == 7:
            question = "7)A movie is scheduled for two hours. The theatre advertisements are 3.8 minutes long. There are two previews; one is 4.6 minutes long, and the other is.2.9 minutes long. The rest of time is devoted to the feature film. How long is the feature film?"
            options1 = "a)108.7 minutes"
            options2 = "b)97.5 minutes"
            options3 = "c)118.98 minutes"
            answer = "a)108.7 minutes"

        elif ch == 8:
            question = "8)Twelve is 20% of what number?"
            options1 = "a)5"
            options2 = "b)20 "
            options3 = "c)60"
            answer = "c)60"

        elif ch == 9:
            question = "9)The product of two and four more than three times a number is 20.What is the number?"
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "a)True"

        elif ch == 10:
            question = "10)Sam has baked a circular cake.  The cake has a diameter of 10 inches.  Sam needs to know how much icing it will take to cover the top of the cake,which of the following was does Sam need to use to figure this out?"
            options1 = "a)10 x 3.14"
            options2 = "b)5 x 2 x 3.14"
            options3 = "c)5 x 5 x 3.14"
            answer = "c)5 x 5 x 3.14"
        elif ch >= 11:
            total = request.session['total']
            AnswerModel.objects.create(userId=uobj, catagory="notmotivationalmessage", sessionone=total)
            return redirect('nonselectsessionpage')

        else:
            question = "none"
            options1 = "none"
            options2 = "none"
            options3 = "none"
            answer = "none"
    elif session=="sessiontwo":
        se = 'sessiontwo'
        if ch == 1:
            question = "1)The average of three numbers is 77.The first number is twice the second and the second number is twice the third. Find the first number."
            options1 = "a)33"
            options2 = "b)66"
            options3 = "c)132"
            answer = "c)132"
        elif ch == 2:
            question = "2)The average of 10 numbers is calculated as 15.It is discovered later on that while calculating the average one number, namely 36 was wrongly read as 26.The correct average is "
            options1 = "a)16"
            options2 = "b)14"
            options3 = "c)18.6"
            answer = "a)16"
        elif ch == 3:
            question = "3))A circle has a radius of 12 inches.  What is the area of the circle?"
            options1 = "a)400.14 inches squared"
            options2 = "b)452.16 inches squared"
            options3 = "c)75.36 inches squared"
            answer = "b)452.16 inches squared"

        elif ch == 4:
            question = " 4Mark has a circular swimming pool with are radius of 7 feet. If he wants a cover to go over the pool what is the least amount of material needed to cover the pool?"
            options1 = "a)43.96 feet squared"
            options2 = "b)21.98 feet squared"
            options3 = "c)153.86 feet squared"
            answer = "c)153.86 feet squared"


        elif ch == 5:
            question = "5)The chord is the longest diameter in a circle."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "b)False"

        elif ch == 6:
            question = "6)Molly is making pizza for supper and wants to cover the top of the pizza with sauce.She has measured the radius of the pizza to be 5 inches, how many square inches will the sauce cover?"
            options1 = "a)31.4 inches squared"
            options2 = "b)78.5 inches squared"
            options3 = "c)15.7 inches squared"
            answer = "b)78.5 inches squared"

        elif ch == 7:
            question = "7)Pam's mom is fixing cookies for her class.  She wants to put icing on the cookies.The radius of the cookies is 2 inches.She is making 20 cookies, what is the area that the icing will cover if she icings all 20 cookies?"
            options1 = "a)251.2 inches squared"
            options2 = "b)125.6 inches squared"
            options3 = "c)12.56 inches squared"
            answer = "a)251.2 inches squared"

        elif ch == 8:
            question = "8)A cicular stool needs to be covered with new fabric.  If the diameter of the stool is 2 feet, how much material is needed to cover the stool"
            options1 = "a)12.56 feet squared"
            options2 = "b)6.28 feet squared "
            options3 = "c)3.14 feet squared"
            answer = "c)3.14 feet squared"

        elif ch == 9:
            question = "9)The radius is always half of the diameter."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "a)True"

        elif ch == 10:
            question = "10)Sam has baked a circular cake.  The cake has a diameter of 10 inches.  Sam needs to know how much icing it will take to cover the top of the cake,which of the following was does Sam need to use to figure this out?"
            options1 = "a)10 x 3.14"
            options2 = "b)5 x 2 x 3.14"
            options3 = "c)5 x 5 x 3.14"
            answer = "c)5 x 5 x 3.14"
        elif ch==11:
            name1 = request.session['name1']
            obj = get_object_or_404(AnswerModel, userId=uobj)
            obj.sessionfive = name1
            obj.save(update_fields=["sessionone"])
            return redirect('nonselectsessionpage')
        else:
            question = "none"
            options1 = "none"
            options2 = "none"
            options3 = "none"
            answer = "none"
    elif session == "sessionthree":
        se = 'sessionthree'
        if ch == 1:
            question = "1)A cicular stool needs to be covered with new fabric.  If the diameter of the stool is 2 feet, how much material is needed to cover the stool"
            options1 = "a)12.56 feet squared"
            options2 = "b)6.28 feet squared "
            options3 = "c)3.14 feet squared"
            answer = "c)3.14 feet squared"
        elif ch == 2:
            question = "2)The average of 10 numbers is calculated as 15.It is discovered later on that while calculating the average one number, namely 36 was wrongly read as 26.The correct average is "
            options1 = "a)16"
            options2 = "b)14"
            options3 = "c)18.6"
            answer = "a)16"
        elif ch == 3:
            question = "3)The chord is the longest diameter in a circle."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "b)False"

        elif ch == 4:
            question = "4)Molly is making pizza for supper and wants to cover the top of the pizza with sauce.She has measured the radius of the pizza to be 5 inches, how many square inches will the sauce cover?"
            options1 = "a)31.4 inches squared"
            options2 = "b)78.5 inches squared"
            options3 = "c)15.7 inches squared"
            answer = "b)78.5 inches squared"

        elif ch == 5:
            question = "5)Pam's mom is fixing cookies for her class.  She wants to put icing on the cookies.The radius of the cookies is 2 inches.She is making 20 cookies, what is the area that the icing will cover if she icings all 20 cookies?"
            options1 = "a)251.2 inches squared"
            options2 = "b)125.6 inches squared"
            options3 = "c)12.56 inches squared"
            answer = "a)251.2 inches squared"
        elif ch == 6:
            question = "6)The radius is always half of the diameter."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "a)True"

        elif ch == 7:
            question = "7)Sam has baked a circular cake.  The cake has a diameter of 10 inches.  Sam needs to know how much icing it will take to cover the top of the cake,which of the following was does Sam need to use to figure this out?"
            options1 = "a)10 x 3.14"
            options2 = "b)5 x 2 x 3.14"
            options3 = "c)5 x 5 x 3.14"
            answer = "c)5 x 5 x 3.14"
        elif ch == 8:
            question = "8)The radius of a circle is 3 inches. What is the area?"
            options1 = "a)9.25 inches squared "
            options2 = "b)20.28 inches squared "
            options3 = "c)28.26 inches squared"
            answer = "c)28.26 inches squared"
        elif ch == 9:
            question = "9)The diameter of a circle is 8 centimeters. What is the area?"
            options1 = "a)50.24 centimeters squared"
            options2 = "b)64 centimeters squared"
            options3 = "c)16.24 centimeters squared"
            answer = "a)50.24 centimeters squared"
        elif ch == 10:
            question = "10))A circle has a radius of 12 inches.  What is the area of the circle?"
            options1 = "a)400.14 inches squared"
            options2 = "b)452.16 inches squared"
            options3 = "c)75.36 inches squared"
            answer = "b)452.16 inches squared"
        elif ch>=11:
            name2 = request.session['name2']
            obj = get_object_or_404(AnswerModel, userId=uobj)
            obj.sessiontwo = name2
            obj.save(update_fields=["sessiontwo"])
            return redirect('nonselectsessionpage')
        else:
            question = "none"
            options1 = "none"
            options2 = "none"
            options3 = "none"
            answer = "none"
    elif session == "sessionfour":
        se = 'sessionfour'
        if ch == 1:
            question = "1)If a population of yeast cells grows from 10 to 320 in a period of five hours, what is the rate of growth?"
            options1 = "a)It doubles its numbers every hour. "
            options2 = "b)It triples its numbers every hour "
            options3 = "c)It doubles its numbers every two hours."
            answer = "a)It doubles its numbers every hour."
        elif ch == 2:
            question = "2)The number of red blood corpuscles in one cubic millimeter is about 5,000,000, and the number of white blood corpuscles in one cubic millimeter is about 8,000. What, then, is the ratio of white blood corpuscles to red blood corpuscles?"
            options1 = "a)1:625"
            options2 = "b)1:40"
            options3 = "c)4:10"
            answer = "a)1:625"
        elif ch == 3:
            question = "3)Which of the following numbers can be divided evenly by 19?"
            options1 = "a)54"
            options2 = "b)63"
            options3 = "c)76"
            answer = "c)76"

        elif ch == 4:
            question = " 4)A rectangular tract of land measures 860 feet by 560 feet. Approximately how many acres is this? (one acre = 43,560 square feet)"
            options1 = "a)12.8 acres"
            options2 = "b)11.06 acres"
            options3 = "c)10.5 acres"
            answer = "b)11.06 acres"


        elif ch == 5:
            question = "5)On a particular morning the temperature went up 1 ° every two hours. If the temperature was 53° at 5 A.M., at what time was it 57°?"
            options1 = "a)1 p.m"
            options2 = "b)8 a.m"
            options3 = "c)7 a.m"
            answer = "a)1 p.m"

        elif ch == 6:
            question = "6)For health reasons, Amir wants to drink eight glasses of water a day. He has already had six glasses. What fraction is Amir left with?"
            options1 = "a)1/8"
            options2 = "b)1/6"
            options3 = "c)1/4"
            answer = "c)1/4"

        elif ch == 7:
            question = "7)A movie is scheduled for two hours. The theatre advertisements are 3.8 minutes long. There are two previews; one is 4.6 minutes long, and the other is.2.9 minutes long. The rest of time is devoted to the feature film. How long is the feature film?"
            options1 = "a)108.7 minutes"
            options2 = "b)97.5 minutes"
            options3 = "c)118.98 minutes"
            answer = "a)108.7 minutes"

        elif ch == 8:
            question = "8)Twelve is 20% of what number?"
            options1 = "a)5"
            options2 = "b)20 "
            options3 = "c)60"
            answer = "c)60"

        elif ch == 9:
            question = "9)The product of two and four more than three times a number is 20.What is the number?"
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "a)True"

        elif ch == 10:
            question = "10)Sam has baked a circular cake.  The cake has a diameter of 10 inches.  Sam needs to know how much icing it will take to cover the top of the cake,which of the following was does Sam need to use to figure this out?"
            options1 = "a)10 x 3.14"
            options2 = "b)5 x 2 x 3.14"
            options3 = "c)5 x 5 x 3.14"
            answer = "c)5 x 5 x 3.14"
        elif ch >= 11:
            name3 = request.session['name3']
            obj = get_object_or_404(AnswerModel, userId=uobj)
            obj.sessionthree = name3
            obj.save(update_fields=["sessionthree"])
            return redirect('nonselectsessionpage')

        else:
            question = "none"
            options1 = "none"
            options2 = "none"
            options3 = "none"
            answer = "none"
    elif session == "sessionfive":
        se = 'sessionfive'
        if ch == 1:
            question = "1)The radius of a circle is 3 inches. What is the area?"
            options1 = "a)9.25 inches squared "
            options2 = "b)20.28 inches squared "
            options3 = "c)28.26 inches squared"
            answer = "c)28.26 inches squared"
        elif ch == 2:
            question = "2)The diameter of a circle is 8 centimeters. What is the area?"
            options1 = "a)50.24 centimeters squared"
            options2 = "b)64 centimeters squared"
            options3 = "c)16.24 centimeters squared"
            answer = "a)50.24 centimeters squared"
        elif ch == 3:
            question = "3))A circle has a radius of 12 inches.  What is the area of the circle?"
            options1 = "a)400.14 inches squared"
            options2 = "b)452.16 inches squared"
            options3 = "c)75.36 inches squared"
            answer = "b)452.16 inches squared"

        elif ch == 4:
            question = " 4Mark has a circular swimming pool with are radius of 7 feet. If he wants a cover to go over the pool what is the least amount of material needed to cover the pool?"
            options1 = "a)43.96 feet squared"
            options2 = "b)21.98 feet squared"
            options3 = "c)153.86 feet squared"
            answer = "c)153.86 feet squared"


        elif ch == 5:
            question = "5)The chord is the longest diameter in a circle."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "b)False"

        elif ch == 6:
            question = "6)Molly is making pizza for supper and wants to cover the top of the pizza with sauce.She has measured the radius of the pizza to be 5 inches, how many square inches will the sauce cover?"
            options1 = "a)31.4 inches squared"
            options2 = "b)78.5 inches squared"
            options3 = "c)15.7 inches squared"
            answer = "b)78.5 inches squared"

        elif ch == 7:
            question = "7)Pam's mom is fixing cookies for her class.  She wants to put icing on the cookies.The radius of the cookies is 2 inches.She is making 20 cookies, what is the area that the icing will cover if she icings all 20 cookies?"
            options1 = "a)251.2 inches squared"
            options2 = "b)125.6 inches squared"
            options3 = "c)12.56 inches squared"
            answer = "a)251.2 inches squared"

        elif ch == 8:
            question = "8)A cicular stool needs to be covered with new fabric.  If the diameter of the stool is 2 feet, how much material is needed to cover the stool"
            options1 = "a)12.56 feet squared"
            options2 = "b)6.28 feet squared "
            options3 = "c)3.14 feet squared"
            answer = "c)3.14 feet squared"

        elif ch == 9:
            question = "9)The radius is always half of the diameter."
            options1 = "a)True"
            options2 = "b)False"
            options3 = "c)a and b"
            answer = "a)True"

        elif ch == 10:
            question = "10)Sam has baked a circular cake.  The cake has a diameter of 10 inches.  Sam needs to know how much icing it will take to cover the top of the cake,which of the following was does Sam need to use to figure this out?"
            options1 = "a)10 x 3.14"
            options2 = "b)5 x 2 x 3.14"
            options3 = "c)5 x 5 x 3.14"
            answer = "c)5 x 5 x 3.14"
        elif ch >= 11:
            name4 = request.session['name4']
            obj = get_object_or_404(AnswerModel, userId=uobj)
            obj.sessionfive = name4
            obj.save(update_fields=["sessionfive"])
            return redirect('nonselectsessionpage')

        else:
            question = "none"
            options1 = "none"
            options2 = "none"
            options3 = "none"
            answer = "none"

    data = [question, options1, options2, options3, answer]

    return render(request,'user/notmotivationalmegpage.html',{'view_question':data,'next':next,'se':se})

def selectsessionpage(request):
    return render(request,'user/selectsessionpage.html')
def nonselectsessionpage(request):
    return render(request,'user/nonselectsessionpage.html')
def logout(request):
    return render(request,'logout')

def mydetails(request):
    userid = request.session['userid']
    ted = RegistrationModel.objects.get(id=userid)
    return render(request, 'user/mydetails.html', {'object': ted})

def updatemydetails(request):
    userid = request.session['userid']
    objec = RegistrationModel.objects.get(id=userid)
    if request.method == "POST":
        FirstName = request.POST.get('FirstName', '')
        LastName = request.POST.get('LastName', '')
        UserId = request.POST.get('UserId', '')
        Password = request.POST.get('Password', '')
        MobileNumber = request.POST.get('MobileNumber', '')
        EmailId = request.POST.get('EmailId', '')
        Gender = request.POST.get('Gender', '')

        obj = get_object_or_404(RegistrationModel, id=userid)
        obj.firstname = FirstName
        obj.lastname = LastName
        obj.userid = UserId
        obj.password = Password
        obj.mobilenumber = MobileNumber
        obj.emailid = EmailId
        obj.gender = Gender

        obj.save(update_fields=["firstname", "lastname","userid", "password", "mobilenumber", "emailid",
                                "gender", ])
        return redirect('mydetails')

    return render(request,'user/updatemydetails.html',{'obj': objec})

def viewnotification(request):
    obj = NotificationModel.objects.all()
    return render(request,'user/viewnotification.html',{'object':obj})

def feedback(request):
    userid = request.session['userid']
    object = RegistrationModel.objects.get(id=userid)
    if request.method=="POST":
        feed=request.POST.get('feedback')
        FeedbackModel.objects.create(username=object,feedback=feed)

    return render(request,'user/feedback.html')