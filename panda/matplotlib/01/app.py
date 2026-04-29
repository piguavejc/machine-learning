import matplotlib.pyplot as plt


def main():
    x = [4, 2, 7, 6, 3]
    plt.plot(x)
    plt.show()
    plt.savefig("grafica.png")


if __name__ == "__main__":
    main()
