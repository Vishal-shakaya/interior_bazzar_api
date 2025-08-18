from ast import Try
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES
from app_ib.Utils.LocalResponse import LocalResponse
from app_ib.Controllers.Auth.Tasks.AuthTasks import AUTH_TASK
from app_ib.Controllers.Auth.Validators.AuthValidators import AUTH_VALIDATOR


class AUTH_CONTROLLER:
    
    @classmethod 
    async def SignupUser(self, data):
        try:
            response_data = {}

            # Validate Password
            validate_password = await AUTH_VALIDATOR._validate_password(password=data.password)
            print(f'validate_password')

            if validate_password.code == RESPONSE_CODES.error:
                return LocalResponse(
                    code=RESPONSE_CODES.error,
                    response=RESPONSE_MESSAGES.error,
                    message=validate_password.message,
                    data={})

            # Check if user already exist 
            is_user_exist = await AUTH_TASK.IsUserExist(data.username)
            print(f'is user exist {is_user_exist}')
            if is_user_exist:
                return LocalResponse(
                    response=RESPONSE_MESSAGES.success,
                    message=RESPONSE_MESSAGES.user_exist,
                    code=RESPONSE_CODES.success,
                    data={})
            else:

                # Create User
                user_ins = await AUTH_TASK.CreateUser(data.username, data.password, data.type)
                print(f'Print username if user created {user_ins.username}')

                if user_ins:
                    # Generate Token and build final response data
                    response_data = await AUTH_TASK.GenerateUserToken(user_ins)
                    print(f'response data {response_data}')

                else:
                    return LocalResponse(
                        response=RESPONSE_MESSAGES.error,
                        message=RESPONSE_MESSAGES.token_generate_error,
                        code=RESPONSE_CODES.error,
                        data={})
                
                # Success Response: 
                return LocalResponse(
                    response=RESPONSE_MESSAGES.success,
                    message=RESPONSE_MESSAGES.user_register_success,
                    code=RESPONSE_CODES.success,
                    data=response_data)

        except:
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.user_register_error,
                code=RESPONSE_CODES.error,
                data={})

    @classmethod
    async def ResetPassword(self, user_ins, data):
        try:
            # Validate Password
            validate_password = await AUTH_VALIDATOR._validate_password(password=data.password)
            print(f'validate_password')
            if validate_password.code == RESPONSE_CODES.error:
                return LocalResponse(
                    code=RESPONSE_CODES.error,
                    response=RESPONSE_MESSAGES.error,
                    message=validate_password.message,
                    data={})
            
            # Reset Password
            is_password_reset = await AUTH_TASK.ResetPassword(user_ins=user_ins, data=data)
            if is_password_reset:
                return LocalResponse(
                    response=RESPONSE_MESSAGES.success,
                    message=RESPONSE_MESSAGES.password_reset_success,
                    code=RESPONSE_CODES.success,
                    data={})
            else:
                return LocalResponse(
                    response=RESPONSE_MESSAGES.error,
                    message=RESPONSE_MESSAGES.password_reset_error,
                    code=RESPONSE_CODES.error,
                    data={})

        except:
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.password_reset_error,
                code=RESPONSE_CODES.error,
                data={})

