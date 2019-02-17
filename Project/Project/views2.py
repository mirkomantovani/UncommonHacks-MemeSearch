from django.http import HttpResponse
from django.template import loader

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def results(request):
   query = request.GET['query']
   #INSERT PROCESSING HERE #
   res = ["https://i.redd.it/flnltgom9zg21.jpg","https://i.redd.it/20ine7d2ntg21.jpg","https://i.redd.it/uwtae12j0tg21.jpg"]
   template = loader.get_template("results.html")
   context = {'images' : res,'query':query}
   return HttpResponse(template.render(context,request))

def home(request):
  template = loader.get_template("home.html")
  context = {'value' : ""}
  return HttpResponse(template.render(context,request))

