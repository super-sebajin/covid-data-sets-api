class DatabaseException(Exception):
    pass

class ApiException(Exception):
    pass

class InvalidCredentialsError(ApiException):
    """Invalid username or password"""
    pass

