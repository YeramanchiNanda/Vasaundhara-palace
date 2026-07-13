# Vasundhara Palace - Client Website Handover Guide

Welcome to your new website! This guide explains how to easily manage and update the website's content, menu items, images, and videos without writing any code.

---

## 1. Updating the Food & Beverage Menu

We have separated the menu data from the visual design. All menu items, prices, and special configurations are kept in a single, simple data file: `data/menu.json`.

### How to edit the menu:
1. Open the file **`data/menu.json`** using any text editor (such as Notepad on Windows or TextEdit on Mac, or a code editor like VS Code).
2. Inside, you will see lists of items grouped under their categories (e.g., Breakfast Classics, Dosa Specials). Each item looks like this:
   ```json
   {"name": "Masala Dosa / Set Dosa", "price": "₹80"}
   ```
3. **To change a price**: Simply change the number after `"price"`. E.g., `"price": "₹90"`.
4. **To add a new item**: Add a new line inside the brackets following the exact formatting:
   ```json
   {"name": "My New Signature Dish", "price": "₹150"}
   ```
   *Note: Ensure every item in a list ends with a comma `,` EXCEPT the very last item in that category.*
5. **Special badges (Gold Stars)**: If you want to show a golden highlight star next to a chef special, add `"special": true`. E.g.:
   ```json
   {"name": "Ghee Masala Dosa", "price": "₹125", "special": true}
   ```
6. **Out-of-Stock / Unavailable items**: If an item is temporarily sold out, you can grey it out by adding `"disabled": true`. E.g.:
   ```json
   {"name": "Harabara Kabab", "price": "₹200", "disabled": true}
   ```
7. **Empty spacing**: To insert vertical empty spacing between sections within a category, add a spacer object:
   ```json
   {"spacer": true}
   ```

### Compile your changes:
Once you have saved your edits in `data/menu.json`, you must regenerate the website:
- **On macOS**: Double-click **`build_menu.command`**.
- **On Windows**: Double-click **`build_menu.bat`**.

A window will open and automatically update `menu.html`. You are now ready to upload the updated files to your hosting server!

---

## 2. Managing Images & Videos (Media)

You can swap out any image or video on the website by simply replacing the files inside the **`assets/`** folder. 

### Rules for media updates:
- **Matching File Names**: Your new photo/video file must be named **exactly** like the original file name in the assets list.
- **File Format**: The format must match (e.g., replace a `.jpg` image with a new `.jpg`, or a `.mp4` video with a `.mp4` video).

For a complete reference of what file names appear where, open and read **`assets/MEDIA_UPLOADS_GUIDE.md`**.

### Recommended Media Guidelines:
To ensure the website loads lightning-fast for your guests, optimize your assets:
- **Image Compression**: Use free online tools like [TinyJPG](https://tinyjpg.com/) or [TinyPNG](https://tinypng.com/) to compress images before saving them in the `assets/` folder.
- **Image Formats**: Use `.jpg` for high-resolution food photography, and `.png` for graphics with transparent backgrounds (like your logo).
- **Video Sizes**: Videos should be compressed (ideally under 10MB to 15MB) using tools like [Handbrake](https://handbrake.fr/).

---

## 3. Deployment & Maintenance

### How to put changes live on your server:
1. Generate the menu changes locally using the compiler script.
2. Connect to your hosting provider's file manager (e.g., Hostinger cPanel File Manager, GoDaddy, Vercel, Firebase) or use an FTP client.
3. Upload the modified files to your server directory:
   - If you modified the menu: Upload `menu.html` and `data/menu.json`.
   - If you replaced images/videos: Upload the modified files inside the `assets/` directory.

### Maintenance & Caching best practices:
- **Browser Caching**: Browsers cache static files (like images, styles, and videos) to make sites load faster. When you replace an asset (e.g. `vasundhara-lotus.png`), users might not see the new file immediately.
- **The Cache Buster Solution**: In the HTML source code, you can append a version string to force browsers to fetch the new file (e.g. `href="assets/vasundhara-lotus.png?v=final_deploy"`, changing `final_deploy` to a new number or date like `v=2026_06_30`).
