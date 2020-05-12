# KeepFocus
Desktop application user tracking, help to understand where your time goes. 

## How it works
1. The program takes screenshots regularly.
2. Image processing and text extraction by <br />
● extract_text.py: it extracts text and compares it with data in database<br />
● image_segmentation.py: it compares screenshot with images in database.<br />
3. Record the user activities during the day and give detailed reports and an accurate
picture of how you spend your day.

## Packages used
1. Database: Sqlalchemy <br />
2. Image segmentation: opencv <br />
3. Text extraction: pytesseract<br />
4. GUI: PyQt5

## prerequisite
### Installations for pytesseract :
 #### On Linux
```python
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
```
#### On Windows

1. You need to have Tesseract OCR installed on your computer.<br>
   get it from here. https://github.com/UB-Mannheim/tesseract/wiki <br>
   Download the suitable version.
2. Add Tesseract path to your System Environment. i.e. Edit system variables.

## Installing
```python
 pip3 install -r requirements 
 ```
 ## Executing program
 ``` 
 python main_gui.py
 ```
 ## Team Members
 ``` 
 1. Marina Fares.<br>
 2. Mariam Safwat. <br>
 3. Merna Raouf. <br>
 4. Nader Nabil. <br>
 5. Mina Atef.<br>
 ```
 ## Demo link

https://youtu.be/SkK6Z2_8CxI

