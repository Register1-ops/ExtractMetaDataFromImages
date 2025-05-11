from PIL import Image # type: ignore
from PIL.ExifTags import TAGS # type: ignore

def extract_metadata(image_path):
    img = Image.open(image_path)
    exif_data = img._getexif()  # Extract EXIF data
    
    if exif_data is None:
        return "No EXIF data found."
    
    metadata = {}
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        metadata[tag_name] = value
    
    return metadata

image_path = 'IMG_9452.PNG'
metadata = extract_metadata(image_path)
print(metadata)
