from django.contrib.auth import get_user_model
from django.db.utils import OperationalError, ProgrammingError

def run():
    try:
        User = get_user_model()
        username = "Kavin"
        email = "nalehcosmetics@gmail.com"
        password = "Kavin@123"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            print(f"✅ Superuser created: {username} / {password}")
        else:
            print("ℹ️ Superuser already exists — skipping.")
    except (OperationalError, ProgrammingError) as e:
        print(f"⚠️ Database not ready: {e}")
