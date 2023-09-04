# CS50x Final Project: Linkbits - URL shortener

## Video Demo Link

https://youtu.be/ZGU58UKLukY

## Description

### Overview
Linkbits is a responsive, mobile-first URL shortener web application. It usesthe  Bootstrap CSS framework and the Flask 
web app framework. Linkbits was created in fulfillment of the final project for CS50x.

### app.py
`app.py` contains a bunch of imports and routes. The home/index route supports GET and POST. 

URL shortening in the `"/"` route only works with POST. URL shortening uses the shrtcode API. The API doesn't require 
any authentication. The long url is validated in `index.html` before being passed to the API. The response received in 
json is returned to `index.html` to render the short URL.

The `"/faq"` route handles the FAQ.

View the shrtcode API docs [here](https://shrtco.de/docs).

### layout.html
`layout.html` is the base page template. It contains the shared parts of the web app like the navbar. It also contains 
the references to the CSS file, scripts, favicons, and so on. 

### index.html
`index.html` is the homepage. It contains a responsive  "banner" on top. In smaller-width viewports, the image in the 
"banner" is hidden to streamline the webpage.

The container where the long url is inputted is also responsive. The form validates the inputted text as url.

The result card is contained inside a block tag which only shows up once a short url is returned from `app.py`. The 
short url can be copied to the clipboard using a button which uses javascript.

### faq.html
`faq.html` uses Bootstrap's accordion to make responsive, collapsible content. 

### Built with
* HTML
* CSS
* Javascript
* Flask
* Bootstrap

### Author
Manuel Parcon - [Email me](mailto:mceparcon@gmail.com)