from django.shortcuts import render
from django.http import HttpResponse
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
                'id': '5b471e70c20a6b5d789f560d',
                'lbl':'Number',
                'placeholder':'Ticket number'
            }
        ]
    }

    return render(request, 'email_hubbler/index.html',context)

def emailsent(request):
    return HttpResponse(request.POST.get('5b46029bc20a6b25bbf51e74'))