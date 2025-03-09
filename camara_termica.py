import numpy as np
import matplotlib.pyplot as plt
ImagenTiff = np.array(plt.imread("c:\\Users\\andyh\\Downloads\\FLIR_00088.tiff"))
D = np.double(ImagenTiff)
temp_min = -40
temp_max = 160
NBits = 14
MatrizCenti = np.array((temp_max - temp_min)*D/2**NBits + temp_min)

fig = plt.figure("Imagen Termica")
plt.imshow(MatrizCenti, cmap = plt.cm.hot_r)

plt.colorbar(shrink = 0.92)
plt.figure("Histograma")
hist, bins = np.histogram(MatrizCenti, np.arange(0,temp_max), density=True)
histoTempBar = np.int32(MatrizCenti.round())
plt.hist(histoTempBar,5,facecolor = 'red', alpha = 0.5)
plt.show()