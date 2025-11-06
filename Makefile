run:
uvicorn app.interfaces.api.main:app --reload --host 0.0.0.0 --port 8080


test:
pytest -q