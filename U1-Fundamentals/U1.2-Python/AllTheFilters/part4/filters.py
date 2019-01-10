from PIL import Image
import math

# Return an Image loaded from the specified file.
#  * filename: string, name of file to load
def load_img(filename):
  im = Image.open(filename)
  return im

# Display Image to the user (for debugging purposes).
#   * im: Image to display
def show_img(im):
  im.show()

# Save the Image to a file with the specified filename,
#  then show the Image to the user.
#  * im: Image to be saved
#  * filename: string, name to save file as
def save_img(im, filename):
  im.save(filename, "jpeg")
  show_img(im)
