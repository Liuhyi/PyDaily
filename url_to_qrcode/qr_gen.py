import qrcode


class Solution:
    def __init__(self, url):
        self.url = url

    def qr_gen(self):
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(self.url)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save('qr_img.png')


if __name__ == '__main__':
    url = "http://www.python.org/"
    s = Solution(url)
    s.qr_gen()
