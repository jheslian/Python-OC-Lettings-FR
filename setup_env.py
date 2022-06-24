from django.core.management.utils import get_random_secret_key

with open(".env", "w") as f:
    f.write(f"export SECRET_KEY={get_random_secret_key()}\n")
    f.close()
