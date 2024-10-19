from django.shortcuts import render
import joblib
import numpy as np
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Load the trained model
model = joblib.load('random_forest_model.pkl')

@api_view(['POST'])
def predict_default(request):
    """
    This view handles prediction requests for credit default risk.
    """
    try:
        # Example input: {"data": [[feature1, feature2, ..., featureN]]}
        input_data = request.data['data']
        
        # Convert input data into NumPy array for the model
        input_array = np.array(input_data)

        # Make predictions using the loaded model
        prediction = model.predict(input_array)
        
        # Return the prediction
        return Response({'prediction': prediction.tolist()})
    except Exception as e:
        return Response({'error': str(e)}, status=400)


