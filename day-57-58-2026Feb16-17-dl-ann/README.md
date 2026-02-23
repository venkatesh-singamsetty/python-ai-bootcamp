```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

pip install numpy pandas tensorflow keras torch opencv-python ultralytics mediapipe langchain langgraph

pip show numpy pandas tensorflow keras torch opencv-python ultralytics mediapipe langchain langgraph
```

```bash
ann.compile(optimizer = 'sgd', loss = 'binary_crossentropy', metrics = ['accuracy'])
adam
adagrad
adadelta
adamax
rmsprop
sgd

ann.fit(X_train, y_train, batch_size = 32, epochs = 10)
ann.fit(X_train, y_train, batch_size = 32, epochs = 50)
ann.fit(X_train, y_train, batch_size = 32, epochs = 100)
```
