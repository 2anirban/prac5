from django.shortcuts import render
from .models import *
from .forms import *

#fields=["author1","title1","body1","image1"]
def from1(request):
    if request.method=="POST":
        form=blogform1(request.POST)
        if form.is_valid():
            form1=form.save()
            author1=form1.author1
            title1=form1.title1
            body1=form1.body1
            image1=form1.image1
            blog_cr=Blog.objects.create(author_name=author1,body=body1,title=title1,image=image1)
            form1.save()
    else:
        form=blogform1()
    context={"form":form}
    return render(request,'template/blog.html',context)

            


