# 🚨 Rescue App

**Rescue App** คือแอปพลิเคชันมือถือที่พัฒนาด้วย **KivyMD** และ **Python** สำหรับการรายงานเหตุฉุกเฉิน แอปนี้ช่วยให้ผู้ใช้สามารถส่งรายงานเหตุด้วยการถ่ายภาพและตำแหน่ง โดยอ้างอิงข้อมูลตำแหน่งมาจาก Public IP เก็บข้อมูลลงใน **MongoDB** พร้อมทั้งแนะนำวิธีการช่วยเหลือผู้ประสบภัย และอธิบายสัญลักษณ์กู้ภัยต่าง ๆ อย่างละเอียด

---

## 📌 คุณสมบัติเด่น

- 📍 **รายงานเหตุฉุกเฉิน:**

  - ถ่ายภาพเหตุการณ์และส่งพร้อมข้อมูลตำแหน่ง Public IP
  - เก็บและจัดการข้อมูลใน MongoDB อย่างมีประสิทธิภาพ

- 🗺️ **แผนที่:**

  - แสดงตำแหน่งของเหตุการณ์บนแผนที่

- 🛟 **คำแนะนำการช่วยเหลือ:**

  - ขั้นตอนการช่วยเหลือผู้ประสบภัยในสถานการณ์ต่าง ๆ
  - อธิบายสัญลักษณ์กู้ภัยและความหมาย

- 🔒 **ระบบยืนยันตัวตน:**
  - ระบบลงทะเบียนและเข้าสู่ระบบที่ปลอดภัย
  - แบ่งสิทธิ์การเข้าถึงระหว่างผู้ใช้ทั่วไปและผู้ดูแลระบบ

---

## 🛠️ เทคโนโลยีที่ใช้

- **Frontend:** KivyMD (Material Design สำหรับ Kivy)
- **Backend:** Python และ MongoDB
- **ฐานข้อมูล:** MongoDB สำหรับจัดเก็บรายงานและข้อมูลผู้ใช้
- **WebCam** openCV2 สำหรับให้งานกล้อง และจัดเก็บใน MongoDB
- **GPS** kivy_garden สำหรับโชว์แผนที่ และตำแหน่งปัจจุบัน

---

## 📂 โครงสร้างโปรเจค

```
RESCUE-APP/
├── fonts/
├── Image/
├── kivy_env/
├── rescue_screen/
├── test_function/
├── main_kivyMD.py
├── .gitignore
└── README.md
```

---

## ⚙️ การติดตั้งและใช้งาน

### 1. Clone โปรเจค:

```bash
git clone https://github.com/PunPK/Rescue-App.git
cd Rescue-App
```

### 2. ติดตั้ง Dependencies:

**สำหรับ macOS และ Linux**

```bash
python3 venv kivy_env
source kivy_env/bin/activate
```

### 3. ติดตั้งแพ็กเกจเพิ่มเติม:

```bash
pip install kivyMD
pip install pymongo
pip install kivy
pip install kivy_garden
pip install gridfs
pip install opencv2
```

### 4. ตั้งค่า MongoDB:

```python
MongoClient("localhost", 27017)
# ใช้งานผ่าน localhost 27017
```

### 5. รันแอป:

```bash
python main_kivyMD.py
```
## 🛠️ Functions:

### 1. หน้าการใส่หน้าและการรันหน้าของแอป ได้แบ่งเป็น 2 ฝั่ง

**1. ผู้ใช้งานยังไม่ได้ Login**
```python
class RescueApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"

        self.screen_manager = MDScreenManager() # ตั้งค่า Screen สำหรับการจัดการ Screen

        main_screen = MainScreen(name="main") # ใช้ Function MainScreen ตั้งค่าเป็นหน้าแรก
        self.screen_manager.add_widget(main_screen) # ดึงหน้า main มาใส่ใน screen_manager
        self.screen_manager.add_widget(ReceiverScreen(name="receiver")) # เรียกใช้ class ของหน้า และตั้งชื่อหน้า
        self.screen_manager.add_widget(LoginScreen(name="login"))
        self.screen_manager.add_widget(RegistrationScreen(name="register"))
        self.screen_manager.add_widget(Ruem_ber(name="officer"))
        self.screen_manager.add_widget(MyDevelop(name="mydevelop"))
        self.screen_manager.add_widget(ApplicationInfoScreen(name="applicationinfo"))
        self.screen_manager.add_widget(MapViewScreen(name="mapview"))
        self.screen_manager.add_widget(Tips_page(name="tipsview"))
        self.screen_manager.add_widget(SymbolScreen(name="symbolview"))
        self.screen_manager.current = ตั้งค่า หน้าแรกเป็น main ซึ่งคือ MainScreen สำหรับเมื่อเปิดแอปมาครั้งแรก

        return self.screen_manager
```

