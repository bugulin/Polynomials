from .format import form
from .postfix import to_postfix

def parse(text):
    return to_postfix(form(text))
