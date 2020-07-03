# OCR
### Optical Character Recognition:Extracting Text From Images,Textract


[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

### Sample Input
![alt text](https://github.com/sarnesh444/OCR/blob/master/ORMtoSQL.JPG)

### Sample Output
![alt text](https://github.com/sarnesh444/OCR/blob/master/output.JPG)

## Tools used

* [Pytesseract](https://pypi.org/project/pytesseract/) a python package that is centric to OCR.

* [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) pytesseract runs with tesseract under the hood.

* [Open CV](https://opencv.org/) a computer vision python library.

## Prerequisites

This repo assumes you use Python 3.x.

### Dependencies
Install the dependencies using PIP the package manager for python
Make sure the streamlit version is above 0.49.0
```
pip install pytesseract
```

### Guidelines
* Navigate to [this](https://github.com/UB-Mannheim/tesseract/wiki) website
* Download the one that suits your sys-architecture
* Find a path like ProgramFIles/Tesseract-OCR/tesseract.exe
* Only after this the file shall execute else you can run into errors


### Additonal

* Color to Black,Gray
  * It's is observed that Tesseract performs better when the image is in black and white.
  * [This](https://github.com/sarnesh444/OCR/blob/master/color_to_bq.py) file mananges to achieve this converts color to black,gray image
  * Sample Input
  ![alt text](https://github.com/sarnesh444/OCR/blob/master/test.JPG)
  * Sample Output
  ![alt text](https://github.com/sarnesh444/OCR/blob/master/colors.JPG)
  
  
* Color to Image with white background and black font
  * It's is observed that Tesseract performs even better when the image has a white background with black font
  * [This](https://github.com/sarnesh444/OCR/blob/master/change.py) file mananges to achieve this converts color image to the one with white bg and black font.
  * Sample Input
  ![alt text](https://github.com/sarnesh444/OCR/blob/master/cbv_template_contextdict.JPG)
  * Sample Output
  ![alt text](https://github.com/sarnesh444/OCR/blob/master/result.png)
  
### Future Work

#### The objective is to create a chrome extension for OCR
##### Many times when watching a code explanation video the host might forget to give a link to the source code which will force the listener to type the code all over again
##### not yielding much result.
##### With "Textract" I would like to convert this into a chrome extension thereby enabling learners to extract text from video directly thereby removing the hassle of writing code again.
![alt text](https://cdn.systweak.com/content/wp/systweakblogsnew/uploads_new/11-Best-Google-Chrome-Extensions-You-Must-Have.jpg)

* The work is currently in progress check the progress [here](https://github.com/sarnesh444/OCR/tree/master/OCRChrome)

## Contributing

If you found any mistakes in my code, or if you can enhance the quality of documention, please feel free to contribute!
Here are 3 steps to contributing.

1. [Fork](https://github.com/sarnesh444/IndianNumberPlateDetection/fork) this project.
2. Commit your changes.
3. Create a new Pull Request and link an [issue](https://github.com/sarnesh444/IndianNumberPlateDetection/issues/new) with it.

## Meta 

| Name | Github | LinkedIn | E-mail | Phone|
| --- | --- | --- | --- | --- |
| Saranesh ManiRatna.K | [@saranesh](https://github.com/sarnesh444) | [@saranesh](https://www.linkedin.com/in/saranesh-kanumuri-17a7a5181/) |[E-mail](mailto:sarnesh444@gmail.com) | [(+91) 8500717519](tel:+918500717519)

#### This project is NOT meant for production and hasn't been tested thoroughly.


