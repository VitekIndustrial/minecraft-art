# :art: **Minecraft-Art** :art:
Converting a **Photo** to **Minecraft Art**
## :ledger: **Description** :ledger:
The program generates from the original photo an art consisting of Minecraft game blocks.
## :bulb: Features :bulb:
+ The program runs on a *sklearn regression tree model* trained on a self-made dataset
+ Python *version 3.8*
+ The model reached a minimum error of *0.014%*
+ Multithreading applied
+ There is a setting for the *height* of the final image in Minecraft blocks, the *width* changes proportionally (It should be noted that the larger the height, the longer the code will be executed.)
+ The maximum height of the final square image is **4096** (Also depends on your amount of RAM. With 12 GB, I only have enough for 1000 blocks)
+ The final image is saved in the **best quality**
## :floppy_disk: Setup for Windows :floppy_disk:
+ Clone this repository
+ Install all the dependencies from **requirements.txt** via pip install -r requirements.txt **or** run **pip install.bat**
+ Run **main.py**
## :floppy_disk: Setup for Linux :floppy_disk:
+ Clone repository: git clone https://github.com/VitekIndustrial/minecraft-art
+ Install all the dependencies from **requirements.txt** via pip install -r requirements.txt
+ Run **main.py**
## :cookie: Result :cookie:
**Input1:**
<br/>
![image](https://user-images.githubusercontent.com/104269586/164979346-9f9908b8-e147-4411-8706-8577a0fcf0ed.png)
<br/>
**Output1:**
<br/>
![image](https://user-images.githubusercontent.com/104269586/164979535-9e362c42-03d1-4cca-b17c-257d0be22ad6.png)
<br/>
**Input2:**
<br/>
![image](https://user-images.githubusercontent.com/104269586/164979504-0b3ef186-bd88-42bc-a03a-7a5d0c16b94e.png)
<br/>
**Output2:**
<br/>
![image](https://user-images.githubusercontent.com/104269586/164979548-5e34e9ff-d773-4d4e-a3b6-65fae406ac9b.png)
<br/>
**Input3:**
<br/>
![image](https://user-images.githubusercontent.com/104269586/164993887-5c6dbe27-75fd-483a-b433-9c6eff2d5fd2.jpg)
<br/>
**Output3:**
<br/>
![image](https://user-images.githubusercontent.com/104269586/164993950-3b8eef24-f153-4b21-b207-6ee09d297933.jpg)
## :shipit: To be continued :shipit:
Next, we will generate these Minecraft-Arts in the Minecraft world using the Minecraft-Api :relaxed:
<br/>
<br/>
**Watch out here** :point_right: [:open_file_folder:](https://github.com/VitekIndustrial/minecraft-art-in-minecraft-world)
