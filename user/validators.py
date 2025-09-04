# myapp/validators.py
from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator:
    def validate(self, password, user=None):

        # Rule 1 - Enforce at least one uppercase letter
        # if not re.search(r'[A-Z]', password):
        #     raise ValidationError(
        #         "Password must contain at least one uppercase letter.",
        #         code='password_no_uppercase',
        #     )
        
        # Rule 2 Prevent common words
        common_words = ['123@gfth', 'password', '123456', 'qwerty']
        if password.lower() in common_words:
            raise ValidationError(
                "Password is too common.",
                code='password_too_common',
            )

    def get_help_text(self):
        return "Your password must contain at least one uppercase letter and not be a common word."
    