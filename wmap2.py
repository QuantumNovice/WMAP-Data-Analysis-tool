import matplotlib.pyplot as plt

def load():
    with open('wmap_tt_spectrum_9yr_v5.txt') as afile:
        lines = afile.readlines()

    line2 = []
    #print(len(lines))
    for line in lines[:]:
        if line.startswith('#'):
            lines.remove(line)
    for line in lines:
        line = line.strip()
        line = line.split(' ')
        while '' in line[:]:
            line.remove('')
        line2.append([float(i) for i in line])
    #print(len(lines))

    #print(line2[0])
    return line2

data = load()
labels = ['Multipole Moment', 'Power Spectrum in uK^2', 'Error derived from diagonal terms of Fisher matrix',
          'Portion of error attributed to measurement errors(uK^2)',
          'portion of error attributed to cosmic variance, assuming the best-fit LCDM model']

##j = 0
##x = [i[j] for i in data]
##y = [i[j+1] for i in data]
##plt.plot(x,y, '.')
##plt.xlabel(labels[j])
##plt.ylabel(labels[j+1])
##plt.show()
for j in range(4):
    x = [i[j+1] for i in data]
    plt.plot(x, label=labels[j])
    plt.legend()
plt.show()

