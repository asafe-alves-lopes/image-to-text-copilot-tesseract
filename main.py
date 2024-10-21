import os
import pytesseract
from PIL import Image

inputDir = 'input'
outputDir = 'output'

def returnFullPathToInput(input):
    return inputDir+'/'+input

def returnFullPathToOutput(input):    
    return outputDir+'/'+returnFileNameWithAnotherExtenstion(input, 'txt')

def returnFileNameWithAnotherExtenstion(fileName, extension):
    return fileName.split('.')[0]+'.'+extension

inputs = os.listdir(inputDir)

for input in inputs:
    image = Image.open(returnFullPathToInput(input))
    text = pytesseract.image_to_string(image)
    arquivo = open(returnFullPathToOutput(input), "w")
    arquivo.write(text)
    arquivo.close()