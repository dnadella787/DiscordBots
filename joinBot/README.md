This bot allows members of your server to get a DM when specified members of your server enter a voice channel. So if I wanted to know whenever the user 'bob44' joined a voice channel, I would receive a DM from joinBot telling me whenever 'bob44' joined a voice channel in my discord server.

To setup you must add a '.env' file in the same folder as joinBot.py and its contents should be:

    DISCORD_TOKEN={your discord bot token}
    DISCORD_GUILD={your discord guild}

Tweak the roles as needed in the code. For example, if the only people you want to be able to add/remove people or increase/decrease points are people with the role 'Student' and 'Professor' then change 'role1' and 'role2' in the code to be 'Student' and 'Professor' at the start of each command in @command.has_any_role(..)


The bot has commands:

    !start - creates the join-bot text channel in which all other commands must be specified

    !ping-me [user_name] - this specifies to the bot that whenever 'user_name' enters a voice channel, it should send a DM to the person that used this command. (bot will not allow duplicates or yourself)
