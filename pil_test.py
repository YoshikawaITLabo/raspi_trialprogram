from PIL import Image, ImageDraw, ImageFont
from rgbmatrix import RGBMatrix, RGBMatrixOptions

# LEDマトリクスの設定
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 3
options.parallel = 2
options.hardware_mapping = 'regular'
options.disable_hardware_pulsing = True
options.gpio_slowdown = 4
matrix = RGBMatrix(options = options)

# テキストをレンダリングするイメージを作成
image = Image.new('RGB', (64, 32))
draw = ImageDraw.Draw(image)

# テキストをレンダリングするイメージを作成
c = Image.new('RGB', (64, 32))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('/home/kazuhiro/Downloads/sazanami-20040629/sazanami-gothic.ttf', 15)

# 複数の色を含むテキストをレンダリング
draw.text((0, 0), 'こんにちわ', fill=(255, 0, 0), font=font)
draw.text((30, 0), '世界', fill=(0, 255, 0), font=font)

# イメージをLEDマトリクスに表示
matrix.SetImage(image.convert('RGB'))