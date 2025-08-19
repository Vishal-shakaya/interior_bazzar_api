from ast import Try
import time
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES
from app_ib.Utils.LocalResponse import LocalResponse
from app_ib.Controllers.Auth.Tasks.AuthTasks import AUTH_TASK
from app_ib.Controllers.Auth.Validators.AuthValidators import AUTH_VALIDATOR
from app_ib.Utils.MyMethods import MY_METHODS


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
    async def LoginUser(self, data):
        try:
            # Validate Password
            validate_password = await AUTH_VALIDATOR._validate_password(password=data.password)
            print(f'validate_password')

            # Login User
            login_user = await AUTH_TASK.LoginUser(data.username, data.password)
            print(f'login_user {login_user}')

            if login_user:
                # Generate Token and build final response data
                response_data = await AUTH_TASK.GenerateUserToken(login_user)
                print(f'response data {response_data}')
                return LocalResponse(
                    response=RESPONSE_MESSAGES.success,
                    message=RESPONSE_MESSAGES.user_login_success,
                    code=RESPONSE_CODES.success,
                    data=response_data)

            else:
                return LocalResponse(
                    response=RESPONSE_MESSAGES.error,
                    message=RESPONSE_MESSAGES.user_login_error,
                    code=RESPONSE_CODES.error,
                    data={})
        except:
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.user_login_error,
                code=RESPONSE_CODES.error,
                data={})

    @classmethod
    async def LogoutUser(self, user_ins):
        try:
            logout_user = await AUTH_TASK.LogoutUser(user_ins)
            print(f'logout_user {logout_user}')
            if logout_user:
                return LocalResponse(
                    response=RESPONSE_MESSAGES.success,
                    message=RESPONSE_MESSAGES.user_logout_success,
                    code=RESPONSE_CODES.success,
                    data={})
        except:
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.user_logout_error,
                code=RESPONSE_CODES.error,
                data={})

    @classmethod
    async def DeleteUser(self, user_ins):
        try:
            delete_user = await AUTH_TASK.DeleteUser(user_ins)
            print(f'delete_user {delete_user}')
            if delete_user:
                return LocalResponse(
                    response=RESPONSE_MESSAGES.success,
                    message=RESPONSE_MESSAGES.user_removed_success,
                    code=RESPONSE_CODES.success,
                    data={})
        except:
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.user_remove_error,
                code=RESPONSE_CODES.error,
                data={})

    @classmethod
    async def GenerateAndSendForgotPasswordLink(self, data):
        try:
            # Check if user exist
            is_user_exist = await AUTH_TASK.IsUserExist(username=data.username)
            print(f'is user exist {is_user_exist}')
            
            timestamp= MY_METHODS.GetCurrentTimeinStr()

            if is_user_exist:
                # Generate and send forgot password link
                link= await AUTH_TASK.GenerateForgotPasswordLink(username=data.username,timestamp=timestamp)
                if(link):
                    print(f'link {link}')

                    # Send Email
                    # is_link_send= await AUTH_TASK.SendEmailForgotPasswordLink(username=data.username,link=link)
                    # if(is_link_send):
                    #     return LocalResponse(
                    #         response=RESPONSE_MESSAGES.success,
                    #         message=RESPONSE_MESSAGES.send_link_success,
                    #         code=RESPONSE_CODES.success,
                    #         data={})
                    # else:
                    #     return LocalResponse(
                    #         response=RESPONSE_MESSAGES.error,
                    #         message=RESPONSE_MESSAGES.send_link_error,
                    #         code=RESPONSE_CODES.error,
                    #         data={})

                else:
                    return LocalResponse(
                        response=RESPONSE_MESSAGES.error,
                        message=RESPONSE_MESSAGES.generate_link_error,
                        code=RESPONSE_CODES.error,
                        data={})

            if not is_user_exist:
                return LocalResponse(
                    response=RESPONSE_MESSAGES.error,
                    message=RESPONSE_MESSAGES.user_not_exist,
                    code=RESPONSE_CODES.error,
                    data={})



            return LocalResponse(
                response=RESPONSE_MESSAGES.success,
                message=RESPONSE_MESSAGES.send_link_success,
                code=RESPONSE_CODES.success,
                data={})
        except:
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.send_link_error,
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