**2. ผู้ใช้งานที่ Login และเป็น Role: Admin**
```python
class RescueAdminApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.root = Builder.load_string(KV) # ดึงไฟล์ KV มาใช้งาน
        self.screen_manager = self.root.ids.screen_manager

        self.screen_manager.add_widget(ReportList(name="home-admin")) # เรียกใช้ class ของหน้า และตั้งชื่อหน้า
        self.screen_manager.add_widget(ReportDetailsScreen(name="reports-detail"))
        self.screen_manager.add_widget(Tool_page(name="tool-page"))
        self.screen_manager.add_widget(Card_page(name=("card-page")))
        self.screen_manager.add_widget(CreateCardScreen(name=("create_card")))
        self.screen_manager.add_widget(EditCardScreen(name=("edit_card")))
        self.screen_manager.add_widget(Tips_page(name=("tips-page")))
        self.screen_manager.add_widget(CreateTipScreen(name=("create_tip")))
        self.screen_manager.add_widget(EditTipScreen(name=("edit_tip")))
        self.screen_manager.add_widget(MyAdminDevelop(name=("view-develop")))
        # Set initial screen AFTER adding screens
        self.screen_manager.current = "home-admin" ตั้งค่า หน้าแรกเป็น home-admin ซึ่งคือ ReportList สำหรับเมื่อ login เข้ามา

        return self.root
```

### 2. Function Login

**1. การเรียกใช้งาน DataBase**

```python
from pymongo import MongoClient, errors

client = MongoClient("localhost", 27017) # เชื่อมต่อ MongoDB localhost 27017
db = client["rescue_app"] # เรียกใช้ ฐานข้อมูลใน DataBase MongoDB
users_collection = db["users"] # ตั้งชื่อ collection users MongoDB

# ตรวจสอบและสร้างข้อมูลผู้ใช้และรายงานหากไม่มี
if users_collection.count_documents({}) == 0:
    users_collection.insert_many(
        [
            {"username": "admin", "password": "admin123", "role": "admin"}, # สร้าง User เริ่มต้น
        ]
    )
```

**2. การเรียกใช้งาน Font**

```python
LabelBase.register(name="ThaiFont", fn_regular="fonts/THSarabunNew.ttf") # ลง font และตั้งชื่อ Font เป็น ThaiFont
```

**3. LoginScreen.py**
```python
class LoginScreen(MDScreen):
    def login(self):
        username = self.ids.username_input.text #รับค่าซึ่งดึงข้อมูล id username_input จาก .kv
        password = self.ids.password_input.text #รับค่าซึ่งดึงข้อมูล id password_input จาก .kv

        user = users_collection.find_one({"username": username})

        if user and user["password"] == password: # ตรวจสอบว่า User และ Password มีครบ
            role = user["role"]
            if role == "admin": # ถ้าเป็น role Admin
                # Switch to admin app
                MDApp.get_running_app().switch_to_admin_app() # ดึงข้อมูลแอปที่รันอยู่ และจะเรียกใช้ switch_to_admin_app() ใน main_kivyMD.py

        self.ids.username_input.text = "" # ล้างข้อมูลจาก id username_input ของ .kv
        self.ids.password_input.text = "" # ล้างข้อมูลจาก id password_input ของ .kv
```
**4. Screen.kv**
```kv
                TextInput:
                    id: username_input # ตั้งชื่อ ID สำหรับไปเรียกใช้ใน .py
                    hint_text: 'ชื่อผู้ใช้'
                    font_name: 'ThaiFont' # เรียกใช้งาน font จากที่ตั้งค่าไว้ใน .py

                TextInput:
                    id: password_input 
                    hint_text: 'รหัสผ่าน'
                    font_name: 'ThaiFont'
```
**5. main_kivyMD.py**
```python
def switch_to_admin_app(self):
        self.stop() # หยุดการใช้งาน App ปัจจุบัน 
        from admin_kivyMD import RescueAdminApp # ดึง App ของ Admin มา
        RescueAdminApp().run() # รัน App ของ Admin แทน
```

### 3. Function Logout

**1. admin_kivyMD.py  (KV)**
```kv
MDBottomNavigationItem:
            name: 'nav_logout'
            text: 'logout'
            icon: 'logout-variant'
            on_tab_press: app.switch_to_user_app() # เรียกใช้งาน RescueAdminApp -> switch_to_user_app
```
**2. admin_kivyMD.py**
```python
class RescueAdminApp(MDApp): 
    def switch_to_user_app(self):
        self.stop() # หยุดการใช้งาน App ปัจจุบัน 
        from main_kivyMD import RescueApp # ดึง App ของ User มา
        RescueApp().run() # รัน App ของ User แทน
```

### 4. Functions Create Edit Delete Number Info

