
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponseRedirect , HttpResponse
import simplejson


from utils import quitar_tildes, quitar_words, preprocesar

@ensure_csrf_cookie
def home(request):
    file_poem = open('ihc_game/poema.txt').read()
    print file_poem
    trap_word = 'clavo'

    txt_lst = file_poem.split()
    n_txt_lst = []
    for i in txt_lst:
        if i != trap_word:
            n_txt_lst.append(i)

    fixed_poem = ' '.join(n_txt_lst)

    return render_to_response('home.html' , {'poema' : file_poem , 'trap_word':trap_word, 'fixed_poem':fixed_poem}, context_instance=RequestContext(request));


def analizar(request):
    print request.POST
    if request.POST.has_key('texto'):

        print 'analizar';
        texto = request.POST['texto']
        print texto
        texto_real = request.POST['texto_real']
        print texto_real
        palabra = request.POST['palabra']
        print palabra


        print "tipo de dato", type(texto)

        palabra = preprocesar(palabra)

        texto_real = preprocesar(texto_real)
        texto_real = quitar_words(texto_real, palabra)
        
        texto = preprocesar(texto)


        iguales = texto_real == texto

        print palabra, texto_real, texto, iguales

        response_dict = {}
        response_dict.update({'respuesta':iguales})
    
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

    else :
        return render_to_response('home.html', context_instance=RequestContext(request) ) 





































