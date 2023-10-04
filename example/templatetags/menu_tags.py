from django import template
from example.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_path = context['request'].path
    menu_items = MenuItem.objects.filter(menu_name=menu_name, parent=None)

    def render_menu_item(menu_item):
        children = menu_item.children.all()
        active_class = 'active' if current_path.startswith(menu_item.url) else ''
        if children:
            return f'<li class="{active_class}"><a href="{menu_item.url}">{menu_item.title}</a><ul>{"".join(render_menu_item(child) for child in children)}</ul></li>'
        return f'<li class="{active_class}"><a href="{menu_item.url}">{menu_item.title}</a></li>'

    menu_html = "".join(render_menu_item(item) for item in menu_items)
    return f'<ul>{menu_html}</ul>'