from django.shortcuts import render , HttpResponse
from .models import *
from Codekaro import settings
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.core.mail import send_mail , EmailMessage
from . tokens import generate_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib import messages
from django.shortcuts import redirect
from user_agents import parse
from django.db.models import IntegerField
from django.db.models.functions import Cast
# Create your views here.



def home(request):
    variable_name = 'visit_count'  # Assuming 'visit_count' is the variable you want to increase
    try:
        # Try to get the variable from the database
        variable = GlobalVariable.objects.get(variable_name=variable_name)

        # Increment the value
        if request.user.is_superuser:
            variable.variable_value += 0
        else:
            variable.variable_value += 1

    except GlobalVariable.DoesNotExist:
        # If the variable doesn't exist in the database, create a new record
        variable = GlobalVariable(variable_name=variable_name, variable_value=1)

    variable.save()  # Save the changes to the database

    visits = {'vis' : variable.variable_value}
    return render(request , 'home.html' , visits)


def templates(request):
    return render(request , 'templates.html')

def addf(request):
    context = {'success' : False}
    if request.method == "POST" :
        name = request.POST['name']
        email = request.user.email
        description = request.POST['desc']
        link = request.POST['link']

        ins = add(name = name , email = email , description = description , link = link)
        ins.save()
        user = request.user.username
        context = {'success' :True , 'username' : user}
        return render(request , 'Addprob.html' , context)
    return render(request , 'Addprob.html' , context)


def signout(request):
    context = {'log' : False}
    if request.method == "POST" :
        logout(request)
        context = {'log' : True}
        return render(request , 'signin.html' , context)

def signup(request) :
    context = {'sent' : False , 'nsent' : False}
    checking = {'exist' : True}
    if request.method == "POST" :
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email =request.POST['email']
        check = User.objects.filter(email = email)

        if(check.exists()) :
            return render(request , 'signup.html' , checking)

        if((len(username) == 0) or (len(fname) == 0) or (pass1 != pass2)) :
            context = {'sent' : False , 'nsent' : True}
            return render(request , 'signup.html' , context)

        myuser = User.objects.create_user(username=username , email=email , password= pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        #myuser.save()

        
        
        # Welcome Email
        subject = "Welcome upcoming sniper!"
        message = "Hello, Hope you are good and healthy " + myuser.username + "!" + " Thank you for adding us to your basket! , We have sent you a confirmation email, please activate your account.."
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject=subject ,message= message ,from_email= from_email ,recipient_list= to_list , fail_silently = False)

         # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = False
        email.send()
        context = {'sent' : True}
        return render(request , 'signin.html' , context)
    return render(request , 'signup.html')


def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')



def signin(request):
    context = {'success' : False}
     
    if request.method == "POST" :
        
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username = username , password = pass1)
        context = {'success' : True , 'username' : username}    
        
        if user is not None :
            login(request , user)
            return render(request , "home.html" , context )
        else :
            return render(request , 'signin.html' , context)
        
    return render(request , 'signin.html')    


def searchf(request) :
    query = request.GET['search']

    brains = list(brain.objects.all())
    recursions = list(recursion.objects.all())
    beginners = list(beginner.objects.all())
    greeds = list(greed.objects.all())
    brutes = list(brute.objects.all())
    subs = list(sub.objects.all())
    implements = list(implement.objects.all())
    sorts = list(sort.objects.all())
    binaries = list(binary.objects.all())
    pointers = list(pointer.objects.all())
    hashs = list(hash.objects.all())
    pairs = list(pair.objects.all())
    dpstands = list(dpstand.objects.all())
    dps = list(dp.objects.all())
    trees = list(tree.objects.all())
    graphs = list(graph.objects.all())
    dsus = list(dsu.objects.all())
    segtrees = list(segtree.objects.all())
    mixes = list(mixed.objects.all())
    bits = list(bit.objects.all())
    all_objects = bits + brains + recursions + beginners + greeds + brutes + subs + implements + sorts + binaries + pointers + hashs + pairs + dpstands + dps + trees + graphs + dsus + segtrees + mixes
    all_objects = sorted(all_objects, key=lambda obj: int(obj.order))
    user_agent = parse(request.META['HTTP_USER_AGENT'])

    filtered = [obj for obj in all_objects if obj.name.startswith(query)]
    params = {'questions' : filtered}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'searchphone.html' , params)
    else :
        return render(request , 'search.html' , params)


def brainf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    
    brains = sorted(brain.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : brains}

    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)

def bitf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    
    bits = sorted(bit.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : bits}

    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)    
    
def recursionf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])

    recursions = sorted(recursion.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : recursions}
    
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)

def beginnerf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    beginners = sorted(beginner.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : beginners}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def brutef(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    brutes = sorted(brute.objects.all() , key=lambda obj: int(obj.order))
    
    params = {'questions' : brutes}
    
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)

def greedf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    greeds = sorted(greed.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : greeds}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def subf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    subs = sorted(sub.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : subs}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def implementf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    implements = sorted(implement.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : implements}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def sortf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    sorts = sorted(sort.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : sorts}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def binaryf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    binaries = sorted(binary.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : binaries}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def pointerf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    pointers = sorted(pointer.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : pointers}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def hashf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    hashs = sorted(hash.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : hashs}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def pairf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    pairs = sorted(pair.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : pairs}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def dpstandf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    dpstands = sorted(dpstand.objects.all(), key=lambda obj: int(obj.order))
    params = {'questions' : dpstands}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def dpf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    dps = sorted(dp.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : dps}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def treef(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    trees = sorted(tree.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : trees}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def graphf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    graphs = sorted(graph.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : graphs}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def dsuf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    dsus = sorted(dsu.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : dsus}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)


def segtreef(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    segtrees = sorted(segtree.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : segtrees}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)
    

def mixedf(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    mixes = sorted(mixed.objects.all() , key=lambda obj: int(obj.order))
    params = {'questions' : mixes}
    if (user_agent.is_mobile or user_agent.is_tablet) :
        return render(request , 'brainphone.html' , params)
    else :
        return render(request , 'brain.html' , params)