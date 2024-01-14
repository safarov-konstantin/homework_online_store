from django import template


register = template.Library()


@register.filter()
def mymedia(path_img):
    if path_img:
        return path_img.url
    else:
        return '#'
    