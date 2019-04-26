import jinja2

templ = """
{%- for item in items recursive %}
    {{item.name}}
    {%- if item.children %}
        {{- loop(item.children) }}
    {%- endif %}
{%- endfor %}
"""

items = [{'name': 'Bobby'},
         {'name': 'Jack',
          'children': [
              {'name': 'Jake'},
              {'name': 'Jill'}]},
         {'name': 'Babby', 'children': []}]

template = jinja2.Template(templ)
print(template.render(items=items))