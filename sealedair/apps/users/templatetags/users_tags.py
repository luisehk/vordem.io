from django import template
register = template.Library()


@register.simple_tag(takes_context=True)
def change_words(context, word):
    if word == "oldpassword":
        return "Contraseña actual"
    if word == "password1":
        return "Nueva contraseña"
    if word == "password2":
        return "Confirmar contraseña"
