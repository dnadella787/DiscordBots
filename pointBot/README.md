This is a python bot that keeps track of users points and allows you to add/remove users by their usernames and also roles. 

To setup you must add a '.env' file in the same folder as pointbot.py and its contents should be:

    DISCORD_TOKEN={your discord bot token}
    DISCORD_GUILD={your discord guild}

Tweak the roles as needed in the code. For example, if the only people you want to be able to add/remove people or increase/decrease points are people with the role 'Student' and 'Professor' then change 'role1' and 'role2' in the code to be 'Student' and 'Professor' at the start of each command in @command.has_any_role(..)

It has the following commands:

    !start - sets up the text channel 'point-bot' which is where all other commands must go
    
    !add [user_name] - adds the user to the point list, every user starts off with 250 points, also prints out the current point list in descending order

    !add-role [role_name] - adds all users with the role 'role_name' to the point list, again all start off with 250 points and prints out the current point list in descending order

    !remove [user_name] - removes the user from the point list, also prints out the current point list in descending order

    !remove-all - empties the point list

    !increase [user_name] [num of points] - increase a specific user's points by a certain amount, only takes positive integers

    !decrease [user_name] [num of points] - decrease a specific user's points by a certain amount, only takes positive integers

    !print-points - prints out a list of all the point list members and their point number in descending order