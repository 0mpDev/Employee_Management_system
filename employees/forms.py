# from django import forms
# from .models import Employee

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = '__all__'
#         widgets = {
#             'hire_date': forms.DateInput(attrs={'type': 'date'}),
#             'salary': forms.NumberInput(attrs={'step': '1000'}),
#         }
        
#         labels = {
#             'first_name': 'First Name',
#             'last_name': 'Last Name',
#             'email': 'Email Address',
#             'department': 'Department',
#             'position': 'Job Position',
#             'salary': 'Monthly Salary',
#             'hire_date': 'Date Hired'
#         }
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    full_name = forms.CharField(
        label='Full Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. John Doe'})
    )

    class Meta:
        model = Employee
        fields = ['full_name', 'email', 'department', 'position', 'salary', 'hire_date']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
            'salary': forms.NumberInput(attrs={'step': '1000'}),
        }
        labels = {
            'email': 'Email Address',
            'department': 'Department',
            'position': 'Job Position',
            'salary': 'Monthly Salary',
            'hire_date': 'Date Hired'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-fill full_name if editing
        if self.instance and self.instance.pk:
            self.fields['full_name'].initial = f"{self.instance.first_name} {self.instance.last_name}"

    def save(self, commit=True):
        instance = super().save(commit=False)
        full_name = self.cleaned_data.get('full_name', '').strip()
        names = full_name.split(" ", 1)
        instance.first_name = names[0]
        instance.last_name = names[1] if len(names) > 1 else ''
        if commit:
            instance.save()
        return instance
