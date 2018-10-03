from django.contrib.auth import get_user_model


User = get_user_model()


def invite_user(email):
    # cleanup email
    email = email.lower()
    email = email.strip()

    user = None

    try:
        user = User.objects.get(
            email__iexact=email)
    except User.DoesNotExist:
        if '@' in email:
            user = User.objects.create_user(
                username=email,
                email=email)

    return user
