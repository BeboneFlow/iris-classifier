# Copilot / AI Agent Instructions for "iris clasifier" ✅

## Quick project summary 🔧
- Small example project that trains an Iris classifier using scikit-learn.
- Key artifacts:
  - Training script: `src/train.py` (simple train + print metrics)
  - Notebook: `notebooks/iris_model.ipynb` (experimentation and plotting)
  - Trained artifact(s): `outputs/model.joblib`, `outputs/confusion_matrix.png`
  - Tests: `test/test_train.py` (currently mirrors train logic)
  - Requirements: `test/requrirements.txt` (note: file lives inside `test/` and the name is misspelled)

---

## What an AI agent should know before making changes 💡
- This repo is not a production codebase—it's learning/experiment-focused. Changes should be minimal and conservative unless asked to refactor.
- Determinism: `random_state=42` is used in the codebase. Preserve or explicitly update seeds when changing train/test splits.
- Artifacts are stored in `outputs/`. If adding model persistence, use `joblib` and write into `outputs/`.

---

## Developer workflows & concrete commands (Windows) ▶️
1. Create/activate venv (if needed):
   - `python -m venv venv`
   - `venv\Scripts\activate` (PowerShell: `venv\Scripts\Activate.ps1`)
2. Install deps:
   - `pip install -r test/requrirements.txt`
3. Run training script:
   - `python src/train.py`
4. Run the notebook:
   - `jupyter notebook notebooks/iris_model.ipynb`
5. Run tests:
   - `pytest` from repo root (ensure venv activated and deps installed)

---

## Project-specific conventions & examples 🧭
- Model persistence: the repo includes `outputs/model.joblib`, so use `joblib.dump()` / `joblib.load()` and keep artifacts in `outputs/`.
  - Example: `from joblib import dump, load; dump(model, "outputs/model.joblib")`
- Visual artifacts (plots) are stored in `outputs/` (see `outputs/confusion_matrix.png`). Commit small binary artifacts only if necessary.
- Scripts use print-based diagnostics (no logging framework). Keep this consistent unless explicitly asked to introduce logging.

---

## Known, discoverable issues (actionable targets) ⚠️
- `test/test_train.py` has a bug: `mode12` is used instead of `model2` on lines that fit predictions; this will raise NameError and fail tests. Fix: replace `mode12` → `model2`.
- `test/requrirements.txt` is correctly listing dependencies but is located in `test/` and the filename is misspelled. When adding CI or contributors' docs, mention this path.
- `src/train.py` does not save the final model by default while `outputs/model.joblib` exists (likely produced by the notebook). If you add model-saving behavior to `src/train.py`, write to `outputs/` and include a brief unit test verifying the file exists and can be loaded with `joblib`.

---

## Testing & CI guidance ✅
- Run `pytest` locally. Fix the `test_train.py` typo first.
- Tests are simple functional checks that mirror training; keep tests deterministic (use the same `random_state=42`).
- There is no CI configuration in the repository; if asked to add CI, include steps: setup Python, install `test/requrirements.txt`, run `pytest`.

---

## When making changes, include these checks in your PR 🔍
- Does training still produce deterministic results (same accuracy) with `random_state=42`?
- If adding model persistence, verify `joblib.load("outputs/model.joblib")` succeeds in a test.
- Update or add a short note in `notebooks/iris_model.ipynb` if experiment results or plots change.

---

## Useful files to review 📁
- `src/train.py` — main training script
- `notebooks/iris_model.ipynb` — exploratory notebook (produces `outputs/model.joblib` / plots)
- `test/test_train.py` — tests (contains a bug; `mode12` → `model2`)
- `test/requrirements.txt` — dependency list (install here for local dev)
- `outputs/` — trained artifacts and plots

---

If any section is unclear or you'd like me to implement the minimal fixes (test typo, add model saving to `src/train.py`, or move/fix the requirements file), tell me which change(s) you want and I can open a focused PR. 🔧