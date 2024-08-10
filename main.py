import instaloader

# Get instance
loader = instaloader.Instaloader()

# Login using the credentials
loader.login(USER, PASSWORD)

# Use Profile class to access metadata of account
profile = instaloader.Profile.from_username(loader.context,'maliha_baharS')
