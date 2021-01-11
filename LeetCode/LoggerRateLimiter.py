class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.messages = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        
        if message not in self.messages:
            self.messages[message] = timestamp
            return True
        else:
            if timestamp - self.messages[message] < 10:
                return False
            else:
                self.messages[message] = timestamp
                return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

#TODO
#reduce space complexity - does it need to store all of the messages and their time stamps?
#reduce time complexity 
#perhaps store only the messages printed within the last 10 seconds?
#if it has been more than 10 seconds since the last message was printed, then we don't even need to consider any other messages
