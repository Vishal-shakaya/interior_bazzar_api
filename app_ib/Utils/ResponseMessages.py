class RESPONSE_MESSAGES:
    success= True
    warning= False
    error= False

    default_success= 'success'
    default_warning= 'warning'
    default_error= 'error'

    update_success= 'Updated successfully'
    input_error= 'Unable to read input'
    validate_error = 'Unable to validate input'

    user_profile_create_success="User profile created successfully" 
    user_profile_create_error="User profile create error"
    user_profile_update_success="User profile updated successfully"
    user_profile_update_error="User profile update error"
    user_profile_fetch_success="User profile fetched successfully"
    user_profile_fetch_error="User profile fetch error"
    user_profile_delete_success="User profile deleted successfully"
    user_profile_delete_error="User profile delete error"



    # AUTH
    user_exist= 'User already exist'
    user_not_exist= 'User not exist'
    user_register_success= 'Register successfully'
    user_register_error= 'Unable to register'
    token_generate_error = "Unable to generate token"
    token_generate_success = "Token generated successfully"
    user_login_success= 'Login successfully'
    user_login_error= 'Unable to login'
    user_logout_success= 'Logout successfully'
    user_logout_error= 'Unable to logout'
    
    user_remove_error= 'Unable to remove user'
    user_removed_success= 'User removed successfully'

    invalid_mail= 'Invalid mail address'
    invalid_password= 'Invalid password'

    generate_link_error = 'Unable to generate link'
    generate_link_success = 'link generated successfully'

    send_link_success = 'Link sent successfully'
    send_link_error= 'Unable to send link'
    link_expired_error= 'Link expired'


    password_reset_success= 'Password reset successfully'
    password_reset_error= 'Unable to reset password'
    user_removed_success= 'User removed successfully'
    password_not_match= 'Password does not match'




    ############################################
    #Business
    ############################################
    business_register_success= 'Business registered successfully'
    business_register_error= 'Unable to register business'
    business_update_success = 'Update successfully'
    business_update_error = 'Unable to update business'

    business_fetch_error= 'Unable to fetch business detail'
    business_fetch_success= 'Business detail fetched'
    business_already_exist = "Business already exist"


    ############################################
    #Query
    ############################################
    query_generate_error= 'Unable to generate query'
    query_generate_success= 'Query generated successfully'

    query_remove_error= 'Unable to remove query'
    query_remove_success= 'Query deleted successfully'

    query_fetch_error= 'Unable to fetch query'
    query_fetch_success= 'Query fetch successfully'

    query_assign_errror= 'Unable to assign query'
    query_assign_success= 'Query assigned successfully'

class VALIDATION_MESSAGES:
    password_length= 'Password must be at least 8 characters long'
    password_must_contain_digit= 'Password must contain at least one digit'
    password_must_contain_letter= 'Password must contain at least one letter'

