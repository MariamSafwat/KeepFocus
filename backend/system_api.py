import pyscreenshot as ImageGrab
import platform

# import linux module
if platform.platform().startswith('Linux'):
    import notify2
#import win10 module
elif  platform.platform().startswith('Windows') and platform.release() == '10':
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
    if platform.platform().startswith('Linux'):
        notify2.init('')
        n = notify2.Notification(title, message)
        n.show()
    
    elif platform.platform().startswith('Windows') and platform.release() == '10':
        n = ToastNotifier()
        n.show_toast(title, message)


if __name__ == "__main__":
    sendNotification("test message", "message")