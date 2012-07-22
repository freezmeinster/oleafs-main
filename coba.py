from django.template import Template

word = """
{% block apa %}
asdfasfadsfasdf
{% endblock %}

{% block nu %}
asdfasdf
{% endblock %}
"""

b = Template(word)

