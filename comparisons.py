
import webbrowser
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
a = input().strip()

try:
    if int(a) > 0:
        print(True)
    else:
        print(False)

except ValueError:
    print('This is what you deserve!')
    webbrowser.open(url)
    input('press any key and have a nice day =)')
    
    
    
        