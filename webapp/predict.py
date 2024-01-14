import torch
from PIL import Image
from torchvision import transforms
from net import *

def preprocess_image(image_path):
    interpolation_mode = transforms.InterpolationMode.BICUBIC
    resize_transform = transforms.Resize((50,50), interpolation=interpolation_mode)
    transform = transforms.Compose([
                                resize_transform,
                                transforms.Grayscale(num_output_channels=1),
                                transforms.ToTensor(),
                                transforms.Normalize((0.5,), (0.5,)),
                            ])
    image = Image.open(image_path)
    tensor = transform(image)
    return tensor

def predict(image_path):
    model_path = 'AIArtClassifier.pth'
    model = torch.load(model_path)
    model.eval()
    
    image = preprocess_image(image_path)
    image1 = image[None,:,:,:]
    
    probability = torch.sigmoid(model(image1))
    prediction = 1.0 if probability.item() > 0.7 else 0.0
    
    label = "ai generated" if prediction == 1 else "human made"
    probability_str = str(probability.item())
    
    return {'label': label, 'probability': probability_str}
    
    
