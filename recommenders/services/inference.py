import onnxruntime as ort

class InferenceService:
    def __init__(self, model_path: str):
        self.session = ort.InferenceSession(model_path)

    async def run_inference(self, input_data: dict) -> dict:
        inputs = {k: v for k, v in input_data.items()}
        outputs = await self.session.run(None, inputs)
        return {f'output_{i}': output for i, output in enumerate(outputs)}