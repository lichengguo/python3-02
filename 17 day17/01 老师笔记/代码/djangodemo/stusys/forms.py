from django import forms
from users.models import Student
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude = ("is_delete", )