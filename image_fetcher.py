import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # 🌍 Hardcoded image URL
    url = "https://images.pexels.com/photos/13397143/pexels-photo-13397143.jpeg"

    # 🏠 Create a directory for storing fetched images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # 🌐 Fetch the image from the internet
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 🚦 Raise HTTPError if response status is not 200

        # 🧾 Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename in URL, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Full save path
        file_path = os.path.join(save_dir, filename)

        # 💾 Save the image in binary mode
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"✅ Image successfully saved as: {file_path}")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"❌ Error fetching the image: {req_err}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    fetch_image()
