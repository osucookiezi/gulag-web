# -*- coding: utf-8 -*-

# app name
app_name = 'Cookiezi (BETA)'

# secret key
secret_key = 'changeme'

# domain (used for api, avatar, etc)
domain = 'cookiezi.gay'

# mysql credentials
mysql = {
    'db': 'gulag',
    'host': 'localhost',
    'user': 'server',
    'password': 'changeme',
}

# path to gulag root (must have leading and following slash)
path_to_gulag = 'changeme'

# enable debug (disable when in production to improve performance)
debug = False

# disallowed names (hardcoded banned usernames)
disallowed_names = {
    'matty', 'rrtyui',
    'hvick225', 'qsc20010'
}

# disallowed passwords (hardcoded banned passwords)
disallowed_passwords = {
    'password', 'minilamp'
}

# enable registration
registration = True

# social links (used throughout gulag-web)
github = 'https://github.com/Yo-ru/gulag-web'
discord_server = 'https://discord.com/invite/Y5uPvcNpD9'
youtube = 'https://www.youtube.com/channel/UC6_kBICWejtDc1U6fn9ZLiQ'
twitter = 'https://twitter.com/mattylive_'
instagram = 'https://instagram.com/'
