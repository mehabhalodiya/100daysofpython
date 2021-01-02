# Screen Recorder

The process is as follows:

* Capture a screenshot using pyautogui.
* Convert that screenshot to a numpy array.
* Write that numpy array to a file with the proper format using a video writer in OpenCV.

---
*Note: You need to get the correct SCREEN_SIZE from your operating system, that is the screen resolution, otherwise writing to the file won't work (alternatively, you can use pyautogui.size() function to get the size of the primary monitor).*

---

fourcc is the video codec library that OpenCV will use to write the video file, we specified XVID here. The 20.0 float value passed as third parameter to cv2.VideoWriter corresponds to the FPS (Frame Per Second).

First, we use the screenshot() function which returns an image object, so we need to convert it to a proper numpy array. After that, we need to convert that frame into RGB, that's because OpenCV uses BGR by default.

You can also record only regions of your screen, by passing region keyword argument which is a four-integer tuple representing the top, left, width and height of the region to capture, here is how it's done:

```
img = pyautogui.screenshot(region=(0, 0, 300, 400))
```

Also, you can replace the `while True` statement with a `for` loop as follows:

```
for i in range(200):
    # make a screenshot
    img = pyautogui.screenshot()
    # the rest of the code...
```

Alright, there are endless of ideas you can use to extend this.

Happy Coding!
