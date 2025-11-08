from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError, ProgrammingError

class NalecosmeticConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Nalecosmetic'

    def ready(self):
        try:
            User = get_user_model()
            username = "Kavin"
            email = "nalehcosmetics@example.com"
            password = "Naleh@123"

            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username, email, password)
                print(f"✅ Superuser created: {username} / {password}")
        except (OperationalError, ProgrammingError):
            # Database may not be ready during migration phase
            pass
