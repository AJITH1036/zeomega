from enum import Enum

class Status(Enum) :
    NO_STATUS = -1
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2


print(Status.IN_PROGRESS.name)
print(Status.IN_PROGRESS.value)
   