
from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect , get_object_or_404
from cours.models import cours
from cours.forms import CreateBlogPostForm
from account.models import Account
from operator import attrgetter


def cours(request):
    return render(request, 'cours/cours.html')






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

	context['form'] = form

	return render(request, 'cours/create.html', context)


def detail_cours_view(request, slug):
	
	context = {}
	cour_s = get_object_or_404(cours, slug=slug)
	context['cour_s'] = cour_s

	return render(request, 'cours/detail.html', context)

def home_screen_view(request):
	
    context = {}
    cour_s = sorted(cours.objects.all(), key=attrgetter('date_updated'), reverse=True)
    context['cour_s'] = cour_s
    return render(request, "cours/cours.html", context)