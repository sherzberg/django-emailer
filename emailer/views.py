from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from emailer.models import EmailTemplate
import Image

from emailer.models import Email

def tracking(request, tracking_id):

    email = Email.objects.email_from_tracking(tracking_id)
    if email:
        email.opened = True
        email.save()
        
    image = Image.new("RGB", (1, 1))
    response = HttpResponse(mimetype="image/png")
    image.save(response, "PNG")
    
    return response

def templates(request):
    templates = EmailTemplate.objects.all()
    return render_to_response('emailer/template_list.js', {'templates': templates},
            context_instance=RequestContext(request), 
            mimetype='text/javascript')
    
def template(request, template_id):
    template = get_object_or_404(EmailTemplate, id = template_id)
    
    response = HttpResponse(template.html)
    return response
