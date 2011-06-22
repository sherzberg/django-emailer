from django.contrib import admin
from django import forms

try:
    from tinymce.widgets import TinyMCE as HtmlWidget
except:
    from django.forms import Textarea as HtmlWidget
    
from emailer.models import *
     
class EmailAdminForm(forms.ModelForm):  
    html = forms.CharField(widget=HtmlWidget(attrs={'cols': 80, 'rows': 40}))
    
    class Meta:
        model = Email
        
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email_blast', 'to_address', 'status', 'opened', 'get_tracking_png_url',)
    list_filter = ('status',)
    form = EmailAdminForm

class EmailBlastAdminForm(forms.ModelForm):  
    html = forms.CharField(widget=HtmlWidget(attrs={'cols': 80, 'rows': 40}))
    
    class Meta:
        model = EmailBlast
           
class EmailBlastAdmin(admin.ModelAdmin):
    list_display = ('name', 'send_after',)
    list_filter = ('type', 'send_after',)
    form = EmailBlastAdminForm
    
class EmailTemplateAdminForm(forms.ModelForm):
    name = forms.CharField()
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={'cols': 80, 'rows': 4}))    
    html = forms.CharField(widget=HtmlWidget(attrs={'cols': 80, 'rows': 40}))
                           
class EmailTemplateAdmin(admin.ModelAdmin):                           
    list_display = ('name', 'date_created',)
    form = EmailTemplateAdminForm
    
class EmailListAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_created',)
    
admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(EmailBlast, EmailBlastAdmin)
#admin.site.register(EmailList)