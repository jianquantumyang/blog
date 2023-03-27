from django.views.generic import ListView,CreateView
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from two.forms import AddCategoryForm, AddPostForm
from .models import Category, Blog
# Create your views here.




menu = [
    {'title_name':"О Сайте","url_name":"about"},
    {'title_name':"Добавить статью","url_name":"addpage"},
    {'title_name':"Добавить категории","url_name":"category_add"},
]


    
class IndexHome(ListView):
    paginate_by = 3
    model = Blog
    template_name="index.html"
    context_object_name = "posts"
    
    def get_context_data(self, *, object_list=None, **kwargs ):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = "Дом"
        context['cat_selected'] = 0
        context['cats']= Category.objects.all()
        return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
# def index(req):
#     # print(BASE_DIR)

#     posts = Blog.objects.all()
#     p = Paginator(posts, 1)
#     page_number = req.GET.get("page")
    
#     context = {
#         "posts":p.get_page(page_number),
#         'menu':menu,
        
#         'title':'Главная страница',
#         'cats':Category.objects.all(),
#         'cat_selected':0,
#     }
#     return render(req, "index.html", context=context)




# Category
def show_category(req,cat_id):
    posts = Blog.objects.filter(cat_id=cat_id)
    p = Paginator(posts, 5)
    page_number = req.GET.get("page")
    cons = Category.objects.filter(id=cat_id)
    context = {
        "menu":menu,
        "posts":p.get_page(page_number),
        "title": 'Категория - ' + cons[0].name,
        'cats':Category.objects.all(),
        'cat_selected':cat_id,
    }
    
    return render(req,"show_category.html",context=context)
   


def about(request):
    return render(request,"about.html",context={"menu":menu})

def post(req,post_id):
    
    blog = Blog.objects.filter(id=post_id)[0]

    context={
        "post_id":post_id,
        "blog": blog,
        "title":blog.title,
        "menu":menu,
        'cats': Category.objects.all(),
    }
    return render(req,"post.html",context=context)


class AddPage(CreateView):
    form_class= AddPostForm
    template_name="addpage.html"
    def get_context_data(self, *, object_list=None, **kwargs ):
        
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = "Добавление статьи"
        return context
#AddPage
# def addpage(req):
#     form = AddPostForm()
    
#     if req.method =="POST":
#         form =  AddPostForm(req.POST,req.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
#         else:
#             context = {
#             'form':form,    
#             'menu':menu,
#             'title':'Добавление статьи'
#             }
#             pass
#     else:
#         form = AddPostForm()
#         context = {
#         'form':form,    
#         'menu':menu,
#         'title':'Добавление статьи'
#         }
    
    
   
    
    

#     return render(req,"addpage.html",context=context)


def post_category_add(req):
    form = AddCategoryForm()
    if req.method == "POST":
        form = AddCategoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context= {
        "form": form,
        "title":"Добавление категории"
    }
    return render(req,"post_category_add.html",context=context)
