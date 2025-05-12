def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'vk-oauth2':
        if response.get('email'):
            user.email = response['email']
            user.save()
