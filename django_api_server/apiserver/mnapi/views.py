from rest_framework.decorators import api_view
from rest_framework.response import Response
from PIL import Image, ImageOps
from django.apps import apps
import numpy as np


@api_view(['POST'])
def predict(request):

    if 'image' not in request.FILES:
        return Response({'error': 'No image uploaded'}, status=400)
    
    try:
        image = request.FILES['image']
        image = Image.open(image).convert('RGBA')
        background = Image.new('RGBA', image.size, (0, 0, 0, 255))
        image_with_background = Image.alpha_composite(background, image).convert('L')
        img = image_with_background.resize((28, 28))
        img = ImageOps.invert(img)
        img = np.array(img).reshape(1, -1)
        scaler = apps.get_app_config('apiserver').scaler
        model = apps.get_app_config('apiserver').model
        img = scaler.transform(img)
        pred = model.predict(img)[0]
        return Response({'prediction': int(pred)}, status=200)
    except Exception as e:
        return Response({'error': 'There is an error', 'details': str(e)}, status=500)
