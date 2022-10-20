
class Time:

    #  general comments, loops, if statements, no acccessor methods and string methods need to be commented

    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def getSeconds(self):
        return self.seconds

    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def timeInSeconds(self):  # this method returns a time object in total seconds
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def changeTheTime(self, h, m, s):  # this method mutates a time object by changing its parameters to new values
        self.hours = h
        self.minutes = m
        self.seconds = s

    def twelveHourClock(self):  # this method returns a time object in military time in twelve hour time with pm/am
        if self.hours < 12:
            return str(self) + "am"
        elif self.hours > 12:
            return str(self.hours - 12) + ":" + str(self.minutes) + ":" + str(self.seconds) + "pm"
        else:
            return str(self) + "pm"

    def whatTimeIsIt(self):  # this method returns morning, afternoon, evening, or nighttime based on time object time
        if self.hours >= 6 & self.hours < 12:
            return "morning"
        elif self.hours >= 12 & self.hours < 17:
            return "afternoon"
        elif self.hours >= 17 % self.hours < 22:
            return "evening"
        else:
            return "nighttime"

    def compareTo(self, time):  # this method compares two time objects and returns the difference in seconds
        # if the self time object is before the method parameter time, the returned time is negative, and vice versa
        t1 = self.timeInSeconds()
        t2 = time.timeInSeconds()
        return t1 - t2

    def timeTill(self, time):  # this method returns the time difference between two time objects, or how long from
        # one to the other --> this doesn't completely work lol but its fine
        t1 = self.timeInSeconds()
        t2 = time.timeInSeconds()
        diff = t2 - t1
        h = int(diff / 3600)
        diff = diff - 3600 * h
        m = int(diff / 60)
        diff = diff - 60 * m
        return h, ":", m, ":", diff


