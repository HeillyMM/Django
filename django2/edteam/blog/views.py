from django.shortcuts import render

# Create your views here.

# siempre se recibe como parametro el rquest
def index(request):
    lista_articulos = [
        {
            "titulo":"mover,copiar y ddd",
            "imagen":"https://www.msn.com/es-xl/noticias/other/hantavirus-c%C3%B3mo-se-transmite-y-cu%C3%A1l-es-su-letalidad/ar-AA23wFow?ocid=msedgntp&pc=U531&cvid=6a0f588a3aa043ad84732606e98172d3&ei=6",
            "autor":"Alvaro felipe chavez"
         },
         {
            "titulo":"el camino del frontend",
            "imagen":"https://www.msn.com/es-xl/noticias/other/hantavirus-c%C3%B3mo-se-transmite-y-cu%C3%A1l-es-su-letalidad/ar-AA23wFow?ocid=msedgntp&pc=U531&cvid=6a0f588a3aa043ad84732606e98172d3&ei=6",
            "autor":"Jilmeriz Lopez"
         },
         {
            "titulo":"la ruta del desarrollador backend",
            "imagen":"https://www.msn.com/es-xl/noticias/other/hantavirus-c%C3%B3mo-se-transmite-y-cu%C3%A1l-es-su-letalidad/ar-AA23wFow?ocid=msedgntp&pc=U531&cvid=6a0f588a3aa043ad84732606e98172d3&ei=6",
            "autor":"Alvaro felipe chavez"
         }
    ]
    
    context = {
        "articulos":lista_articulos
    }
    return render(request,"blog/index.html",context)