**1. การเรียกใช้งาน DataBase**

```python
from pymongo import MongoClient, errors
client = MongoClient("localhost", 27017)  # เชื่อมต่อ MongoDB localhost 27017
db = client["rescue_app"] # เรียกใช้ Data Base MongoDB
numbers_info_collection = db["numbers_info"] # ตั้งชื่อ numbers_info_collection MongoDB
```

**2. หน้าแสดง Crad เพื่อโชว์ข้อมูล Number**
```python
class Card_page(MDScreen):
    def load_cards(self): # Load การ์ด ทั้งหมด
        self.card_list.clear_widgets()
        numbers_info_data = numbers_info_collection.find() ค้นหาข้อมูล Crad ใน mongodb

        for i in numbers_info_data: # loop การแสดงผลข้อมูลการ์ด
            item = TwoLineListItem(
                text=f"Phone Number: {i['phone_number']}", # ดึง phone_number ใน collection มาแสดงผล
                secondary_text=f"Agency: {i['agency']}", # ดึง agency ใน collection มาแสดงผล
                on_release=lambda x, i=i: self.edit_card(i), # เพิ่มให้สามารถกดปุ่มแล้วจะสามารถ Edit ได้
            )
            self.card_list.add_widget(item)
```


**3. หน้า Create Crad เพื่อโชว์ข้อมูล Number**
```python
class CreateCardScreen(MDScreen):
    def save_card(self, instance):
        title = self.title_field.text
        phone_number = self.phone_number_field.text
        data = {"agency": title, "phone_number": phone_number} # ดึงข้อมูลมาเก็บไว้
        numbers_info_collection.insert_one(data) # นำเข้า DataBase

        self.manager.current = "card-page"
        self.manager.get_screen("card-page").load_cards() # กลับไปหน้า card-page และ fetch ข้อมูลให้ตรงตาม DataBase
```

**4. หน้า Edit Delete Crad เพื่อโชว์ข้อมูล Number**
```python
class Card_page(MDScreen):
    def edit_card(self, card_data): # เมื่อมีการกด Edit Card จะเรียกใข้งาน Function
        self.manager.get_screen("edit_card").set_card_data(card_data) # ไปยังหน้า edit_card พร้อมทั้ง set ข้อมูลที่จะส่งไปด้วย แต่ที่จะสามารถแก้ไขได้
        self.manager.current = "edit_card" # สลับหน้าไปยังหน้า Edit

class EditCardScreen(MDScreen):
    def set_card_data(self, card_data):
        self.card_data = card_data
        self.title_field.text = card_data["agency"] # ดึงข้อมูลมาเก็บไว้ 
        self.phone_number_field.text = card_data["phone_number"] # ดึงข้อมูลมาเก็บไว้ 

    def save_card(self, instance): # กด save ข้อมูล crad
        title = self.title_field.text # ดึงค่า title_field และมาแปลงเป็น text
        phone_number = self.phone_number_field.text # ดึงค่า phone_number_field และมาแปลงเป็น text
        numbers_info_collection.update_one( # เก็บข้อมูลใน collections
            {"_id": self.card_data["_id"]}, # เลือกที่ id ตรงกัน และส่งค่าข้อมูลไป
            {"$set": {"agency": title, "phone_number": phone_number}}, # ดึง title ของ phone_number มาเก็บใน Database 
        )

        self.manager.current = "card-page"
        self.manager.get_screen("card-page").load_cards() # กลับไปหน้า card-page และ fetch ข้อมูลให้ตรงตาม DataBase
```


**5. หน้า Delete Crad เพื่อโชว์ข้อมูล Number**
```python
class EditCardScreen(MDScreen):
    def delete_card(self, instance):
        numbers_info_collection.delete_one({"_id": self.card_data["_id"]}) # หาที่ id ตรงกันของข้อมูลกับใน DataBase และทำการลบข้อมูลนั้นไปด้วย delete_one
        self.manager.current = "card-page"
        self.manager.get_screen("card-page").load_cards() # กลับไปหน้า card-page และ fetch ข้อมูลให้ตรงตาม DataBase
```

### 5. Functions Create Edit Delete Safty Tips

**1. การเรียกใช้งาน DataBase**

```python
from pymongo import MongoClient, errors
client = MongoClient("localhost", 27017)  # เชื่อมต่อ MongoDB localhost 27017
db = client["rescue_app"] # เรียกใช้ Data Base MongoDB
tips_info_collection = db["safty_tips"] # ตั้งชื่อ tips_info_collection MongoDB
```

