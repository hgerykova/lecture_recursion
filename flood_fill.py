import matplotlib.pyplot as plt


def flood_fill(image, x, y):
    image_shape = image.shape
    x_img, y_img = image_shape
    if x >= x_img or y >= y_img:
        return image
    if x < 0 or y < 0:
        return image
    elif image[x,y] == 0 or image[x,y] == 2:
        return image
    else:
        image[x, y] = 2
        plt.imshow(image, cmap="rainbow")
        plt.show(block=False)
        plt.pause(0.3)
        plt.clf()
        flood_fill(image, x+1, y)
        flood_fill(image, x-1, y)
        flood_fill(image, x, y+1)
        flood_fill(image, x, y-1)
        return image


def main():
    # img = plt.imread("files/img0.png")[:, :, 0]
    img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill(img, 0, 0)

    plt.imshow(img, cmap="rainbow")
    plt.show(block=False)
    plt.pause(3)
    plt.clf()


if __name__ == "__main__":
    main()
