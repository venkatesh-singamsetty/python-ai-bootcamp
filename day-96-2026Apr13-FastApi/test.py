from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def hello_world():
    return {"message": "Hello World"}

@app.get("/prakash_senapati")
def prakash_senapati():
      return {"message": "This is a FastAPI application created by prakash senapati."}
