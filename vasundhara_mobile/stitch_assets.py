#!/usr/bin/env python3
import os
import shutil
import re
import subprocess

def run_menu_compilation(root_dir):
    print("Compiling menu using update_menu.py...")
    script_path = os.path.join(root_dir, "update_menu.py")
    if os.path.exists(script_path):
        result = subprocess.run(["python3", script_path], capture_output=True, text=True)
        if result.returncode == 0:
            print("Menu compilation successful.")
        else:
            print(f"Error compiling menu: {result.stderr}")
    else:
        print("update_menu.py not found, skipping compilation.")

def clean_and_create_dir(path):
    if os.path.exists(path):
        print(f"Cleaning existing directory: {path}")
        shutil.rmtree(path)
    os.makedirs(path)

def copy_web_files(root_dir, dest_dir):
    files_to_copy = [
        "index.html",
        "menu.html",
        "party-hall.html",
        "gallery.html",
        "styles.css",
        "script.js",
        "404.html"
    ]
    for file_name in files_to_copy:
        src = os.path.join(root_dir, file_name)
        dst = os.path.join(dest_dir, file_name)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copied {file_name}")
        else:
            print(f"Warning: {file_name} not found in root!")

def copy_subdirs(root_dir, dest_dir):
    subdirs = ["data", "assets"]
    for subdir in subdirs:
        src = os.path.join(root_dir, subdir)
        dst = os.path.join(dest_dir, subdir)
        if os.path.exists(src):
            shutil.copytree(src, dst)
            print(f"Copied directory {subdir} recursively.")
        else:
            print(f"Warning: {subdir} directory not found in root!")

def create_offline_fallbacks(dest_assets_dir):
    # Mapping of source existing images to target missing images for fully offline capability
    mappings = {
        "vasundhara-pic1.jpg": ["gallery-1.jpg"],
        "vasundhara-pic2.jpg": ["gallery-2.jpg", "vasundhara-pic6.jpg"],
        "vasundhara-pic3.jpg": ["gallery-3.jpg", "vasundhara-pic7.jpg"],
        "vasundhara-pic4.jpg": ["gallery-4.jpg", "vasundhara-pic8.jpg"],
        "vasundhara-pic5.jpg": ["gallery-5.jpg", "vasundhara-pic9.jpg"],
    }
    print("Generating offline local placeholder images...")
    for src_name, dst_list in mappings.items():
        src_path = os.path.join(dest_assets_dir, src_name)
        if os.path.exists(src_path):
            for dst_name in dst_list:
                dst_path = os.path.join(dest_assets_dir, dst_name)
                shutil.copy2(src_path, dst_path)
                print(f"  Created offline fallback: {dst_name} (from {src_name})")
        else:
            print(f"  Warning: Source image {src_name} not found in assets, cannot create fallbacks!")

def strip_cache_busters(dest_dir):
    print("Stripping cache-busting query parameters from local assets...")
    html_files = [f for f in os.listdir(dest_dir) if f.endswith(".html")]
    
    # Regex to find query parameters on assets (e.g., assets/vasundhara-lotus.png?v=final_deploy)
    # Matches patterns like href="assets/something.css?v=123" or src="assets/something.png?v=abc"
    pattern = re.compile(r'(\b(?:href|src)="assets/[^"?]+)\?v=[a-zA-Z0-9_-]+(")')
    
    for file_name in html_files:
        file_path = os.path.join(dest_dir, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        modified_content, count = re.subn(pattern, r'\1\2', content)
        if count > 0:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(modified_content)
            print(f"  Processed {file_name}: stripped {count} query parameter(s).")
        else:
            print(f"  No changes needed for {file_name}.")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    dest_dir = os.path.join(script_dir, "assets", "web")
    
    run_menu_compilation(root_dir)
    clean_and_create_dir(dest_dir)
    copy_web_files(root_dir, dest_dir)
    copy_subdirs(root_dir, dest_dir)
    
    dest_assets_dir = os.path.join(dest_dir, "assets")
    create_offline_fallbacks(dest_assets_dir)
    strip_cache_busters(dest_dir)
    
    print("\nOffline stitching completed successfully!")
    print(f"Local web files are bundled at: {dest_dir}")

if __name__ == "__main__":
    main()
