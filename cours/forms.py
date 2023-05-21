from django import forms

from cours.models import cours


class CreateBlogPostForm(forms.ModelForm):

	class Meta:
		model = cours
		fields = ['title', 'body', 'image']