**2. หน้าแสดง Crad เพื่อโชว์ข้อมูล Safty Tips**
```python
class Tips_page(MDScreen):
    def load_cards(self): # Load การ์ด ทั้งหมด
        self.card_list.clear_widgets()
        tip_info_collection = tips_info_collection.find() # ค้นหาข้อมูล Crad ใน mongodb

        for i in tip_info_collection:  # loop การแสดงผลข้อมูลการ์ด
            item = OneLineListItem(
                text=f"name: {i['name']}",  # ดึง name ใน collection มาแสดงผล
                on_release=lambda x, i=i: self.edit_tip(i),  # เพิ่มให้สามารถกดปุ่มแล้วจะสามารถ Edit ได้
            )
            self.card_list.add_widget(item)
```


**3. หน้า Create ข้อมูล Safty Tips**
```python
class CreateTipScreen(MDScreen):
    def save_card(self, instance):
        title = self.title_field.text
        url = self.url_field.text
        data = {"name": title, "url": url} # ดึงข้อมูลมาเก็บไว้
        tips_info_collection.insert_one(data) # นำเข้า DataBase

        self.manager.get_screen("tips-page").load_cards() # กลับไปหน้า tips-page และ fetch ข้อมูลให้ตรงตาม DataBase
        self.manager.current = "tips-page"
```

**4. หน้า Edit ข้อมูล Safty Tips**
```python
class Tips_page(MDScreen):
    ef edit_tip(self, card_data): # เมื่อมีการกด Edit Card จะเรียกใข้งาน Function
        self.manager.get_screen("edit_tip").set_card_data(card_data) # ไปยังหน้า edit_card พร้อมทั้ง set ข้อมูลที่จะส่งไปด้วย แต่ที่จะสามารถแก้ไขได้
        self.manager.current = "edit_tip" # สลับหน้าไปยังหน้า Edit

class EditTipScreen(MDScreen):
    def set_card_data(self, card_data):
        self.card_data = card_data
        self.title_field.text = card_data["name"] # ดึงข้อมูลมาเก็บไว้ 
        self.url_field.text = card_data["url"] # ดึงข้อมูลมาเก็บไว้ 

    def save_card(self, instance): # กด save ข้อมูล crad
        title = self.title_field.text # ดึงค่า title_field และมาแปลงเป็น text
        url = self.url_field.text # ดึงค่า title_field และมาแปลงเป็น text
        tips_info_collection.update_one( # อัดเดตข้อมูลใน collections
            {"_id": self.card_data["_id"]}, # เลือกที่ id ตรงกัน และส่งค่าข้อมูลไป
            {"$set": {"name": title, "url": url}}, # ดึง title ของ url มาเก็บใน Database 
        )

        self.manager.current = "tips-page"
        self.manager.get_screen("tips-page").load_cards() # กลับไปหน้า tips-page และ fetch ข้อมูลให้ตรงตาม DataBase
```


**5. หน้า Delete ข้อมูล Safty Tips**
```python
class EditTipScreen(MDScreen):
    def delete_card(self, instance):
        numbers_info_collection.delete_one({"_id": self.card_data["_id"]})  # หาที่ id ตรงกันของข้อมูลกับใน DataBase และทำการลบข้อมูลนั้นไปด้วย delete_one
        self.manager.current = "tips-page"
        self.manager.get_screen("tips-page").load_cards() # กลับไปหน้า card-page และ fetch ข้อมูลให้ตรงตาม DataBase
```

### 6. หน้าสำหรับ ส่งreport
```bash
client = MongoClient("localhost", 27017)
db = client["rescue_app"]
users_collection = db["users"]
reports_collection = db["reports"]
```
เชื่อม database(MongoDB) ใช้ library pymongo import MongoClient (เป็น localhost ที่ port 27017) และกำหนด collection

```bash
if users_collection.count_documents({}) == 0:
    users_collection.insert_many(
        [
            {"username": "admin", "password": "admin123", "role": "admin"},
            {"username": "user", "password": "user123", "role": "user"},
        ]
    )

if reports_collection.count_documents({}) == 0:
    reports_collection.insert_one(
        {"location": "Initial Location", "description": "Initial Description"}
    )
```
ถ้าใน collection นั้นไม่มีเอกสารให้ใส่ไปเป็นค่า default ไปก่อน 1 อัน เช่นใน report ให้ใส่ location เป็น “Initial Location” description เป็น “Initial Description”

