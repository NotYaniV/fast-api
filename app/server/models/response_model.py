class ResponseModel(object):
    def __init__(self,data,message) -> None:
        self.data = data
        self.code = 200
        self.message = message

    def __repr__(self):
        return {
            "data": [self.data],
            "code": self.code,
            "message": self.message,
        }