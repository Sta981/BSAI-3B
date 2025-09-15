# Requirements : Set According To Fixed Temprature
# Input : Room Temprature
# Output : Print -> Turn ON Turn OFF
class ModelReflexAgent():
    def __init__(self, temp):
        self.fixed_temp = temp
        self.last_action = None


    def sensor(self, temp):
        self.room_temp = temp

    def performance(self):
        action = None
        if self.room_temp > self.fixed_temp:
            action = "Turn On AC"
        elif self.room_temp <= self.fixed_temp:
            action = "Turn Of AC"

        if action == self.last_action:
            print("No Change")
        else:
            self.last_action = action
            
        return action
            

    def actuator(self):
         action = self.performance()
         print("Temp:", self.room_temp,  "Action:", action)

agent = ModelReflexAgent(16) # Fixed Temprature
rooms = {
    "Living Room" : 26,
    "Bedroom" : 16,
    "KItchen" : 25,
    "Drawing Room" : 16
}

for room in rooms:
    temp = rooms[room]
    agent.sensor(temp)
    print(room, ":", end="")
    agent.actuator()


# agent.sensor(23) # Romm Temprature
# agent.actuator()