```bash
Builder.load_file("rescue_screen/Screen.kv") #โหลดไฟล์ Kivy Layout

Window.size = (430, 740) #กำหนดขนาดของหน้าต่าง kivy


class ReceiverScreen(MDScreen): #สร้างคลาส ReceiverScreen
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #สร้าง MapView ที่แสดงแผนที่และกำหนดค่าพิกัดเริ่มต้น ใส่ map ใน boxlayout ที่ id map_container
        self.mapview = MapView(zoom=13, lat=7.00724, lon=100.50176)
        self.ids.map_container.add_widget(self.mapview)
        self.marker = None #set maker ใน map และตำแหน่ง เป็น None
        self.current_location = None
        self.get_location_from_ip()   #ใช้ ฟังชั่น get_location_from_ip ฟังก์ชั่นนี้จะเอาpublic ip ไปหาตำแหน่ง

        #set การ setup กล้อง,capture ,widget ของ image, layout,รูปที่ capture เป็น none
        self.camera_index = None
        self.capture = None
        self.image_widget = None
        self.layout = None
        self.captured_image_widget = None
        #ใช้ฟังก์ชันเพื่อเพิ่มแผนที่
        self.add_map()

    def get_location_from_ip(self):
        try:
            response = requests.get("https://ipinfo.io") #ใช้ library request  เพื่อไปget ข้อมูลของ public ip ที่เว็บ https://ipinfo.io/ (ไฟล์ json)
            data = response.json()
            loc = data["loc"].split(",")
            lat, lon = float(loc[0]), float(loc[1]) #เอาแค่ค่า latitude longitude
            print(f"Location from IP: lat={lat}, lon={lon}")
            self.current_location = [lat, lon]

            if self.marker:
                self.mapview.remove_marker(self.marker)
            self.marker = MapMarker(lat=lat, lon=lon) #เพิ่มตัวชี้ตำแหน่งลงบนแผนที่ ที่ latitude longitude นั้น
            self.mapview.add_marker(self.marker)

        except Exception as e:
            print(f"Error fetching location from IP: {e}")

    def update_current_location(self, *args): #อัปเดตตำแหน่งปัจจุบันโดยการดึงจาก IP อีกครั้ง
        self.get_location_from_ip()
        print(f"Using real-time IP-based location: {self.current_location}")

    def add_map(self): #เพิ่มแผนที่และปุ่มเพื่อดึงตำแหน่งปัจจุบันตั้ง default ของตัวชี้ตำแหน่งไว้
        self.marker = MapMarker(lat=7.00724, lon=100.50176)
        self.mapview.add_marker(self.marker)
        #ปุ่มเพื่อดึงตำแหน่งปัจจุบัน เมื่อกดแล้วจะได้ตำแหน่งปัจจุบันมา
        get_location_btn = Button(
            text="Get Current Location", size_hint=(1, None), height="50dp"
        )
        get_location_btn.bind(on_press=self.update_current_location)
        self.ids.map_container.add_widget(get_location_btn)
    def setup_camera(self):
        if platform.system() == "Darwin": #ตั้งค่ากล้องโดยใช้ค่า index กล้องของ platformนั้น
            self.camera_index = 0
        elif platform.system() == "Linux":
            self.camera_index = 2
        elif platform.system() == "Windows":
            self.camera_index = 1
        else:
            print("ใช้ไม่ได้บอก Hopeeee")
            return

        if not self.layout: #สร้างเลย์เอาต์สำหรับแสดงภาพจากกล้อง ใช้ library from kivy.uix.image import Image
            self.layout = BoxLayout(orientation="vertical", size_hint=(1, 1))
            self.image_widget = Image(size_hint=(1, 1))
            self.layout.add_widget(self.image_widget)

        self.ids.cam_container.add_widget(self.layout)

        self.capture = cv2.VideoCapture(self.camera_index) #เปิดการจับภาพจากกล้อง ใช้ cv2
        if not self.capture.isOpened():
            print("Error: Could not open camera.")
        else:
            print("Camera opened successfully!")
            Clock.schedule_interval(self.update, 1.0 / 30.0)
            self.ids.open_cam_button.opacity = 0

    def update(self, dt): #ฟังก์ชันที่อัปเดตภาพจากกล้องทุกๆ 30 เฟรม
        try:
            ret, frame = self.capture.read()

            if ret:
                print("Frame captured successfully.")
                frame = cv2.rotate(frame, cv2.ROTATE_180)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

                texture = Texture.create(
                    size=(frame.shape[1], frame.shape[0]), colorfmt="rgb"
                )
                texture.blit_buffer(frame.tobytes(), colorfmt="rgb", bufferfmt="ubyte")

                #เอาภาพที่ได้จาก texture ใส่ ใน image widget
                self.image_widget.texture = texture
            else:
                print("Error: Could not read frame.")
        except Exception as e:
            print(f"An error occurred while updating the frame: {e}")

    def capture_photo(self):
        try:
            self.update_current_location()
            ret, frame = self.capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.flip(frame, 0)
                #แสดงภาพที่จับได้บน widget
                _, buffer = cv2.imencode(".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                self.img_str = base64.b64encode(buffer).decode("utf-8")
                print("Photo captured. Ready to send in report.")
                self.show_popup("Success", "Photo captured successfully!")
                self.ids.photo_container.opacity = 1

                if not self.captured_image_widget:
                    self.captured_image_widget = Image()
                    self.ids.photo_container.add_widget(
                        self.captured_image_widget, index=1
                    )

                texture = Texture.create(
                    size=(frame.shape[1], frame.shape[0]), colorfmt="rgb"
                )
                texture.blit_buffer(frame.tobytes(), colorfmt="rgb", bufferfmt="ubyte")
                self.captured_image_widget.texture = texture
            else:
                print("Error: Could not capture the photo.")
                self.show_popup("Error", "Failed to capture the photo.")
        except Exception as e:
            print(f"An error occurred while capturing the photo: {e}")
            self.show_popup("Error", f"An error occurred: {e}")

    def send_report(self): #การส่งreport
        try:
            self.update_current_location()   # เอา location ล่าสุดที่ได้จากการupdate locatin
            location = self.ids.location_input.text #ชื่อ location,descriptipn เอามาจากการ input ข้อมูล
            description = self.ids.description_input.text

            if location and description:
                report = {
                    "location": location,
                    "description": description,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
                if self.current_location:
                    report["latitude"] = self.current_location[0]
                    report["longitude"] = self.current_location[1]

                if hasattr(self, "img_str"):
                    report["image"] = self.img_str # image ส่งที่เข้ารหัสไว้แล้ว

                # เพิ่มเอกสารเข้า DB (report collection)
                reports_collection.insert_one(report)

                # reset field หลังจากส่ง,หยุดการทำงานกล้อง,show ข้อความ และให้กลับไปที่หน้า main
                self.ids.location_input.text = ""
                self.ids.description_input.text = ""
                self.on_stop()
                self.show_popup("Success", "Report sent successfully!")
                self.Nav("main")
            else:
                # Show error message if fields are not filled
                self.show_popup("Error", "Please fill all fields!")
        except Exception as e:
            print(f"An error occurred while sending the report: {e}")
            self.show_popup("Error", f"An error occurred: {e}")

    def show_popup(self, title, message): #ฟังก์ชั่นไว้สำหรับ show ข้อความ
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4),
        )
        popup.open()

    def on_stop(self): # ฟังชั่นการหยุดกล้อง
        if self.capture and self.capture.isOpened() or self.setup_camera(): #ถ้ากล้องเปิดอยู่ให้มีค่าเป็น None และไม่ update frame ที่ได้
            self.capture.release()
            self.capture = None 
            Clock.unschedule(self.update)
        #ถ้ามี layout ของ image ให้ set layout image widget เป็น None
        if self.layout and self.layout in self.ids.cam_container.children:
            self.ids.cam_container.remove_widget(self.layout)
            self.layout = None
            self.image_widget = None

    def Nav(self, page): #ฟังก์ชั่น Navigate ไปหน้าอื่น
        self.manager.current = page
```

