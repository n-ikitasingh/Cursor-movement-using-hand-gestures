# Cursor Movement Using Hand Gestures

Cursor Movement Using Hand Gestures is a gesture-based interaction system developed to enable individuals with motor impairments to navigate digital interfaces and perform text editing tasks using hand gestures.

## System Requirements:

Before proceeding, ensure that your system meets the following requirements:
- **Operating System:** Windows 10 or later
- **Hardware:** Webcam or built-in camera with a minimum resolution of 720p
- **Software:** Python 3.6 or later, PyCharm IDE (optional), required libraries (specified below)

## Installation:

1. **Install Python:** If Python is not already installed on your system, download and install the latest version of Python from the [official website](https://www.python.org).
2. **Install PyCharm (Optional):** Download and install PyCharm, a popular Python IDE, from the [JetBrains website](https://www.jetbrains.com/pycharm/download).
3. **Install Required Libraries:** Open the command prompt or terminal and install the following Python libraries using pip:
    ```bash
    pip install opencv-python
    pip install mediapipe
    pip install autopy
    pip install pyautogui
    ```

## Running the System:

1. **Open PyCharm (Optional):** Launch PyCharm IDE if installed, or open any text editor of your choice to run the Python script.
2. **Open the Project:** Navigate to the directory where the Cursor Movement Using Hand Gestures project files are located.
3. **Open the Python Script:** Open the Python script file named "gesture_interaction_system.py" in the IDE or text editor.
4. **Configure Camera (Optional):** If you have multiple cameras connected to your system, specify the camera index in the script (line 22) to select the desired camera.
5. **Run the Script:** Click on the "Run" button in PyCharm to execute the code script.

## Using the System:

Once the system is running, follow these instructions to interact with digital interfaces using hand gestures:
- **Hand Detection:** Position your hand in front of the camera, ensuring it is well-lit and within the camera's field of view. The system will detect and track your hand movements.
- **Gesture Recognition:** Perform specific hand gestures to control cursor movement, navigate menus, and interact with on-screen elements. Refer to the gesture guide provided below for a list of supported gestures and their corresponding actions.
- **Text Editing:** Activate text editing mode by performing the designated gesture. Use additional hand gestures to select, copy, cut, paste, and edit text within the text editor interface.
- **Cursor Control:** Move your hand horizontally, vertically, or diagonally to control the position of the cursor on the screen. Perform left-click and right-click gestures to interact with on-screen buttons, links, and menus.
- **Scrolling:** Activate scrolling mode by performing the scroll gesture. Tilt your hand up or down to scroll vertically through documents, web pages, or other scrollable content.

## Gesture Guide:

- **Open Hand:** Activate cursor control mode.
- **Two Hands Detected:** Activate text editing mode.
- **Thumbs Down:** Left-click (select items, click buttons).
- **Pinky Finger Down:** Right-click (context menu, secondary actions).
- **Index Finger Up:** Scroll Up (vertical scrolling).
- **Index Finger Up + Middle Finger up:** Scroll Down (vertical scrolling).
- **Additional Gestures:** Customizable by the user for convenience.

## Troubleshooting:

If you encounter any issues while using the Cursor Movement Using Hand Gestures system, consider the following troubleshooting steps:
- Ensure proper lighting conditions and camera placement for optimal hand detection and tracking.
- Verify that the required Python libraries are installed correctly and up to date.
- Restart the system and recalibrate hand gestures if tracking inaccuracies or inconsistencies occur.
- Consult the project documentation or online resources for additional support and troubleshooting tips.
