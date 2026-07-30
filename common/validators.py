from datetime import date
from rest_framework.exceptions import ValidationError

def validate_adult_from_token(request):
    token = request.auth
    if token:
        birth_date_str = token.get("birth_date")
    else:
        birth_date_str = None
    if not birth_date_str:
        raise ValidationError("Укажите дату рождения, чтобы создать продукт.")
    birth_date = date.fromisoformat(birth_date_str)
    today = date.today()
    age = today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )
    if age < 18:
        raise ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")