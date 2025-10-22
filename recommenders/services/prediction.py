from inference import InferenceService
import numpy as np

inference_model_path = "path/to/your/model.onnx"
model = InferenceService(inference_model_path)


async def run_prediction() -> dict:
    input_data = {
        model.session.get_inputs()[0].name: np.random.rand(1, 100).astype(np.float32), # Placeholder input data
        model.session.get_inputs()[1].name: np.random.rand(1, 50).astype(np.float32), # Placeholder input data
    }

    predictions = await model.run_inference(input_data)
    return predictions