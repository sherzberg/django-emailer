// This list was created by django-emailer

var tinyMCETemplateList = [
    // Name, URL, Description

    {% for template in templates %}
    ["{{template.name}}", "{{template.get_absolute_url}}", "{{template.description}}"],
    {% endfor %}

];
