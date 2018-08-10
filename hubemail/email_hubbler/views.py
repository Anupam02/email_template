from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail,EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

user_name = None
feedback = None
ticket_number = None
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
            },

        ]
    }

    return render(request, 'email_hubbler/index.html',context)

def emailsent(request):
    user_name = request.POST.get('5b46029bc20a6b25bbf51e74')
    feedback = request.POST.get('5b471e70c20a6b5d789f560d')
    ticket_number = request.POST.get('5b46029bc20a6b25bbf51e76')
    info_list = [user_name, feedback, ticket_number]
    request.session['info'] = info_list
    
    
    context = {
    'subjectTags':
        [ 
            {
                'type':'#Number',
                'id': '5b46029bc20a6b25bbf51e76',
                'from':16,
                'to': 23,
                'lenght': len(user_name)
            },

        ],
     'emailBodyTags' :
        [
            {
                'text':'#single line text',
                'id' : '5b46029bc20a6b25bbf51e74',
                'from':119,
                'to':136,
                'length': len(user_name)
            },
            {
                'text':'#Paragraph',
                'id':'5b471e70c20a6b5d789f560d',
                'from':397,
                'to':407,
                'length': len(feedback)
            },
            {
                'text':'#Number',
                'id':'5b46029bc20a6b25bbf51e76',
                'from':577,
                'to':584,
                'length': len(ticket_number)
            }
        ]
    }
  
    return render(request, 'email_hubbler/email_template1.html',context)

def send_mail(request):
    session_list = request.session.get('info')
    # from_first_view = request.session[0]

    to = request.POST.get('to')
    cc = request.POST.get('cc')
    from_s = request.POST.get('from')
    subject = request.POST.get('subject')
    email_body = request.POST.get('emailbody')
    # from_index_subject= subject.find("#")

    subject_updated = ' '.join(session_list[2] if word.startswith('#') else word for word in subject.split())
    email_body_updated = []
    count = 0
    print(session_list)
    # for word in email_body.split():
    #     if word.startswith('#'):
    #         email_body_updated.append(session_list[count])
    #         count = count + 1
    #     else:
    #         email_body_updated.append(word)
    # email_body_updated_str = ' '.join(x for x in email_body_updated)
    # email_body_updated_formatted = ''
    words = []
    for line in email_body.split('\n'):
        words.extend(line.split())
        words.append('\n')

    for word in words:
        if word.startswith('#'):
            email_body_updated.append(session_list[count])
            count = count + 1
        else:
            email_body_updated.append(word) 

    email_body_updated_str = ' '.join( x for x in email_body_updated)           

    # send_mail(subject_updated,email_body_updated_str,from_s,[to])
    # email_body_updated = ' '.join( user_name if word.startswith('#') else word for word in email_body.split())
    # from_index_email_body_user = email_body.find()

    email = EmailMessage(subject_updated, email_body_updated_str, to=[to])
    email.send()
    return HttpResponse("Mail has been sent!!!")