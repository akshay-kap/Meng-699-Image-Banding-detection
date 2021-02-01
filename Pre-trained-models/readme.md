Use the uploaded folder as trained tensorflow model infrence.
Use tensorflow.load_model method to load model
The model.predict method will provide ypu with a probablility associated with given patch , value closer to 1 means that patch does not have banding, whereas value closer to 0 shows that patch has high banding
