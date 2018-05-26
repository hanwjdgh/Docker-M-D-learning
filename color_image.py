from PIL import Image
import numpy as np

with open("tower.jpg","rb") as file:
    img = Image.open(file)
    img = img.convert("RGB")
    img = img.resize((64,64))
    data = np.asarray(img)
    img.save("test.png")