import pyscreenshot as ImageGrab
from sys import platform

# import linux module
if platform.startswith('linux'):
     import notify2
#import win10 module
elif  platform.startswith('win') and platform.release() == '10':
    from win10toast import ToastNotifier

def takeScreenshot ():
    
    """When called it returns an image object with the screenshot.

    Args:
        None.

    Returns:
        im (image object) : contains the screenshot 
    """

    im = ImageGrab.grab()
    return im



def sendNotification(title, message):

    """it sends Notification using system api, compatible with win10 and linux

    Args:
        title (str)   : the title of the Notification
        message (str) : the body of the Notification

    Returns:
        None

    """

    if platform.startswith('linux'):
        notify2.init('')
        n = notify2.Notification(title, message)
        n.show()
    
    elif platform.startswith('win') and platform.release() == '10':
        n = ToastNotifier()
        n.show_toast(title, message)

