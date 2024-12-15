#pip install eel
import eel 

eel.init('Gui') #foulder name

@eel.expose

def app(): #app main function
    print('App running')
    
app()

eel.start('index.html',size=(500,600)) #runapp window