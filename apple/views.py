from django.http import HttpResponse


def generic( request ) :
    return HttpResponse( u'Works!' )