from django import forms

class GradeForm(forms.ModelForm):
     
    def clean(self):
        user = self.request.user
        cleaned_data = super().clean()
        if user.is_superuser:
            return
        if cleaned_data.get('subject').teacher != user:
            raise forms.ValidationError('You dont have rights to do this.')
        print('ole')

