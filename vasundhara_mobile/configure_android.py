#!/usr/bin/env python3
import os
import re

def patch_android_manifest():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    manifest_path = os.path.join(script_dir, "android", "app", "src", "main", "AndroidManifest.xml")

    print(f"Checking for AndroidManifest at: {manifest_path}")
    if not os.path.exists(manifest_path):
        print("Error: AndroidManifest.xml not found.")
        print("Please run 'flutter create .' in the vasundhara_mobile directory first, then run this script.")
        return

    with open(manifest_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # 1. Add Internet permission if missing
    internet_permission = '<uses-permission android:name="android.permission.INTERNET"/>'
    if "android.permission.INTERNET" not in content:
        # Insert permission right before <application>
        content = re.sub(
            r"(<application)",
            f"    {internet_permission}\n\n$1",
            content,
            flags=re.IGNORECASE
        )
        print("Added INTERNET permission.")
        modified = True
    else:
        print("INTERNET permission already exists.")

    # 2. Add usesCleartextTraffic="true" to allow HTTP traffic in local dev
    cleartext_attr = 'android:usesCleartextTraffic="true"'
    if cleartext_attr not in content:
        # Insert it inside the <application tag
        content = re.sub(
            r"(<application[^>]*?)(>)",
            rf"\1\n        {cleartext_attr}\2",
            content,
            flags=re.IGNORECASE | re.DOTALL
        )
        print("Added usesCleartextTraffic=\"true\" for local testing.")
        modified = True
    else:
        print("usesCleartextTraffic is already configured.")

    if modified:
        with open(manifest_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Success: AndroidManifest.xml configured successfully!")
    else:
        print("No changes needed. AndroidManifest.xml is already configured.")

if __name__ == "__main__":
    patch_android_manifest()
