import pyautogui
import time
import pyperclip

# Short delay to switch to the screen manually (if needed)
time.sleep(2)

# Step 1: Click on the icon
pyautogui.click(1458, 1048)
time.sleep(1)  # Wait for the app/window to load

# Step 2: Drag to select text
pyautogui.moveTo(425 ,134)
pyautogui.mouseDown()
pyautogui.moveTo( 446 ,1001, duration=0.5)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy selected text to clipboard (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Read from clipboard
copied_text = pyperclip.paste()

print("Copied Text:\n", copied_text)
