import Module.logger

class UserDefinedException(Exception):
    def raiseException(self, message):
        self.message = message
        Module.logger.ERROR(message)
        raise UserDefinedException(message)
