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
            },

        ]
    }

    return render(request, 'email_hubbler/index.html',context)

def emailsent(request):
    user_name = request.POST.get('5b46029bc20a6b25bbf51e74')
    feedback = request.POST.get('5b471e70c20a6b5d789f560d')
    ticket_number = request.POST.get('5b46029bc20a6b25bbf51e76')

    
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