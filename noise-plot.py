import matplotlib.pyplot as plt

y = [0.5] * 10
x = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]

plt.plot(x, y, 'r')
plt.scatter([100, 98.5, 95, 90], [0.5933333333333334, 0.5933333333333334, 0.5466666666666666, 0.4866666666666667], s = [120] * 4)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)

#plt.ylabel('Accuracy', fontsize=40)
#plt.xlabel('Cosine Similarity', fontsize=40)
#plt.title("Cosine Similarity of Noised Embeddings vs. WinoDict Accuracy")
plt.savefig('noise_image.png', bbox_inches='tight')