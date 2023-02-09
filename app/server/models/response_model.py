class ResponseModel(object):
    def __init__(self,data,message) -> None:
        self.data = data
        self.message = message

    def __repr__(self):
        return {
            "data": [self.data],
            "code": 200,
            "message": self.message,
        }