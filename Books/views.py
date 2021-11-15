from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .forms import BooksForm, NewUserForm
from .models import Books

# Create your views here.


def index(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("homepage")
    else:
        form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


def books_create_view(request):
    if request.user.is_authenticated:
        form = BooksForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("homepage")

    context = {
        "form": form
    }
    return render(request, "book_create.html", context)


def books_detail_view(request, id):
    book = get_object_or_404(Books, id=id)
    return render(request, 'book_detail.html', locals())


def books_update_view(request, id):
    if not request.user.is_authenticated:
        return redirect("homepage")
    a = Books.objects.get(id=id)
    form = BooksForm(instance=a)
    if request.method == "POST":
        form = BooksForm(data=request.POST, files=request.FILES, instance=a)
        if form.is_valid():
            a = form.save(commit=False)
            a.save()
            return redirect("homepage")
    return render(request, 'book_create.html', locals())


def books_delete_view(request, id):
    if not request.user.is_authenticated:
        return redirect("homepage")
    a = get_object_or_404(Books, id=id)
    a.delete()
    print("Deleted Successfully")
    return redirect("homepage")


def list_all(request):
    a = Books.objects.all()
    return render(request, "home.html", locals())


def logout_view(request):
    logout(request)
    return redirect(index)
