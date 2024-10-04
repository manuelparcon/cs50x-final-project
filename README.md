# CS50x Final Project: Linkbits - URL shortener

## Video Demo Link

Video demo can be found using the link: https://youtu.be/ZGU58UKLukY

## Description

### Overview
Linkbits is a lightweight, responsive, and mobile-first URL shortener web application. It uses the  Bootstrap CSS framework and the Flask 
web app framework. Linkbits was created in fulfillment of the final project for CS50x.

My goals for this final project were pretty simple. As this is the first time I'm creating a web app from the ground up, 
the designs and features are basic, but I  wanted to touch on things that were covered in class like HTML, CSS, 
Javascript, Flask, and Bootstrap.

### app.py
`app.py` contains a bunch of imports and routes. The home/index route supports GET and POST. 

URL shortening in the `"/"` route only works with POST. URL shortening uses the shrtcode API. The API doesn't require 
any authentication. The long url is validated in `index.html` before being passed to the API so no other validation was 
added in this file. The wanted response received in json were selected and returned to `index.html` to render the 
shortened URL.

The `"/faq"` route handles the FAQ page, no GET or POST required.

For more information regarding the API used, view the shrtcode API docs [here](https://shrtco.de/docs).

### layout.html
`layout.html` is the base page template. It contains the shared parts of the web app like the navbar. It also contains 
the references to the CSS file, scripts, favicons, and so on. The whole page is responsive made possible by Bootstrap.

### index.html
`index.html` is the homepage. It contains a responsive "banner" on top. In smaller-width viewports, the image in the 
"banner" is hidden to make the webpage more streamlined. Responsiveness also made possible by Bootstrap.

The container where the long url is inputted is also responsive. The "Shorten Link" button auto adjusts and moves down a
row to occupy the whole column when viewport is small. As mentioned earlier, the form validates the inputted text to make sure it's a url.

The result card is contained inside a block tag which only shows up once a short url is returned from `app.py`. The 
short url can be automatically copied to the clipboard using the "Copy" button made possible by javascript.

### faq.html
`faq.html` uses Bootstrap's accordion to make responsive, collapsible content. 

### Built with
* HTML
* CSS
* Javascript
* Flask
* Bootstrap

### Author
Manuel Parcon
