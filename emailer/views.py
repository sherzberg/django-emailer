from django.http import HttpResponse
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