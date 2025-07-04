import logging

from response_data import ResponseData
from register_user_dto import RegisterUserDto
from validator_login import LoginValidator
from validator_first_name import FirstNameValidator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserService:

    def register_user(self, register_user_dto: RegisterUserDto) -> ResponseData:
        logger.info(f"Rejestracja użytkownika: {register_user_dto.__dict__}") # logowanie DTO

        validators = [
            LoginValidator(register_user_dto.login),
            FirstNameValidator(register_user_dto.firstName)
            # TODO: Dodaj pozostale walidatory tutaj...
        ]

        invalid_field_names = [
            validator.field_name()
            for validator in validators
            if not validator.is_valid()
        ]

        response_data = ResponseData()
        response_data.add_invalid_field_names(invalid_field_names)

        return response_data
