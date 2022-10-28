class DataIsNotValidException(Exception):
    def __init__(self, message='--Failed-- this action failed because some of the data is not vaild.'):
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return '--Failed-- this action failed because some of the data is not vaild.'