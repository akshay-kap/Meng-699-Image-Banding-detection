- Use the uploaded [`model folder`](model) as trained tensorflow model infrence.
- Use tensorflow.load_model method to load model.
- The input image patch to this model is of size 235x235 pixels.
- The model.predict method will provide ypu with a probablility associated with given patch , value closer to 1 means that patch does not have banding, whereas value closer to 0 shows that patch has high banding.

<br>

The following image describes the selected CNN_model architecture:

<br>

![CNN_Classifier Architecture](CNN_model_architecture.png)

