
from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect , get_object_or_404
from cours.models import cours , categories
from cours.forms import CreateBlogPostForm
from account.models import Account
from operator import attrgetter
from django.db.models import Q









def create_cours_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=request.user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()

    cat = categories.objects.all()
    context['form'] = form
    context['cat'] = cat

    return render(request, 'cours/create.html', context)
def detail_cours_view(request, slug):
	
	context = {}
	cour_s = get_object_or_404(cours, slug=slug)
	context['cour_s'] = cour_s

	return render(request, 'cours/detail.html', context)

def home_screen_view(request):
	
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    cour_s = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
    context['cour_s'] = cour_s
    return render(request, "cours/cours.html", context)

def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = cours.objects.filter(
			Q(title__contains=q)|
			Q(body__icontains=q)|
			Q(category__title__icontains=q)
			).distinct()
		for post in posts:
			queryset.append(post)

	# create unique set and then convert to list
	return list(set(queryset)) 