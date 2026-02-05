import os
import runpy
from joblib import load


def test_model_saved_and_loadable():
    """Run the training script and verify `outputs/model.joblib` is created and loadable."""
    model_path = os.path.join("outputs", "model.joblib")

    # Ensure a clean start
    if os.path.exists(model_path):
        os.remove(model_path)

    # Execute the training script (runs top-level code)
    runpy.run_path("src/train.py", run_name="__main__")

    assert os.path.exists(model_path), "Model file was not created by src/train.py"

    # Load and sanity-check the model
    model = load(model_path)
    assert hasattr(model, "predict"), "Loaded object does not look like a model"

    # Do a small prediction to ensure it works
    from sklearn.datasets import load_iris
    iris = load_iris()
    X = iris.data
    preds = model.predict(X[:5])
    assert len(preds) == 5
