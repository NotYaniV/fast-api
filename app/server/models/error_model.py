class ErrorResponseModel(object):
    def __init__(self, error, code, message) -> None:
        self.error = error
        self.code = code
        self.message = message
        
    def __repr__(self):
        return {"error": self.error, "code": self.code, "message": self.message}