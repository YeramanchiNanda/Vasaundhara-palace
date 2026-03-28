import re

html_path = "/Users/sush/Desktop/Yeramanchi/vasundhara-palace/index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_content = """<div class="tab-content active" id="tab-breakfast">
                <div class="menu-category-grid">
                    <div class="menu-category reveal-up">
                        <h3 class="gold-text-gradient"><i class="fas fa-sun category-icon"></i> Breakfast Classics</h3>
                        <ul class="menu-list">
                            <li><div class="menu-item-name">Idly (2)</div><div class="menu-dots"></div><div class="menu-item-price">₹45</div></li>
                            <li><div class="menu-item-name">Idly 3 PCS</div><div class="menu-dots"></div><div class="menu-item-price">₹65</div></li>
                            <li><div class="menu-item-name">Single Idly</div><div class="menu-dots"></div><div class="menu-item-price">₹23</div></li>
                            <li><div class="menu-item-name">Rava Idly</div><div class="menu-dots"></div><div class="menu-item-price">₹60</div></li>
                            <li><div class="menu-item-name">Vada (1 PC / 2 PC)</div><div class="menu-dots"></div><div class="menu-item-price">₹30 / ₹60</div></li>
                            <li><div class="menu-item-name">Idly (2) Vada (1)</div><div class="menu-dots"></div><div class="menu-item-price">₹75</div></li>
                            <li><div class="menu-item-name">Single Idly Vada</div><div class="menu-dots"></div><div class="menu-item-price">₹55</div></li>
                            <li><div class="menu-item-name">Poori</div><div class="menu-dots"></div><div class="menu-item-price">₹80</div></li>
                            <li><div class="menu-item-name">Rice Bath</div><div class="menu-dots"></div><div class="menu-item-price">₹65</div></li>
                            <li><div class="menu-item-name">Khara Bath / Kesari Bath</div><div class="menu-dots"></div><div class="menu-item-price">₹50</div></li>
                            <li><div class="menu-item-name special">Chow Chow Bath</div><div class="menu-dots"></div><div class="menu-item-price">₹90</div></li>
                            <li><div class="menu-item-name">Bisi Bele Bath / Pongal</div><div class="menu-dots"></div><div class="menu-item-price">₹70</div></li>
                            <li><div class="menu-item-name">Curd Vada</div><div class="menu-dots"></div><div class="menu-item-price">₹60</div></li>
                            <li><div class="menu-item-name">Mangalore Bajji</div><div class="menu-dots"></div><div class="menu-item-price">₹60</div></li>
                            <li><div class="menu-item-name">Avalakki Bath</div><div class="menu-dots"></div><div class="menu-item-price">₹65</div></li>
                            <li><div class="menu-item-name">Maddur Vada</div><div class="menu-dots"></div><div class="menu-item-price">₹60</div></li>
                            <li><div class="menu-item-name">Shavige Bath</div><div class="menu-dots"></div><div class="menu-item-price">₹70</div></li>
                            <li><div class="menu-item-name special">Mangalore Buns (2 PC)</div><div class="menu-dots"></div><div class="menu-item-price">₹70</div></li>
                            <li><div class="menu-item-name">Pakoda / Bajji</div><div class="menu-dots"></div><div class="menu-item-price">₹60</div></li>
                            <li><div class="menu-item-name">Masala Vada / Rava Vada</div><div class="menu-dots"></div><div class="menu-item-price">₹60</div></li>
                            <li><div class="menu-item-name">Sukkinunde (1 PC)</div><div class="menu-dots"></div><div class="menu-item-price">₹35</div></li>
                            <li><div class="menu-item-name special">Aloo Bonda / Bonda Soup</div><div class="menu-dots"></div><div class="menu-item-price">₹60 / ₹65</div></li>
                        </ul>
                    </div>
                    <div class="menu-category reveal-up" style="transition-delay: 0.1s;">
                        <h3 class="gold-text-gradient"><i class="fas fa-circle-notch category-icon"></i> Dosa Specials</h3>
                        <ul class="menu-list">
                            <li><div class="menu-item-name">Plain Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹70</div></li>
                            <li><div class="menu-item-name">Masala Dosa / Set Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹80</div></li>
                            <li><div class="menu-item-name">Onion Dosa / Rava Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹90</div></li>
                            <li><div class="menu-item-name">Paper Plain Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹110</div></li>
                            <li><div class="menu-item-name special">Paper Masala Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹120</div></li>
                            <li><div class="menu-item-name">Onion Rava Masala Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹120</div></li>
                            <li><div class="menu-item-name">Cheese Plain Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹110</div></li>
                            <li><div class="menu-item-name special">Cheese Masala Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹125</div></li>
                            <li><div class="menu-item-name">Butter Masala Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹100</div></li>
                            <li><div class="menu-item-name">Butter Plain Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹90</div></li>
                            <li><div class="menu-item-name">Rava / Mysore Masala Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹120</div></li>
                            <li><div class="menu-item-name special">Open Butter Masala</div><div class="menu-dots"></div><div class="menu-item-price">₹110</div></li>
                            <li><div class="menu-item-name">Onion Rava / Open Masala</div><div class="menu-dots"></div><div class="menu-item-price">₹110</div></li>
                            <li><div class="menu-item-name special">Ghee Masala Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹125</div></li>
                            <li><div class="menu-item-name">Paneer Masala Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹130</div></li>
                            <li><div class="menu-item-name special">Neer Dosa (3 pc)</div><div class="menu-dots"></div><div class="menu-item-price">₹75</div></li>
                            <li><div class="menu-item-name special">Ghee Pudi Masala Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹130</div></li>
                            <li><div class="menu-item-name">Ghee Pudi Plain Dosa</div><div class="menu-dots"></div><div class="menu-item-price">₹120</div></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="tab-indian">
                <div class="menu-category-grid">
                    <div class="menu-category">
                        <h3 class="gold-text-gradient"><i class="fas fa-bread-slice category-icon"></i> Indian Breads</h3>
                        <ul class="menu-list">
                            <li><div class="menu-item-name">Roti 1 PC</div><div class="menu-dots"></div><div class="menu-item-price">₹40</div></li>
                            <li><div class="menu-item-name">Butter / Methi Roti</div><div class="menu-dots"></div><div class="menu-item-price">₹50</div></li>
                            <li><div class="menu-item-name">Naan / Kulcha</div><div class="menu-dots"></div><div class="menu-item-price">₹50</div></li>
                            <li><div class="menu-item-name special">Garlic Naan</div><div class="menu-dots"></div><div class="menu-item-price">₹65</div></li>
                            <li><div class="menu-item-name">Paratha Plain</div><div class="menu-dots"></div><div class="menu-item-price">₹55</div></li>
                            <li><div class="menu-item-name">Butter Naan / Kulcha</div><div class="menu-dots"></div><div class="menu-item-price">₹60</div></li>
                            <li><div class="menu-item-name">Stuffed Kulcha</div><div class="menu-dots"></div><div class="menu-item-price">₹70</div></li>
                            <li><div class="menu-item-name">Batura (Plain)</div><div class="menu-dots"></div><div class="menu-item-price">₹80</div></li>
                            <li><div class="menu-item-name special">Channa Batura</div><div class="menu-dots"></div><div class="menu-item-price">₹140</div></li>
                            <li><div class="menu-item-name">Plain Papad</div><div class="menu-dots"></div><div class="menu-item-price">₹20</div></li>
                            <li><div class="menu-item-name">Lacha / Pudina Paratha</div><div class="menu-dots"></div><div class="menu-item-price">₹60</div></li>
                            <li><div class="menu-item-name">Aloo / Gobi / Paneer Parota</div><div class="menu-dots"></div><div class="menu-item-price">₹80</div></li>
                            <li><div class="menu-item-name">Roti Curry / Butter Roti</div><div class="menu-dots"></div><div class="menu-item-price">₹100</div></li>
                            <li><div class="menu-item-name">Butter Naan / Kulcha Curry</div><div class="menu-dots"></div><div class="menu-item-price">₹130</div></li>
                        </ul>
                    </div>
                    <div class="menu-category">
                        <h3 class="gold-text-gradient"><i class="fas fa-fire category-icon"></i> Tandoor Starters</h3>
                        <ul class="menu-list">
                            <li><div class="menu-item-name disabled">Harabara Kabab</div><div class="menu-dots"></div><div class="menu-item-price">₹200</div></li>
                            <li><div class="menu-item-name">Paneer Tikka</div><div class="menu-dots"></div><div class="menu-item-price">₹240</div></li>
                            <li><div class="menu-item-name special">Paneer Malai Tikka</div><div class="menu-dots"></div><div class="menu-item-price">₹250</div></li>
                            <li><div class="menu-item-name special">Paneer Peshawari Tikka</div><div class="menu-dots"></div><div class="menu-item-price">₹280</div></li>
                            <li><div class="menu-item-name">Tandoori Mushroom</div><div class="menu-dots"></div><div class="menu-item-price">₹210</div></li>
                            <li><div class="menu-item-name">Tandoori Baby Corn / Gobi</div><div class="menu-dots"></div><div class="menu-item-price">₹200 / ₹190</div></li>
                            <li><div class="menu-item-name special">Veg Sheek Kabab</div><div class="menu-dots"></div><div class="menu-item-price">₹220</div></li>
                            <li><div class="menu-item-name">Tandoori Aloo</div><div class="menu-dots"></div><div class="menu-item-price">₹190</div></li>
                        </ul>
                        
                        <h3 class="gold-text-gradient mt-4"><i class="fas fa-bowl-rice category-icon"></i> Biriyani & Rice</h3>
                        <ul class="menu-list">
                            <li><div class="menu-item-name">Jeera Rice / Ghee Rice</div><div class="menu-dots"></div><div class="menu-item-price">₹140</div></li>
                            <li><div class="menu-item-name">Veg / Peas Pulao</div><div class="menu-dots"></div><div class="menu-item-price">₹150 / ₹160</div></li>
                            <li><div class="menu-item-name">Dal Khichdi</div><div class="menu-dots"></div><div class="menu-item-price">₹150</div></li>
                            <li><div class="menu-item-name">Veg Biriyani / Palak Rice</div><div class="menu-dots"></div><div class="menu-item-price">₹170</div></li>
                            <li><div class="menu-item-name special">Mughalai / Hyderabadi Biriyani</div><div class="menu-dots"></div><div class="menu-item-price">₹185 / ₹180</div></li>
                            <li><div class="menu-item-name">Paneer Biriyani</div><div class="menu-dots"></div><div class="menu-item-price">₹190</div></li>
                            <li><div class="menu-item-name special">VP Special Biriyani</div><div class="menu-dots"></div><div class="menu-item-price">₹200</div></li>
                            <li><div class="menu-item-name">Kaju / Kaju Matar Pulao</div><div class="menu-dots"></div><div class="menu-item-price">₹210 / ₹220</div></li>
                        </ul>
                    </div>
                </div>
                <!-- Row 2 -->
                <div class="menu-category-grid mt-4">
                    <div class="menu-category">
                        <h3 class="gold-text-gradient"><i class="fas fa-leaf category-icon"></i> Palak & Dal Specials</h3>
                        <ul class="menu-list">
                            <li><div class="menu-item-name special">Palak Paneer</div><div class="menu-dots"></div><div class="menu-item-price">₹240</div></li>
                            <li><div class="menu-item-name">Palak Matar / Corn Palak</div><div class="menu-dots"></div><div class="menu-item-price">₹180</div></li>
                            <li><div class="menu-item-name">Plain / Aloo Palak</div><div class="menu-dots"></div><div class="menu-item-price">₹170 / ₹180</div></li>
                            <li><div class="menu-item-name">Dal Fry</div><div class="menu-dots"></div><div class="menu-item-price">₹170</div></li>
                            <li><div class="menu-item-name">Dal Tadka / Dal Palak</div><div class="menu-dots"></div><div class="menu-item-price">₹180</div></li>
                            <li><div class="menu-item-name">Dal Kolhapuri / Dal Makhani</div><div class="menu-dots"></div><div class="menu-item-price">₹190</div></li>
                        </ul>
                        
                        <h3 class="gold-text-gradient mt-4"><i class="fas fa-drum category-icon"></i> Full Indian Meals</h3>
                        <ul class="menu-list">
                            <li><div class="menu-item-name">South Indian Meals</div><div class="menu-dots"></div><div class="menu-item-price">₹130</div></li>
                            <li><div class="menu-item-name">South Meals Parcel</div><div class="menu-dots"></div><div class="menu-item-price">₹150</div></li>
                            <li><div class="menu-item-name">Mini Meals / Parcel</div><div class="menu-dots"></div><div class="menu-item-price">₹80 / ₹100</div></li>
                            <li><div class="menu-item-name">North Indian Meals</div><div class="menu-dots"></div><div class="menu-item-price">₹180</div></li>
                            <li><div class="menu-item-name">North Meals Parcel</div><div class="menu-dots"></div><div class="menu-item-price">₹190</div></li>
                        </ul>
                    </div>
                    <div class="menu-category">
                        <h3 class="gold-text-gradient"><i class="fas fa-fire-burner category-icon"></i> Koftha, Kadai & Jain Curries</h3>
                        <ul class="menu-list">
                            <li><div class="menu-item-name">Veg Jaipuri / Veg Kolhapuri</div><div class="menu-dots"></div><div class="menu-item-price">₹230</div></li>
                            <li><div class="menu-item-name special">Veg Lahore Koftha</div><div class="menu-dots"></div><div class="menu-item-price">₹240</div></li>
                            <li><div class="menu-item-name">Veg Kadai</div><div class="menu-dots"></div><div class="menu-item-price">₹230</div></li>
                            <li><div class="menu-item-name special">Kadai Paneer</div><div class="menu-dots"></div><div class="menu-item-price">₹260</div></li>
                            <li><div class="menu-item-name">Paneer Koftha</div><div class="menu-dots"></div><div class="menu-item-price">₹260</div></li>
                            <li><div class="menu-item-name">Paneer / Kadai Kolhapuri</div><div class="menu-dots"></div><div class="menu-item-price">₹270</div></li>
                            <li><div class="menu-item-name special">Nargis Koftha</div><div class="menu-dots"></div><div class="menu-item-price">₹270</div></li>
                            <li><div class="menu-item-name">Kaju Kadai</div><div class="menu-dots"></div><div class="menu-item-price">₹280</div></li>
                            <li><div class="menu-item-name special">Kaju Kadai Paneer</div><div class="menu-dots"></div><div class="menu-item-price">₹280</div></li>
                            <li><br></li>
                            <li><div class="menu-item-name">Jain Dal Fry / Dal Palak</div><div class="menu-dots"></div><div class="menu-item-price">₹180 / ₹190</div></li>
                            <li><div class="menu-item-name special">Jain Paneer Butter Masala</div><div class="menu-dots"></div><div class="menu-item-price">₹270</div></li>
                            <li><div class="menu-item-name">Jain Kadai Mix Veg</div><div class="menu-dots"></div><div class="menu-item-price">₹240</div></li>
                            <li><div class="menu-item-name">Jain Navaratna Kurma</div><div class="menu-dots"></div><div class="menu-item-price">₹260</div></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="tab-chinese">
                <div class="menu-category-grid">
                    <div class="menu-category">
                        <h3 class="gold-text-gradient"><i class="fas fa-bowl-rice category-icon"></i> Indo-Chinese Rice & Noodles</h3>
                        <ul class="menu-list">
                            <li><div class="menu-item-name">Veg Fried Rice</div><div class="menu-dots"></div><div class="menu-item-price">₹140</div></li>
                            <li><div class="menu-item-name">Singapore Fried Rice</div><div class="menu-dots"></div><div class="menu-item-price">₹170</div></li>
                            <li><div class="menu-item-name special">Veg Schezwan Fried Rice</div><div class="menu-dots"></div><div class="menu-item-price">₹170</div></li>
                            <li><div class="menu-item-name special">Triple Fried Rice</div><div class="menu-dots"></div><div class="menu-item-price">₹200</div></li>
                            <li><div class="menu-item-name">Baby Corn / Mushroom Fried Rice</div><div class="menu-dots"></div><div class="menu-item-price">₹150 / ₹170</div></li>
                            <li><div class="menu-item-name">Veg Noodles</div><div class="menu-dots"></div><div class="menu-item-price">₹150</div></li>
                            <li><div class="menu-item-name special">Veg Schezwan Noodles</div><div class="menu-dots"></div><div class="menu-item-price">₹180</div></li>
                            <li><div class="menu-item-name">Singapore / Mushroom Noodles</div><div class="menu-dots"></div><div class="menu-item-price">₹180</div></li>
                            <li><div class="menu-item-name">Veg Hakka Noodles</div><div class="menu-dots"></div><div class="menu-item-price">₹180</div></li>
                            <li><div class="menu-item-name">Paneer Noodles</div><div class="menu-dots"></div><div class="menu-item-price">₹190</div></li>
                            <li><div class="menu-item-name">Chinese / American Chopsey</div><div class="menu-dots"></div><div class="menu-item-price">₹190</div></li>
                            <li><div class="menu-item-name">Paneer Fried Rice</div><div class="menu-dots"></div><div class="menu-item-price">₹185</div></li>
                            <li><div class="menu-item-name">Ginger Garlic Fried Rice</div><div class="menu-dots"></div><div class="menu-item-price">₹170</div></li>
                            <li><div class="menu-item-name special">Paneer Schezwan Fried Rice</div><div class="menu-dots"></div><div class="menu-item-price">₹190</div></li>
                            <li><div class="menu-item-name special">Chinese Sizzler</div><div class="menu-dots"></div><div class="menu-item-price">₹300</div></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="tab-desserts">
                <div class="menu-category-grid">
                    <div class="menu-category">
                        <h3 class="gold-text-gradient"><i class="fas fa-ice-cream category-icon"></i> Artisanal Ice Creams</h3>
                        <ul class="menu-list">
                            <li><div class="menu-item-name">Vanilla / Chocolate</div><div class="menu-dots"></div><div class="menu-item-price">₹70</div></li>
                            <li><div class="menu-item-name">Strawberry / Mango</div><div class="menu-dots"></div><div class="menu-item-price">₹70</div></li>
                            <li><div class="menu-item-name">Pista / Butterscotch</div><div class="menu-dots"></div><div class="menu-item-price">₹80</div></li>
                            <li><div class="menu-item-name">Tutti Fruity / Kesar Pista</div><div class="menu-dots"></div><div class="menu-item-price">₹80</div></li>
                            <li><div class="menu-item-name">Jelly with Ice Cream</div><div class="menu-dots"></div><div class="menu-item-price">₹110</div></li>
                            <li><div class="menu-item-name">Fruit Salad Plain</div><div class="menu-dots"></div><div class="menu-item-price">₹110</div></li>
                            <li><div class="menu-item-name">Dry Fruits Ice Cream</div><div class="menu-dots"></div><div class="menu-item-price">₹130</div></li>
                            <li><div class="menu-item-name">Fruit Salad with Ice Cream</div><div class="menu-dots"></div><div class="menu-item-price">₹130</div></li>
                            <li><div class="menu-item-name">Vanilla Nut Sundae</div><div class="menu-dots"></div><div class="menu-item-price">₹140</div></li>
                            <li><div class="menu-item-name">Chocolate Nut Sundae</div><div class="menu-dots"></div><div class="menu-item-price">₹150</div></li>
                            <li><div class="menu-item-name">Fruit Salad with Jelly</div><div class="menu-dots"></div><div class="menu-item-price">₹150</div></li>
                            <li><div class="menu-item-name special">Double Sundae</div><div class="menu-dots"></div><div class="menu-item-price">₹160</div></li>
                            <li><div class="menu-item-name special">My Dream Ice Cream</div><div class="menu-dots"></div><div class="menu-item-price">₹160</div></li>
                            <li><div class="menu-item-name">Golden Cherry</div><div class="menu-dots"></div><div class="menu-item-price">₹170</div></li>
                            <li><div class="menu-item-name special">Sizzling Brownie & Ice Cream</div><div class="menu-dots"></div><div class="menu-item-price">₹140</div></li>
                        </ul>
                    </div>
                    <div class="menu-category">
                        <h3 class="gold-text-gradient"><i class="fas fa-mug-hot category-icon"></i> Sweets & Beverages</h3>
                        <ul class="menu-list">
                            <li><div class="menu-item-name">Bengali Sweet / Rasmalai</div><div class="menu-dots"></div><div class="menu-item-price">₹40</div></li>
                            <li><div class="menu-item-name">Jamoon (2 PC)</div><div class="menu-dots"></div><div class="menu-item-price">₹40</div></li>
                            <li><div class="menu-item-name">Carrot / Kashi Halwa</div><div class="menu-dots"></div><div class="menu-item-price">₹60</div></li>
                            <li><div class="menu-item-name special">Bele Holige / Kayi Holige</div><div class="menu-dots"></div><div class="menu-item-price">₹30</div></li>
                            <li><div class="menu-item-name">Champakali Sweets</div><div class="menu-dots"></div><div class="menu-item-price">₹30</div></li>
                            <li><div class="menu-item-name">Badam Malai Sandwich</div><div class="menu-dots"></div><div class="menu-item-price">₹30</div></li>
                            <li><br></li>
                            <li><div class="menu-item-name">Filter Degree Coffee / Tea</div><div class="menu-dots"></div><div class="menu-item-price">₹20</div></li>
                            <li><div class="menu-item-name">Badam / Ginger Tea</div><div class="menu-dots"></div><div class="menu-item-price">₹25</div></li>
                            <li><div class="menu-item-name">Horlicks / Bournvita</div><div class="menu-dots"></div><div class="menu-item-price">₹30</div></li>
                            <li><div class="menu-item-name">Lemon Tea / Milk</div><div class="menu-dots"></div><div class="menu-item-price">₹20</div></li>
                        </ul>
                    </div>
                </div>
            </div>"""

pattern = r'(<div class="tab-content active" id="tab-breakfast">.*?)(<p class="text-center text-muted mt-5" style="font-size: 0.9rem;">)'
content = re.sub(pattern, new_content.replace('\\', '\\\\') + r'\2', content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)
