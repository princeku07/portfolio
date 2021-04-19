from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Contact,Post,Category

# Create your views here.
class HomeView(ListView):
    model=Post
    template_name = 'home.html'  
    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
# def home(request):
    
#     return render(request,'home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        message = request.POST.get('message','')
        contact = Contact(name=name , phone=phone ,email=email,message=message)
        contact.save()
    return render(request,'contact.html')

def about(request):
    
    return render(request,'about.html')

def project(request):
    return render(request,'projects.html')




class PostListView(ListView):
    model = Post
    category = Category.objects.all()
    template_name = 'blog.html'
    paginate_by = 4
    paginate_orphans = 1
    
    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category= cats)
    
    return render(request,'categories.html',{'cats':cats,'category_posts':category_posts})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
