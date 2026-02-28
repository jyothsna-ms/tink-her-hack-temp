<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# <p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# Gesture Based Virtual Drawing Board 🎯

## Basic Details

### Team Name: [Name]

-Jyothsna M S

### Hosted Project Link
[mention your project hosted link here]

### Project Description
This project is a hand gesture-based virtual drawing board that allows users to draw, select colors, and erase using only hand movements in front of a webcam.

The system uses computer vision techniques to detect hand landmarks and interpret gestures in real time.

Users can:

Select colors using finger gestures

Draw using index finger movement

Erase using fist gesture

View palette by opening palm
### The Problem statement
Traditional drawing tools require physical input devices like mouse, stylus, or touchscreen.

This project solves:

Lack of natural interaction interfaces

Need for contactless UI systems

Accessibility-based input methods

It provides a natural human-computer interaction system using computer vision.
### The Solution

---The system uses:

MediaPipe Hand Tracking for gesture detection

OpenCV for camera processing and rendering

NumPy for canvas storage

The gestures are mapped as:

Gesture	Action
Palm Open	Show - color palette
One Finger Raised -	Select color
Index Finger Movement	- Draw


## Technical Details

### Technologies Used

Software

-Python

-OpenCV

-MediaPipe

-NumPy

Tools

-VS Code

-GitHub

---

## Features

Real-time hand tracking

Gesture-based color selection

Contactless drawing system

Smooth canvas rendering

---

## Implementation

#### Installation
```bash
pip install opencv-python mediapipe numpy
```

#### Run
```bash
python main.py
```

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
Camera Input →
Hand Detection (MediaPipe) →
Gesture Recognition →
Drawing Logic →
Canvas Rendering →
Display Output

**Application Workflow:**

![Workflow](docs/workflow.png)
*Add caption explaining your workflow*

---


### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---


*Caption: Completed project ready for testing*

---

## Project Demo

### Video
[Add your demo video link here - YouTube, Google Drive, etc.]

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - e.g., Frontend development, API integration, etc.]
- [Name 2]: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
 🎯


