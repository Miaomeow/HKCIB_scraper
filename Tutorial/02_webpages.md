# Anatomy of a webpage
## HTML
HTML is a programming language that defines the arrangement of the page elements. For example it can define the location of a picture, or what a [hyperlink](https://en.wiktionary.org/wiki/cat#/media/File:Gatto_europeo4.jpg) links to.

Here's a simple HTML sample, almost every single webpage stems from it:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>

        <h1>This is a Heading</h1>
        <p>This is a paragraph.</p>

    </body>
</html> 
```
You see that it has a nested structure. Each <b>element</b> is bounded by <b>a pair of tags</b>. Let's examine each component:
```html
<!DOCTYPE html>
```
It's the declaration of document type. 

```html
<html>
</html>
```
The html element bounds the beginning and the end of an html file.

```html
<head>
    <title>Page Title</title>
</head>
```
The head element contains elements that define the display of the webpage, they are usually invisible inside the webpage. For example, the title, the style, the meta information (e.g. author), the javascript location, etc.

```html
<body>

    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>

</body>
```
The body element contains in contrast the visible elements. They elements are displayed in the same order as they appear on the HTML document. Like this example you see the text in header h1 will appear before the text in paragraph p. The table element, a common tag we see in our targeted webpages, is also inside body.

## CSS
CSS is a style sheet for HTML documents. It describes how HTML elements are to be displayed on screen, or in other media, e.g. smart phones, tablets.

We attach the link to the CSS style sheet in the head element in an HTML document. Like this:
```html
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>

        <h1>This is a heading</h1>
        <p>This is a paragraph.</p>

    </body>
</html> 
```
The <b>attribute</b> rel specifies that "styles.css" has a stylesheet relationship with the current HTML document, whereas href (hyperlink reference) specifies the URL of the link.

Look at a sample CSS style sheet:
```css
body {
    background-color: powderblue;
}
h1 {
    color: blue;
}
p {
    color: red;
}
```
Essentially, CSS saves developers lots of time in styling. Although CSS has almost nothing to do with webscraping, you should know why it exists.

## Javascript
Javascript is a programming language that dynamically changes the content of webpages. It makes interactive webpages possible.

One famous example is Google Maps. The interactive buttons and displays you see are written in Javascript. See more examples in [here](https://www.w3schools.com/js/js_examples.asp).

It is so important to recognise a Javascript because there are so many buttons that we see, executes a Javascript after we click on it. In selenium the error rate of locating a button is much much higer than executing Javascripts! Therefore, we can build a more reliable bot by asking it to execute a Javascript than clicking a button.

Here's an example of a button that triggers javascript:
```html
<button onclick="myFunction()">Click me</button>

<p id="demo"></p>

<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Hello World";
}
</script>
```

```html
<button onclick="myFunction()">Click me</button>
```
The attribute <i>onclick</i> triggers the javascript function myFunction().

```html
<p id="demo"></p>

<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Hello World";
}
</script>
```
Javascript is embedded under the script tag. You can pack inifite amount of javascript functions inside.

In the example, the javascript changes the text inside <i>p</i> element with <i>id="demo"</i> to <i>Hello World</i>.

Usually we embed Javascript either in an external .js sheet and set a link to it in the head element, or we put the scripts at the bottom of an HTML, right above the html closing tag.

Disclaimer: All the sample codes are taken from www.w3schools.com.