import bmp
import fractal

pixels = fractal.mandelbrot(448, 256)

bmp.write_grayscale('../../tmp/mandel.bmp', pixels)
