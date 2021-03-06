# FastAPI Tutorial

FastAPI is a [framework](https://fastapi.tiangolo.com/) to create API quickly and robustly.

## Quickstart

1. Install with `pip install fastapi uvicorn[standard]`.
2. Create a `main.py` with:
   ```python
   from typing import Optional
   from fastapi import FastAPI
   
   app = FastAPI()
   
   @app.get("/")
   def read_root():
       return {"Hello": "World"}
   
   @app.get("/items/{item_id}")
   def read_item(item_id: int, q: Optional[str] = None):
       return {"item_id": item_id, "q": q}
   ```
3. Run with `uvicorn main:app --reload`.

## More info
* Docs are at `http://127.0.0.1:8000/docs`
* Sample query at `http://127.0.0.1:8000/items/5?q=somequery`
