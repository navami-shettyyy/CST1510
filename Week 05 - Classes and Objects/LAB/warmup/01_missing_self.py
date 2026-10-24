# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

# TypeError: Record.status() takes 1 positional argument but 2 were given
# class Record:
#    def status(percent):    # this parameter should be self
#        return percent

# Fixed
class Record:
    def status(self,percent):
        return percent
    
r = Record()
print(r.status(95))
