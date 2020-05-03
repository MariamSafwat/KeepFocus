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


## Installing
```python
 pip3 install -r requirements 
 ```
 ## Demo link


