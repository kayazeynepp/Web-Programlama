from django.http import HttpResponse

def getTheme(request):
    theme='day'
    if 'theme' in request.COOKIES:
        theme = request.COOKIES['theme']
    else:
        theme = 'day'
    return theme

def toggle_theme(request):
    if request.method == 'POST':
        current_theme = request.COOKIES.get('theme', 'day')
        new_theme = 'night' if current_theme == 'day' else 'day'
        response = HttpResponse("Theme toggled!")
        response.set_cookie('theme', new_theme)
        return response
