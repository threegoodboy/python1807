from django.contrib.auth.hashers import make_password, check_password


password=make_password('123')
print(password)
password=check_password(password)
print(password)