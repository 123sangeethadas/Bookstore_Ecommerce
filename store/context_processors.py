
from .models import Category

def cateogory(request):
    return({
        'categories' : Category.objects.all()}
    )