### 7. หน้าสำหรับ show report detail
```bash
class ReportDetailsScreen(MDScreen): #หน้าดูรายละเอียด
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "reports-detail"
        self.mapview = None

    def show_report_details(self, report):
        self.ids.report_location.text = f"Location: {report.get('location', 'Unknown')}"
        self.ids.report_timestamp.text = f"Time: {report.get('timestamp', 'Unknown')}"
        self.ids.report_description.text = (
            f"Description: {report.get('description', 'No Description')}"
        )
        self.ids.report_location.font_name = "ThaiFont"
        self.ids.report_timestamp.font_name = "ThaiFont"
        self.ids.report_description.font_name = "ThaiFont"

        image_data = report.get("image", None)

        if image_data: # ถ้ามีข้อมูล image_data เป็น base64 stringให้ทำการแปลงข้อมูลนั้นเป็น bytes
            try:
                image_bytes = base64.b64decode(image_data)
                image = PILImage.open(BytesIO(image_bytes)) # เปิดภาพจาก image_bytes โดยใช้ PIL (Pillow library) 

                image = image.convert("RGBA")
                img_data = image.tobytes() # แปลงภาพเป็นข้อมูล raw bytes สำหรับใช้งานกับ texture
                
                # สร้าง texture ใหม่โดยใช้ขนาดของภาพและกำหนดสีเป็น RGBA
                texture = Texture.create(
                    size=(image.width, image.height), colorfmt="rgba"
                )
                 # ใส่ข้อมูล image ลงใน texture
                texture.blit_buffer(img_data, colorfmt="rgba", bufferfmt="ubyte")

                # ตั้งค่า texture ให้กับ widget ที่แสดงภาพ (report_image)
                self.ids.report_image.texture = texture

            except Exception as e:
                print(f"Error loading image: {e}")
                self.ids.report_image.source = "image.jpg"
        else:
            # ถ้าไม่มีข้อมูล image_data ใช้ภาพเริ่มต้น
            self.ids.report_image.source = "image.jpg"
        
        # รับค่าพิกัด latitude และ longitude จาก report ถ้าไม่มีให้กำหนดเป็นค่าเริ่มต้น 0
        lat = report.get("latitude", 0)
        lon = report.get("longitude", 0)

        # ถ้า mapview ยังไม่มีการสร้างขึ้น ให้สร้างขึ้นใหม่และเพิ่ม widget mapview เข้าไป
        if self.mapview is None:
            self.mapview = MapView(zoom=13, lat=lat, lon=lon)
            self.ids.map_container.add_widget(self.mapview)

        # ทำการกำหนด center แผนที่ไปที่พิกัดที่ได้จาก report
        self.mapview.center_on(lat, lon)
        # สร้าง marker ที่จุดพิกัด latitude, longitude ที่ได้มา
        marker = MapMarker(lat=lat, lon=lon)
        self.mapview.add_marker(marker) # เพิ่ม marker ลงบนแผนที่
```
###  6. Function Sign Up
```python
*1. การเรียกใช้งาน DataBase*

from pymongo import MongoClient, errors

client = MongoClient("localhost", 27017) # เชื่อมต่อ MongoDB localhost 27017
db = client["rescue_app"] # เรียกใช้ ฐานข้อมูลใน DataBase MongoDB
users_collection = db["users"] # ตั้งชื่อ collection users MongoDB

*2. RegistrationPage.py*
class RegistrationScreen(MDScreen):
    def show_registration_success(self):
        Username = self.ids.username_input.text # ดึงค่าจาก .kv มาเก็บไว้
        Email = self.ids.email_input.text # ดึงค่าจาก .kv มาเก็บไว้
        Password = self.ids.password_input.text # ดึงค่าจาก .kv มาเก็บไว้

        if Username and Password: # ตั้งค่าข้อมูลต่างๆ
            new_user = {
                "username": Username,
                "email": Email,
                "password": Password,
                "role": "user",
            }

            # เพิ่มรายงานใหม่ใน MongoDB
            users_collection.insert_one(new_user)

            # ล้างช่อง input
            self.ids.username_input.text = ""
            self.ids.email_input.text = ""
            self.ids.password_input.text = ""

            # login ผ่าน มี PopUp บอก
            if not self.dialog:
                self.dialog = MDDialog(
                    title="Registration Successful!",
                    text="Your account has been created successfully.",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_release=lambda x: self.dialog.dismiss(),
                        )
                    ],
                )
            self.dialog.open()
        else:
            # login ไม่ผ่าน มี PopUp บอก
            if not self.dialog:
                self.dialog = MDDialog(
                    title="Registration Error!",
                    text="Registration have a problem. Check your new username and password",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_release=lambda x: self.dialog.dismiss(),
                        )
                    ],
                )
            self.dialog.open()

*3. Screen.kv*
kv
                MDTextField:
                    hint_text: "Username *"
                    id: username_input # ตั้งชื่อ ID สำหรับไปเรียกใช้ใน .py
                    mode: "line"
                    line_color_normal: 0.1, 0.4, 0.9, 1
                    markup: True
                
                MDTextField:
                    hint_text: "E mail"
                    id: email_input # ตั้งชื่อ ID สำหรับไปเรียกใช้ใน .py
                    mode: "line"
                    line_color_normal: 0.1, 0.4, 0.9, 1
                    # markup: True
                    
                MDTextField:
                    hint_text: "Password *"
                    id: password_input # ตั้งชื่อ ID สำหรับไปเรียกใช้ใน .py
                    mode: "line"
                    password: True
                    line_color_normal: 0.1, 0.4, 0.9, 1
                    markup: True

```
## หน้าต่างของApp

