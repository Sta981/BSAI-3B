# Requirements : Set According To Fixed Temprature
# Input : Room Temprature
# Output : Print -> Turn ON Turn OFF
class ModelReflexAgent():
    def __init__(self, temp):
        self.fixed_temp = temp
        self.last_action = {}


    def sensor(self,room, temp):
        self.current_room = room 
        self.room_temp = temp

    def performance(self):
        action = None
        if self.room_temp > self.fixed_temp:
            action = "Turn On AC"
        elif self.room_temp <= self.fixed_temp:
            action = "Turn Of AC"
        
        last_action = self.last_action.get(self.current_room)

        if action == last_action:
            print("No Change")
        else:
            self.last_action[self.current_room] = action
            return action
            

    def actuator(self):
         action = self.performance()
         print("Temp:", self.room_temp,  "Action:", action)

agent = ModelReflexAgent(16) # Fixed Temprature
places = [
    ("Living Room" ,26),
    ("Bedroom" , 26),
    ("KItchen" , 25),
    ("Living Room" , 26),
    ("Drawing Room" ,16),
]

for room,temp in places:
    agent.sensor(room,temp)
    print(room, ":", end="")
    agent.actuator()
