from random import choice
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
    return render(request, 'generator/about.html')


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    upper_characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('1234567890')
    special_characters = list('!"#$%&/()=?¡@*¨[:;_]-.,+¿|<>`~^')
    pass_lenght = int(request.GET.get('length'))
    is_upper = bool(request.GET.get('uppercase'))
    is_special = bool(request.GET.get('special'))
    is_numbers = bool(request.GET.get('numbers'))

    if is_upper:
        characters.extend(upper_characters)
    if is_special:
        characters.extend(special_characters)
    if is_numbers:
        characters.extend(numbers)

    generated_password = ''
    
    validations = is_numbers + is_special + is_upper
    validated = 0
    is_invalid_password = True
    while is_invalid_password:
        
        for char in range(pass_lenght):
            generated_password += choice(characters)
        print(generated_password)
        if validations == 0:
            break

        if is_upper:
            for i in upper_characters:
                if not i in list(generated_password):
                    is_invalid_password = True
                else:
                    validated += 1
                    break

        if is_special:
            for i in special_characters:
                if not i in list(generated_password):
                    is_invalid_password = True
                else:
                    validated += 1
                    break

        if is_numbers:
            for i in numbers:
                if not i in list(generated_password):
                    is_invalid_password = True
                else:
                    validated += 1
                    break
        
        
        if validations == validated:
            is_invalid_password = False
            break
        if is_invalid_password == True:
            generated_password = ''
            validated = 0
        


    return render(request, 'generator/password.html', {'password': generated_password})
