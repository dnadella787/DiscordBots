

class member:
    def __init__(self, name):
        self.name = name
        self.points = 250 


member_list = []

member_list.append(member("dman"))
member_list.append(member("andyseaweed007"))

user = "Jonathon"
message = f'{user} was added to point list. The new point list: \n - ' + '\n - '.join([f'{memb.name}: {memb.points}' for memb in member_list])

print(message)
