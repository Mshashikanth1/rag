from tensorflow.keras.applications import EfficientNetB0  # Replace with your chosen model
from tensorflow.keras.preprocessing import image

model = EfficientNetB0(weights='imagenet', include_top=False)  # Load pre-trained model (modify for others)

import torch
from torchvision import models

model = models.resnet50(pretrained=True)  # Replace with your chosen model
model.eval()  # Set to evaluation mode

# Assuming pre-processing is done
predictions = model.predict(image_array)


def is_nsfw(image_path):
    # Load image, pre-process, and get predictions
    image_array = pre_process_image(image_path)
    predictions = model.predict(image_array[None])

    # Extract NSFW probability and apply threshold
    nsfw_probability = predictions[0][nsfw_class_index]  # Assuming you know the NSFW class index
    is_nsfw = nsfw_probability > threshold

    return is_nsfw


image_path = "path/to/your/image.jpg"
if is_nsfw(image_path):
    print("Image is likely NSFW")
else:
    print("Image is likely SFW")
