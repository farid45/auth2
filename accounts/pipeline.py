from .models import Profile

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'github':
        # Получаем или создаем профиль
        profile, created = Profile.objects.get_or_create(user=user)
        
        # Обновляем данные из GitHub
        if 'html_url' in response:
            profile.github_url = response.get('html_url')
            profile.save()