### หน้า explore
<p align="center">
  <img src="./image_of_App/explore_img.png" alt="explore_image">
</p>

หน้าexplore จะเป็นหน้าศูนย์รวมการควบคุมประกอบด้วย:
  - View Map Information
  - Safty Tips 
  - Rescure Symbol
  - Sign up Application
  - Application Information
  - Developer CoE36
---
#### หน้า View Map Information
<p align="center">
  <img src="./image_of_App/map-view-img.png" alt="viewmap">
</p>

หน้านี้จะแสดงถึงตำแหน่งปัจจุบันของผู้ใช้งาน


#### หน้า Safty Tips
<p align="center">
  <img src="./image_of_App/safty-tips.png" alt="safty">
</p>


หน้านี้จะรวมคลิปวิดีโอวิธีการช่วยเหลือตนเอง
--

#### หน้า Rescure Symbol
<p align="center">
  <img src="./image_of_App/rescure-symbol.png" alt="rescure-symbol">
</p>

หน้าจะรวมป้ายด้านความปลอดภัย
--

#### หน้า sign up
<p align="center">
  <img src="./image_of_App/signup.png" alt="signup">
</p>

หน้าสำหรับการสมัครการใช้งาน
--

#### หน้า Developer CoE36
<p align="center">
  <img src="./image_of_App/developby.png" alt="developBy">
