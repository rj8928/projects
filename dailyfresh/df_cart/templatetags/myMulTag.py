# coding=utf-8
from django import template
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()


class MulTag(Node):
    def __init__(self, numList):
        self.numList = numList

    def render(self, context):
        realList = []
        try:
            for numobj in self.numList:
                realList.append(numobj.resolve(context))
        except:
            raise TemplateSyntaxError("multag error")
        try:
            value = realList[0]
            for num in realList[1:]:
                value = value * num
            return round(value, 2)
        except:
            return ''


@register.tag(name="mymul")
def getMulNums(parser, token):
    bits = token.contents.split()
    realList = [parser.compile_filter(x) for x in bits[1:]]
    return MulTag(realList)