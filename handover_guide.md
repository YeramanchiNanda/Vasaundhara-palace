# Vasundhara Palace - Master Website Handover & Operations Guide

Welcome to the official client handover package for the **Vasundhara Palace** website. This handbook is designed for both the project administrator and the client. It details the deliverables, explains how to manage content (menu items, prices, videos, and images) with zero code, recommends hosting providers, and provides a clear sign-off process.

---

## 1. Deliverables Directory

The website package is built using pure, high-performance HTML5, CSS3, and modern ES6 JavaScript. It is optimized to be responsive, meaning it renders beautifully on all devices—from desktop monitors to tablets and mobile phones.

### Core File Structure
* **`index.html`** - The homepage featuring the scrolling hero video, "Our Story" video, food grid portfolio, customer reviews, and interactive contact form.
* **`menu.html`** - The interactive menu page displaying categories in a dual-column layout on desktop, and a horizontal scrollable category bar on mobile devices.
* **`party-hall.html`** - A dedicated layout highlighting reception hall details, guest capacity, and a bento media showcase.
* **`gallery.html`** - A widescreen cinematic lightbox grid showcasing high-resolution photos and silent looping videos.
* **`styles.css`** - The master stylesheet containing colors, typography rules, mobile breakpoints (992px / 768px / 480px), and layout structures.
* **`script.js`** - Controls interactive effects such as the loading screen fade-out, mobile navigation dropdown toggle, vertical sidebar scrollspy alignment, and video playlist loops.
* **`data/menu.json`** - The central menu database.
* **`update_menu.py`** - The automated script that compiles `menu.json` data into the visual design of `menu.html`.

---

## 2. Web Hosting Recommendations (For Production Launch)

Since the website is a static project, it does not require complex backend server runtimes (like PHP or Node.js). To support high user traffic and ensure instant loading times, we recommend the following options:

### Option A: Vercel or Netlify (Recommended - Modern CDN Hosting)
Best for: **Maximum speed, zero maintenance, and 100% uptime.**
* **Cost:** Free tier (includes free SSL certificate and custom domain connection).
* **Pros:** 
  * Files are distributed across a Global Content Delivery Network (CDN), making page loads near-instant.
  * Simple drop-and-deploy interface (drag folder onto Vercel dashboard).
  * Auto-invalidates browser cache when files are updated.
* **Cons:** No native email hosting (you would purchase custom emails like `info@vasundhara-palace.com` via Google Workspace or ZoHo Mail separately).

### Option B: Hostinger or GoDaddy (Traditional cPanel Hosting)
Best for: **All-in-one package (hosting + custom email boxes).**
* **Cost:** Paid subscription (starting at $2 to $5/month).
* **Pros:** 
  * Includes cPanel access where you can directly manage files.
  * Allows you to create and host email boxes directly on the server for free.
* **Cons:** 
  * Slower server response times compared to Netlify/Vercel CDNs.
  * Manual cache busting is sometimes required for visitors to see media changes.

---

## 3. How to Update Website Content

We have separated the data from the design. You do not need to edit HTML code to update the food menu or replace images/videos.

### Part A: Updating the Food & Beverage Menu
All menu categories, items, prices, and special highlight indicators are managed inside **`data/menu.json`**.

1. Open **`data/menu.json`** in any simple text editor.
2. Edit or add menu objects inside their category arrays:
   ```json
   {
     "name": "Ghee Masala Dosa",
     "price": "₹125",
     "special": true
   }
   ```
   * *`"name"`: The item title.*
   * *`"price"`: The displayed price.*
   * *`"special": true`: Appends a premium gold star badge next to the item name.*
   * *`"disabled": true`: Greys out the item (e.g. if temporarily out-of-stock).*
3. **Compile your changes:**
   * **On macOS:** Double-click **`build_menu.command`**.
   * **On Windows:** Double-click **`build_menu.bat`**.
   * This runs the compiler tool and automatically rebuilds `menu.html` with your changes!

### Part B: Managing Media (Images & Videos)
You can swap any visual by simply replacing files in the **`assets/`** folder. Refer to the directory below:

| Target File Name | Section | Recommendation / Size |
| :--- | :--- | :--- |
| `vasundhara-lotus.png` | Main Brand Logo | Transparent `.png` (`300x300px` approx) |
| `vasundhara-hero2.mp4` | Main Hero Background Video | Compress under `3MB` for fast mobile loading |
| `legacy-video.mp4` | "Our Story" section | Vertical Portrait `9:16` ratio |
| `party-trailer.mp4` | Party Hall video showcase | Cinematic Widescreen `16:9` ratio |
| `vasundhara-pic1.jpg` to `vasundhara-pic5.jpg` | Grid Images | Optimized `.jpg` files under `200KB` |

*For a complete file-to-grid mapping sheet, check **`assets/MEDIA_UPLOADS_GUIDE.md`**.*

---

## 4. Step-by-Step Deployment Instructions

### How to deploy to Vercel (CDP):
1. Sign up for a free account at [Vercel](https://vercel.com/).
2. Click **Add New Project**.
3. Select **Deploy folder** and drag-and-drop the main project folder (`vasundhara-palace`).
4. Vercel will analyze the structure and assign a free preview link (e.g. `vasundhara-palace.vercel.app`).
5. Go to project settings, click **Domains**, and type your custom domain (e.g. `vasundhara-palace.com`). Update your domain registrar DNS settings (add CNAME/A records) as prompted by Vercel.

### How to deploy to Hostinger/GoDaddy (cPanel):
1. Log in to your hosting account and open the **File Manager**.
2. Navigate to the public directory (usually **`public_html`**).
3. Upload all the website files (`index.html`, `menu.html`, `party-hall.html`, `gallery.html`, `styles.css`, `script.js`, `404.html`, and the folders `assets/` and `data/`).
4. Visitors will immediately be able to load the site at your domain address.

---

## 5. Formal Project Sign-off & Acceptance

A professional handover requires a formal sign-off. Below is the checklist to execute with your client to complete the project cycle.

### Deliverables Checklist
- [ ] Responsive Website source package delivered.
- [ ] Local menu compiler script successfully configured and tested.
- [ ] Responsive mobile layouts verified on iOS (Safari) and Android (Chrome) viewports.
- [ ] Initial performance audit complete (hero background video optimized to 2.5MB).
- [ ] Master Handover Guide delivered.

### Client Acceptance Sign-off
By signing below, the Client confirms that all deliverables have been completed, inspected, and accepted according to the project specifications.

* **Client Name:** ___________________________
* **Signature:** _____________________________
* **Date:** __________________________________
* **Developer Name:** _______________________
* **Signature:** _____________________________
* **Date:** __________________________________
