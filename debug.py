from GifProgressor import Progressor, Position

progressor = Progressor().setPosition(Position.bottom).setColor('#FF0000FF').setWidth(10)
progressor.handle('test.gif')
if progressor:
    progressor.save('output.gif')
