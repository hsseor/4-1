import numpy
from scipy.special import erfc
import matplotlib.pyplot

snr_db = numpy.arange(0, 32, 2)
snr = 10**(snr_db/10)
ber = 0.5*erfc(numpy.sqrt(snr))

matplotlib.pyplot.semilogy(snr_db, ber, 'bo-')
matplotlib.pyplot.xlabel('SNR(dB)')
matplotlib.pyplot.ylabel('BER')
matplotlib.pyplot.title('P(e) plot of AWGN channel')
matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()

//snr=0db~30db까지 각 2db 간격으로 snr에 따른 p(e) plot 해보기
