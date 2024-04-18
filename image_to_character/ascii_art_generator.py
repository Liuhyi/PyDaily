from PIL import Image


class Solution:
    def __init__(self, path, output_width=100, characters="@#$%^"):
        self.output_width = output_width
        self.characters = list(characters)
        self.image_path = path

    def image_to_character(self):
        image = Image.open(self.image_path)
        width, height = image.size
        ratio = height / width
        output_height = int(self.output_width * ratio)
        image = image.resize((self.output_width, output_height)).convert('L')
        pixels = image.getdata()
        gap = 256 // len(self.characters)
        output_characters = []
        n = len(self.characters)
        for pixel in pixels:
            index = pixel // gap
            if index >= n:
                n -= 1
            output_characters.append(self.characters[index])
        return output_characters

    def character_to_txt(self, output_characters):
        with open('output.txt', 'w') as f:
            for i in range(0, len(output_characters), self.output_width):
                end = i + self.output_width
                if end > len(output_characters):
                    end = len(output_characters)
                f.write(''.join(output_characters[i:end]) + '\n')

    def run(self):
        self.character_to_txt(self.image_to_character())


if __name__ == '__main__':
    solution = Solution("input.png", 200, "qwertryty")
    solution.run()
