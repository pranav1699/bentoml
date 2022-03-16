import numpy as np
import bentoml
from bentoml.io import NumpyNdarray


iris_clf_runner = bentoml.sklearn.load_runner("diabetes_model:latest")

svc = bentoml.Service("diabetes_prediction", runners=[iris_clf_runner])


@svc.api(input = NumpyNdarray(), output= NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    return iris_clf_runner.run(input_series)