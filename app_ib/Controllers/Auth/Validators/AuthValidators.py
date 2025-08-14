from app_ib.Utils.LocalResponse import LocalResponse
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES


class AUTH_VALIDATOR: 
    @classmethod
    async def _validate_password(self,password):
        try:
            msg = ""
            if len(password) < 8:
                msg = 'Password must be at least 8 characters long'
                raise ValueError("Password must be at least 8 characters long")
            if not any(char.isdigit() for char in password):
                msg = 'Password must contain at least one digit'
                raise ValueError("Password must contain at least one digit")
            if not any(char.isalpha() for char in password):
                msg = 'Password must contain at least one letter'
                raise ValueError("Password must contain at least one letter")
            return LocalResponse(
                code=RESPONSE_CODES.success,
                response=RESPONSE_MESSAGES.success,
                message=RESPONSE_MESSAGES.default_success,
                data={}
            )
        except ValueError as e:
            return LocalResponse(
                code=RESPONSE_CODES.error,
                response=RESPONSE_MESSAGES.error,
                data=str(e),
                message=msg
            )

