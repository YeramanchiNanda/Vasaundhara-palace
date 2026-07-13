# Vasundhara Palace - Hybrid Mobile Application (Flutter)

This directory contains a hybrid mobile application container that embeds the responsive Vasundhara Palace website.

---

## 1. Prerequisites

Before running the application, make sure you have the **Flutter SDK** installed:
* [Flutter Installation Guide](https://docs.flutter.dev/get-started/install)

Once installed, check that the command works by running:
```bash
flutter --version
```

---

## 2. Step-by-Step Launch Guide

Follow these simple commands to generate the native code config and start the mobile app:

### Step A: Initialize Platform Projects
Generate the native platform projects (Android/iOS builds) using your local Flutter environment. Run this command inside the `vasundhara_mobile` directory:
```bash
flutter create --platforms=android,ios .
```
*(This command will safely generate the native platform wrappers without touching the custom code files we created for you.)*

### Step B: Configure Android Local Network Permissions
Run the python script to update your `AndroidManifest.xml`. This automatically adds the `INTERNET` permission and enables HTTP cleartext traffic, which is required to load your local web server (`http://192.168.0.107:8000`) on mobile:
```bash
python3 configure_android.py
```

### Step C: Run the App
Connect a physical device (in developer debugging mode) or start an emulator, and launch the app:
```bash
flutter run
```

---

## 3. Configuration & Production Deployment

### Loading your Live Website (Production)
Currently, the mobile app loads your local server (`http://192.168.0.107:8000/index.html`) for testing. 

When you deploy your site to production, update the target URL in `lib/main.dart` at line 53:

```dart
// Change this line to your live URL
..loadRequest(Uri.parse('https://your-live-domain.com/index.html'));
```
