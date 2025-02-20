<<<<<<< HEAD
import cv2

# Load the screenshot
screenshot = cv2.imread("C:\\Users\\user\\Desktop\\my-ai-assistant\\app.png")
# Load a template of the call icon
template = cv2.imread("C:\\Users\\user\\Desktop\\my-ai-assistant\\apptemp.png", 0)

# Convert screenshot to grayscale
gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

# Template matching
result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
_, _, _, max_loc = cv2.minMaxLoc(result)

print("Call icon coordinates:", max_loc)
=======
import cv2

# Load the screenshot
screenshot = cv2.imread("C:\\Users\\user\\Desktop\\my-ai-assistant\\app.png")
# Load a template of the call icon
template = cv2.imread("C:\\Users\\user\\Desktop\\my-ai-assistant\\apptemp.png", 0)

# Convert screenshot to grayscale
gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

# Template matching
result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
_, _, _, max_loc = cv2.minMaxLoc(result)

print("Call icon coordinates:", max_loc)
>>>>>>> e4bf6d6048dcaa09c75806c823b6451865cac2c9
