#!/usr/bin/env python3
import os
import json
import re

def compile_menu():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "data", "menu.json")
    html_path = os.path.join(script_dir, "menu.html")

    print(f"Reading menu data from: {json_path}")
    if not os.path.exists(json_path):
        print(f"Error: Menu database does not exist at {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        menu_data = json.load(f)

    categories = menu_data.get("categories", [])

    # 1. Compile Sidebar Links
    sidebar_chunks = []
    for idx, cat in enumerate(categories):
        cat_id = cat.get("id")
        cat_name = cat.get("name")
        active_class = " active" if idx == 0 else ""
        link_html = f'<a href="#cat-{cat_id}" class="sidebar-link{active_class}">{cat_name}</a>'
        sidebar_chunks.append(link_html)
    
    # Standardize whitespace for inserting into menu.html
    sidebar_html = "\n                        " + "".join(sidebar_chunks) + "\n                        "

    # 2. Compile Continuous Menu Flow
    flow_chunks = []
    for cat in categories:
        cat_id = cat.get("id")
        cat_name = cat.get("name")
        cat_icon = cat.get("icon", "fa-circle-notch")
        items = cat.get("items", [])

        cat_html = []
        cat_html.append(f'                <div id="cat-{cat_id}" class="menu-category-group reveal-up">')
        cat_html.append('                    <div class="category-header">')
        cat_html.append('                        <div class="category-title-wrap">')
        cat_html.append(f'                            <i class="fas {cat_icon} gold-text-gradient category-icon-large"></i>')
        cat_html.append(f'                            <h3 class="gold-text-gradient">{cat_name}</h3>')
        cat_html.append('                        </div>')
        cat_html.append('                        <div class="category-line"></div>')
        cat_html.append('                    </div>')
        cat_html.append('                    <ul class="menu-list split-view-list">')

        for item in items:
            if item.get("spacer"):
                cat_html.append('                        <li><br></li>')
            else:
                name = item.get("name")
                price = item.get("price")
                
                # Check for item classes
                classes = []
                if item.get("special"):
                    classes.append("special")
                if item.get("disabled"):
                    classes.append("disabled")
                
                class_attr = f' class="{" ".join(classes)}"' if classes else ""
                cat_html.append(f'                        <li><div class="menu-item-name{class_attr}">{name}</div><div class="menu-dots"></div><div class="menu-item-price">{price}</div></li>')

        cat_html.append('                    </ul>')
        cat_html.append('                </div>')

        flow_chunks.append("\n".join(cat_html))

    flow_html = "\n                    " + "\n\n".join(flow_chunks) + "\n                    "

    # 3. Read and Update menu.html
    print(f"Reading target template: {html_path}")
    if not os.path.exists(html_path):
        print(f"Error: Target HTML page does not exist at {html_path}")
        return

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Regex replacements
    sidebar_pattern = r"(<!-- SIDEBAR_START -->)(.*?)(<!-- SIDEBAR_END -->)"
    flow_pattern = r"(<!-- FLOW_START -->)(.*?)(<!-- FLOW_END -->)"

    # Validate template tag existence
    if not re.search(sidebar_pattern, html_content, re.DOTALL):
        print("Error: Could not find <!-- SIDEBAR_START --> and <!-- SIDEBAR_END --> placeholder comments in menu.html")
        return
    if not re.search(flow_pattern, html_content, re.DOTALL):
        print("Error: Could not find <!-- FLOW_START --> and <!-- FLOW_END --> placeholder comments in menu.html")
        return

    updated_content = re.sub(
        sidebar_pattern,
        rf"\g<1>{sidebar_html}\g<3>",
        html_content,
        flags=re.DOTALL
    )

    updated_content = re.sub(
        flow_pattern,
        rf"\g<1>{flow_html}\g<3>",
        updated_content,
        flags=re.DOTALL
    )

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("Success! menu.html compiled successfully.")

if __name__ == "__main__":
    compile_menu()
