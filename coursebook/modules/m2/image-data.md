---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Image Data

Earlier in this module, we introduced image data as a 2d or 3d tensor representing pixel values.

Commonly, we may wish to resize, reshape, and/or normalise image data. 

## Resizing (and Resampling)

```{note}
The term *resize* can be used to refer to changing the physical size of an image without changing the number of pixels.
In these contexts, *resampling* is used to refer to the operation that changes the total number of pixels.

However, many popular python image libraries use the term *resize* to refer to changing the total number of pixels.
We will follow this convention.
```

When resizing, interpolation methods determine pixel values when upsampling or downsampling an image. In the case of
 upsampling, the method determines the value for "new" pixels. 
 
For example, using the OpenCV library:
 
```{code-cell} ipython3
import cv2
from matplotlib import pyplot as plt

im = cv2.imread("./data/smiley_16.png")
print(f"loaded data of shape: {im.shape}")

# resize using NEAREST interpolation method
im_64_nearest = cv2.resize(im, (64,64), interpolation=cv2.INTER_NEAREST)

# resize using CUBIC interpolation method
im_64_cubic = cv2.resize(im, (64,64), interpolation=cv2.INTER_CUBIC)

# display with matplotlib
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5), dpi=80, sharex=True, sharey=True,)
ax[0].imshow(im, cmap='gray')
ax[0].set_title("16x16 original")
ax[0].axis('off')

ax[1].imshow(im_64_nearest)
ax[1].set_title("64x64 method=nearest")
ax[1].axis('off')

ax[2].imshow(im_64_cubic)
ax[2].set_title("64x64 method=cubic")
ax[2].axis('off')

plt.show()
```


## Normalisation

Image processing will often expect the data to be normalised.

As we've seen that our image data is represented in a numeric 2d or 3d tensor, we can normalise by converting the image
 to have zero mean, and unit variance. The OpenCV has some built in functionality for this:
 
TODO example code
 
However, for many deep learning tasks, it is common to normalise image data by using precomputed dataset means and stds,
rather than calculate these for each image. For example, using the ImageNet values:
 
TODO example code