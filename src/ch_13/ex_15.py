# Launching a web browser
import webbrowser
#
# webbrowser.open('http://www.python.org')
#
# # Open the page in a new browser window
# webbrowser.open_new('http://www.python.org')

# To open the page in a specific browser
c = webbrowser.get('firefox')
c.open('http://www.python.org')
c.open_new_tab('http://docs.python.org')

if __name__ == '__main__':
    pass
