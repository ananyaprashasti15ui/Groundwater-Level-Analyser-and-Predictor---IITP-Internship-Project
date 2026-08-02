"""
Prediction script for evaluating groundwater level predictor models.
"""

import os
import joblib


def make_predictions(model_path: str, input_data):
    """Load model and return groundwater predictions."""
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    model = joblib.load(model_path)
    return model.predict(input_data)


if __name__ == "__main__":
    print("Prediction module initialized.")
