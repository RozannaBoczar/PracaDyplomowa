import cv2
import pytesseract


class TextReader:
    # read registration from found data on video
    def read_reg(self, img):
        text = pytesseract.image_to_string(img)
        reg = ""
        if len(text) <= 8:
            reg = text
        return reg


def test():
    # https://pl.wikipedia.org/wiki/Tablice_rejestracyjne_w_Polsce
    img = cv2.imread("images/image2.jpg") # works XDDDDDDDDDDDDDDDDDDDD
    text = pytesseract.image_to_string(img)
    print(text)


# test()
