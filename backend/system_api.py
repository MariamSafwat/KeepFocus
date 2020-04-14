import pyscreenshot as ImageGrab


def takeScreenshot ():
    
    """When called it returns an image object with the screenshot.

    Args:
        None.

    Returns:
        im (image object) : contains the screenshot 
    """

    im = ImageGrab.grab()
    return im
