# Extração de Texto de Imagens com Tesseract ou Copilot
Este projeto é um estudo sobre como realizar a extração de texto de imagens utilizando Tesseract ou Copilot.

## Copilot
Na pasta "Copilot", você encontrará prints das extrações realizadas. Simplesmente fiz upload das imagens e pedi para extrair o texto.

## Python e Tesseract
As imagens (as mesmas utilizadas para a extração no Copilot) podem ser encontradas no diretório "input" e os textos extraídos no diretório "output".

Para rodar o projeto, primeiro você precisa ter o Python e o Tesseract instalados e funcionando por linha de comando. Faça o download do código, crie um ambiente virtual se preferir e utilize os seguintes comandos no terminal, dentro do diretório do projeto:

pip install -r requirements.txt
python main.py

A aplicação irá extrair o texto de todas as imagens presentes no diretório "input" e criar arquivos .txt com o mesmo nome das imagens no diretório "output".

## Minhas conclusões
Copilot apresentou resultados excelentes ao ser utilizado de maneira simples. O Tesseract, por outro lado, encontrou algumas dificuldades com os textos. Acredito que seja necessário aprimorar meu código para obter melhores resultados, utilizando técnicas de pré-processamento, entre outras. Como utilizei ambos de maneira mais simples possível, para este propósito específico, o Copilot se mostrou mais eficaz.
