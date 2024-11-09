from django.shortcuts import render

# Define view for homepage
def home(request):
    return render(request, 'profile.html')

# Define view for contact page
def contact(request):
    return render(request, 'contact.html')
