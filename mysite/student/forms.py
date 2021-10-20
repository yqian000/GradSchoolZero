from django import forms


class RateClassForm(forms.Form):
    course = forms.CharField(label = "Select a course: ", required = True)
    star = forms.IntegerField(label =" Assign Stars (1 worst to 5 best): ", required = True)
    review = forms.CharField(widget = forms.Textarea, required = True)

class FileComplaintForm(forms.Form):
    name = forms.CharField(max_length = 60, required = True)
    reason = forms.CharField(widget = forms.Textarea, required = True)