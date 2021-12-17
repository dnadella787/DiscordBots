user_to_ping = {}

def ping_me(original_user, user_name):
    user_to_ping.setdefault(user_name, []).append(original_user)

ping_me("john", "bob")
ping_me("amy", "bob")

print(user_to_ping)