{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Loading the libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.1.0\n",
      "[name: \"/device:CPU:0\"\n",
      "device_type: \"CPU\"\n",
      "memory_limit: 268435456\n",
      "locality {\n",
      "}\n",
      "incarnation: 10926844790436750923\n",
      ", name: \"/device:GPU:0\"\n",
      "device_type: \"GPU\"\n",
      "memory_limit: 4930941747\n",
      "locality {\n",
      "  bus_id: 1\n",
      "  links {\n",
      "  }\n",
      "}\n",
      "incarnation: 12087043325494304880\n",
      "physical_device_desc: \"device: 0, name: GeForce GTX 1060, pci bus id: 0000:01:00.0, compute capability: 6.1\"\n",
      "]\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "import tensorflow.compat.v1 as tf\n",
    "print(tf.__version__)\n",
    "from tensorflow.python.client import device_lib\n",
    "print(device_lib.list_local_devices())\n",
    "from IPython.display import display\n",
    "from PIL import Image\n",
    "import os\n",
    "import zipfile\n",
    "import random\n",
    "import tensorflow as tf\n",
    "import shutil\n",
    "from tensorflow.keras.optimizers import RMSprop,Adam\n",
    "from tensorflow.keras.preprocessing.image import ImageDataGenerator\n",
    "from shutil import copyfile\n",
    "from os import getcwd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Loading model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = tf.keras.models.load_model('model_512_batches_27july2020_epoch14/')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"sequential\"\n",
      "_________________________________________________________________\n",
      "Layer (type)                 Output Shape              Param #   \n",
      "=================================================================\n",
      "conv2d (Conv2D)              (None, 231, 231, 8)       608       \n",
      "_________________________________________________________________\n",
      "max_pooling2d (MaxPooling2D) (None, 115, 115, 8)       0         \n",
      "_________________________________________________________________\n",
      "batch_normalization (BatchNo (None, 115, 115, 8)       32        \n",
      "_________________________________________________________________\n",
      "conv2d_1 (Conv2D)            (None, 111, 111, 8)       1608      \n",
      "_________________________________________________________________\n",
      "max_pooling2d_1 (MaxPooling2 (None, 55, 55, 8)         0         \n",
      "_________________________________________________________________\n",
      "batch_normalization_1 (Batch (None, 55, 55, 8)         32        \n",
      "_________________________________________________________________\n",
      "conv2d_2 (Conv2D)            (None, 53, 53, 16)        1168      \n",
      "_________________________________________________________________\n",
      "max_pooling2d_2 (MaxPooling2 (None, 26, 26, 16)        0         \n",
      "_________________________________________________________________\n",
      "batch_normalization_2 (Batch (None, 26, 26, 16)        64        \n",
      "_________________________________________________________________\n",
      "conv2d_3 (Conv2D)            (None, 24, 24, 16)        2320      \n",
      "_________________________________________________________________\n",
      "max_pooling2d_3 (MaxPooling2 (None, 8, 8, 16)          0         \n",
      "_________________________________________________________________\n",
      "batch_normalization_3 (Batch (None, 8, 8, 16)          64        \n",
      "_________________________________________________________________\n",
      "conv2d_4 (Conv2D)            (None, 8, 8, 32)          544       \n",
      "_________________________________________________________________\n",
      "max_pooling2d_4 (MaxPooling2 (None, 2, 2, 32)          0         \n",
      "_________________________________________________________________\n",
      "global_average_pooling2d (Gl (None, 32)                0         \n",
      "_________________________________________________________________\n",
      "dense (Dense)                (None, 8)                 264       \n",
      "_________________________________________________________________\n",
      "dense_1 (Dense)              (None, 1)                 9         \n",
      "=================================================================\n",
      "Total params: 6,713\n",
      "Trainable params: 6,617\n",
      "Non-trainable params: 96\n",
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "model.summary()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Storing file names into lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "training_banded_list  = os.listdir(\"./training/banded/\")\n",
    "training_non_banded_list = os.listdir(\"./training/nonbanded/\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "58917"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(training_banded_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "76507"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(training_non_banded_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Validation data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "validation_banded_list  = os.listdir(\"./validation/banded/\")\n",
    "validation_non_banded_list = os.listdir(\"./validation/nonbanded/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7474"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(validation_banded_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9563"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(validation_non_banded_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Testing data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "testing_banded_list  = os.listdir(\"./testing/banded/\")\n",
    "testing_non_banded_list = os.listdir(\"./testing/nonbanded/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7476"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(testing_banded_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9564"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(testing_non_banded_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### making sure of all dimensions are of 235 by 235"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# getting relevant libraries\n",
    "import numpy as np\n",
    "from PIL import Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def tell_me_shape(list1, path, store):\n",
    "    \"\"\"\n",
    "    Gets input as a list of files, a path and a store option (0 or 1)\n",
    "    \"\"\"\n",
    "    temp = []\n",
    "    \n",
    "    #iterating over each file\n",
    "    for filename in list1:\n",
    "        \n",
    "        # converting to np array\n",
    "        t = np.asarray(Image.open(path+filename))\n",
    "        \n",
    "        #checking the first dimension\n",
    "        if(t.shape[0] != 235):\n",
    "            print(filename)\n",
    "            \n",
    "        else:\n",
    "            # storing if store =1\n",
    "            if (store==1):\n",
    "                temp.append(t)\n",
    "                \n",
    "                \n",
    "    temp= np.array(temp)\n",
    "    \n",
    "    if (store==1):\n",
    "        return temp\n",
    "    else :\n",
    "        return 1\n",
    "        \n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Checking results for validation set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "validation_banded_np = tell_me_shape(validation_banded_list, \"./validation/banded/\",1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "validation_non_banded_np = tell_me_shape(validation_non_banded_list, \"./validation/nonbanded/\",1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7474, 235, 235, 3)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "validation_banded_np.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(9563, 235, 235, 3)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "validation_non_banded_np.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "with open('validation_banded.pickle', 'wb') as f:\n",
    "    pickle.dump(validation_banded_np, f)\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('validation_non_banded.pickle', 'wb') as f:\n",
    "    pickle.dump(validation_non_banded_np, f)\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### checking results for test set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "testing_banded_np = tell_me_shape(testing_banded_list,\"./testing/banded/\", 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "testing_non_banded_np = tell_me_shape(testing_non_banded_list,\"./testing/nonbanded/\",1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7476, 235, 235, 3)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testing_banded_np.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(9564, 235, 235, 3)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testing_non_banded_np.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "with open('testing_non_banded.pickle', 'wb') as f:\n",
    "    pickle.dump(testing_non_banded_np, f)\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "with open('testing_banded.pickle', 'wb') as f:\n",
    "    pickle.dump(testing_banded_np, f)\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