</p>


เป็นหน้าสำหรับแสดงถึงผู้พัฒนา Application นี้

---
### หน้าส่ง report
<p align="center">
  <img src="./image_of_App/report.png" alt="report_image">
</p>

เป็นหน้าที่ใช้ในการส่งreport ซึ่งจะประกอบด้วย
  - สถานที่
  - รายละเอียด
  - ตำแหน่งgps
  - เหตุการณ์
---

### หน้ารวมเบอร์
<p align="center">
  <img src="./image_of_App/phone_img.png" alt="phone_img">
</p>

หน้านี่จะเป็นหน้ารวมเบอร์ขององค์กรต่างๆที่สามารถโทรเพื่อขอความช่วยเหลือ เช่น 1669 , 191
ประกอบด้วย:
  - เบอร์
  - องค์กร
  - ปุ่มโทร
---

### หน้าlogin สำหรับ admin
<p align="center">
  <img src="./image_of_App/admin-login.png" alt="login">
</p>

หน้าสำหรับเข้าใช้งานระบบฝั่ง admin
--

### หน้า main
<p align="center">
  <img src="./image_of_App/admin-report.png" alt="admin-main">
</p>

หน้าจะแสดง report ที่userส่งมาถ้ากดเข้าไปจะประกอบด้วย:
  - สถานที่
  - รายละเอียด
  - ตำแหน่งgps
  - เหตุการณ์

<p align="center">
  <img src="./image_of_App/report-detail.png" alt="report-detail">
</p>
--

### หน้า Tool Management 
<p align="center">
  <img src="./image_of_App/tool-management.png" alt="tool-management">
</p>

หน้าจะประกอบด้วยปุ่ม
  - Phone Management ใช้เพื่อ create update delete ข้อมูล
  - Safty Tips Management ใช้เพื่อ create update delete ข้อมูล
  - View team develop แสดงผู้พัฒนา App

#### หน้า Phone Management
<p align="center">
  <img src="./image_of_App/phone-mangement.png" alt="phoneM">
</p>

<p align="center">
  <img src="./image_of_App/edit-phone.png" alt="edit">
</p>

<p align="center">
  <img src="./image_of_App/create-phone.png" alt="create">
</p>

หน้า Phone Managent จะประกอบดด้วย3หน้าหลักๆ
  - หน้าสำหรับแสดงผลเบอร์ทุกเบอร์โทรที่มีอยู่ในdb
  - หน้าสำหรับ create เบอร์โทร
  - หน้าสำหรับ edit เบอร์โทร

#### หน้า Safty Tips Management
<p align="center">
  <img src="./image_of_App/safty-management.png" alt="Safty-Tips">
</p>

<p align="center">
  <img src="./image_of_App/create-safty.png" alt="Create-Tips">
</p>

<p align="center">
  <img src="./image_of_App/edit-safty.png" alt="Edit-Tips">
</p>

หน้า Safty Tips Management 
  - หน้าสำหรับแสดงผลSafty-tipsที่มีอยู่ในdbทั้งหมด
  - หน้าสำหรับ create Safty-tip
  - หน้าสำหรับ edit Safty-tip

## 🚨 การใช้งานแอป:

- ลงทะเบียนหรือเข้าสู่ระบบ
- รายงานเหตุด้วยการถ่ายภาพและส่งตำแหน่ง GPS
- ตรวจสอบจุดเกิดเหตุบนแผนที่
- ดูคำแนะนำในการช่วยเหลือผู้ประสบภัย

---

## 🛟 สัญลักษณ์กู้ภัยที่ควรรู้:

- ⚠️ **สัญญาณอันตราย:** ใช้แจ้งเตือนว่ามีอันตรายข้างหน้า
- 🚑 **สัญลักษณ์รถพยาบาล:** บ่งบอกถึงจุดรับส่งผู้ป่วย
- 🔄 **สัญลักษณ์ทางอพยพ:** ช่วยแนะนำทางออกในกรณีฉุกเฉิน

---

## ผู้พัฒนา

### 1. นายกรธัช สุขสวัสดิ์ 6710110005

- **GitHub:** [GitHub Profile](https://github.com/Fishcanwalk)

### 2. นายปุรัสกร เกียรติ์นนทพัทธ์ 6710110270

- **GitHub:** [GitHub Profile](https://github.com/PunPK)

### 3. นายพัฒนชัย พันธุ์เกตุ 6710110280

- **GitHub:** [GitHub Profile](https://github.com/Hopewalk)

---

> 🛠️ **Developed with ❤️ using KivyMD and Python**  
> **240-123 Module Data Structure, Algorithms and Programming ** 🚀
