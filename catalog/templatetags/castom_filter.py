from django import template


register = template.Library()


@register.filter()
def mymedia(path_img):
    if path_img:
        return path_img.url
    else:
        return '#'

    
@register.filter()
def active_version(vesrsions):
    active_version = [v for v in vesrsions if v.is_active==True]
    return active_version
   