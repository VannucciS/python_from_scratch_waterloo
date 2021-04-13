'''
Instructions
Now add a method elapsed such that one.elapsed(two) returns the number of minutes that have passed between one and two, where two is a time later in the day.

Hint:
Make sure to handle the case in which one.minute is greater than two.minute.
'''

class Time:
    """Time stored as hour and minutes

       Methods:
       __init__: initializes a new object
       __str__: prints an object
       earlier_time: returns earlier time

       Attributes:
       hour: int, 0 <= value < 24
       minute: int, 0 <= value < 60
    """

    def __init__(self, hour, minute):
        """Initializes a new object.

           Preconditions:
           hour: int, 0 <= value < 24
           minute: int, 0 <= value < 60

           Parameters:
           hour: hour in time
           minute: minutes in time

           Side effect: attributes set with values
        """
        self.hour = hour
        self.minute = minute
 
    def __str__(self):
        """Prints time.

           Side effect: prints 
        """

        if self.minute < 10:
            min_word = "0" + str(self.minute)
        else:
            min_word = str(self.minute)
        return str(self.hour) + ":" + \
            min_word

    def earlier_time(self, other):
        """Determines earlier of two Times.

           Preconditions:
           other: Time object

           Parameters:
           other: Time compared to self

           Returns: earlier of two times, 
           or other if equal 
        """

        if self.hour < other.hour:
            return self
        elif other.hour < self.hour:
            return other
        elif self.minute < other.minute:
            return self
        else:
            return other

    def safe(self):
        if type(self.hour)!= type(1) or type(self.minute)!= type(1):
            print('Incorrect type')
        elif self.hour < 0 or self.hour > 24:
            print('Hour out of range')
        elif self.minute < 0 or self.minute > 59:
            print('Minute out of range')
        else:
            print('Safe')

    def elapsed(self, other):
        return ((other.hour * 60) + other.minute) - ((self.hour * 60) + self.minute)
        
        
       

one = Time(1,11)           
two = Time(1,22)

print(one.elapsed(two))
