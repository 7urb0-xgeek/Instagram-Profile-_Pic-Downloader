# download_instagram_profile_pic.py

import instaloader

def download_profile_picture(username):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Download profile picture of the given username
    try:
        loader.download_profile(username, profile_pic_only=True)
        print(f"Profile picture of {username} has been downloaded.")
    except instaloader.exceptionn:
        print(f"The profile {username} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    username = input("Enter the Instagram username: ")
    download_profile_picture(username)
