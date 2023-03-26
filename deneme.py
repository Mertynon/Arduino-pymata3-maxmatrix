from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import maxmatrix


board = PyMata3(com_port='com5')
DIN, CLK, CS =7,5,6
mm = maxmatrix.MaxMatrix(board, DIN, CS, CLK)
#example 1
ts = maxmatrix.Tileset()
sprite = ts.get_sprite("D")
mm.write_sprite(sprite)



#example 2
#mm.set_column(0, 0b00000000)
#mm.set_column(7, 0b00000000)
#mm.set_column(6, 0b00000000)
#mm.set_column(1, 0b00000000)
#mm.set_column(5, 0b00000000)
#mm.set_column(2, 0b00000000)
#mm.set_column(4, 0b00000000)
#mm.set_column(3, 0b00000000)
