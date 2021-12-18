class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """
    print("OK")
    
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")