from PIL import Image
import pytesseract


def extract_txt(image_path):

    """it extracts the text from image and count the related words for each application

    Args:
        image_path (str) : the path of the image

    Returns:
        found (dict) : a 'dict' where the 'key' is the application name and the 'value' is 
                       the no. of words found in the image related to that application

    """
    
    # Create an image object of PIL library
    image = Image.open(image_path)

    # pass image into pytesseract module
    image_to_text = pytesseract.image_to_string(image, lang='eng')

    num = count_occurrence (image_to_text , ['facebook',"Facebook","Pages","post", "Like","Share", "Comment"])
    
    found = {}
    found["Facebook"] = num

    return found

def count_occurrence(text,related_words):

    """it counts no. of occurence of each word in the related words list

    Args:
        text (str) : text to search in
        related_words (list) : list of words to search for

    Returns:
        count (int) : summation of the no. of occurrence of the related_words

    """

    count = 0

    for word in related_words:

        count += text.count(word)
    
    return count

print(extract_txt('images/Shot1.png'))