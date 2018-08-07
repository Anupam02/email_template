from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

# Function for default page
def index(request):
    # return HttpResponse("Hello this")

    # showing a default form 
    context = {
        'fields':
        [ 
            {
                'type':'text',
                'id': '5b46029bc20a6b25bbf51e74',
                'lbl': 'User Name',
                'placeholder':'User name'
            },
            {
                'type':'paragraph',
                'id':  '5b471e70c20a6b5d789f560d',
                'lbl':'paragraph',
                'placeholder':'Feedback'
            },
            {
                'type':'number',
                'id': '5b46029bc20a6b25bbf51e76',
                'lbl':'Number',
                'placeholder':'Ticket number'
            }
        ]
    }

    return render(request, 'email_hubbler/index.html',context)

def emailsent(request):
    user_name = request.POST.get('5b46029bc20a6b25bbf51e74')
    feedback = request.POST.get('5b471e70c20a6b5d789f560d')
    ticket_number = request.POST.get('5b46029bc20a6b25bbf51e76')
    subject = "Feedback Ticket " + str(ticket_number)
    # message = "<p>Hello <span class='atwho-inserted' data-atwho-at-query='#'><span id='5b46029bc20a6b25bbf51e74' class='customFields'>"+user_name+"</span></span>⁠,</p><p><br></p><p>Greetings from hubbler. It has been privilege to serve you.&nbsp;</p><p>Your below Feedback &nbsp;is received:</p><p><span class='atwho-inserted' data-atwho-at-query='#'><span id='5b471e70c20a6b5d789f560d' class='customFields'>" + feedback + "</span></span>⁠&nbsp;</p><p><br></p><p>Your Ticket Number : <span class='atwho-inserted' data-atwho-at-query='#'><span id='5b46029bc20a6b25bbf51e76' class='customFields'>" + str(ticket_number)+"</span></span>⁠ is raised and will be responded to asap.</p><p><br></p><p>Happy Hubblering!!</p><p>Team Hubbler</p>"
    msg_html = render_to_string('email_hubbler/email.html',{'user_name':user_name,'feedback':feedback,'ticket_number':ticket_number})
    send_mail(subject,'Hello there','patel.anupam02@gmail.com',['patel.anupam02@gmail.com'],html_message=msg_html)
    return HttpResponse('<h3>Email has been sent succesfully.</h3>')