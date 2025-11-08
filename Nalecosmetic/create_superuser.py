from django.contrib.auth import get_user_model
from django.db.utils import OperationalError, ProgrammingError

try:
    User = get_user_model()
    # 👇 change these values to your own username/email/password
    username = "Kavin"        # your desired username
    email = "nalehcosmetics@example.com"
    password = "Naleh@123"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"✅ Superuser created: {username} / {password}")
except (OperationalError, ProgrammingError):
    # Database might not be ready during first migration
    pass
