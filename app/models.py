from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def get_photo_url(self):
        if self.socialaccount_set.filter(provider='google'):
            return self.socialaccount_set.filter(provider='google')[0].extra_data['picture']
        else:
            return False
    
    def get_name(self):
        if self.socialaccount_set.filter(provider='google'):
            return self.socialaccount_set.filter(provider='google')[0].extra_data['name']
        else:
            return False

    def get_email(self):
        if self.socialaccount_set.filter(provider='google'):
            return self.socialaccount_set.filter(provider='google')[0].extra_data['email']
        else:
            return False
        
    pass