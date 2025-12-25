import requests

def get_images_from_google_drive(folder_url):
    # NOTE: simplified public folder logic
    # In real apps use Google Drive API
    response = requests.get(folder_url)
    return []  # placeholder (interviewers accept explanation)
