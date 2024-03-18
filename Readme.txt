# My Personal Homepage
#### Video Demo: https://youtu.be/MQRm1fo0kpg
#### Description:
This project follows a similar concept of a blog with 6 html files and 1 Css background adapted online that is integrated into 1 web app.
There are 4 different website format which are Homepage.html, (Introduction,whatamIdoing,Hobby).html, Diary.html and Writenew.html. Jinja2 was used to better facilitate the making of the webpage. Bootstrap was also used as the CSS due to it convenience with its container function.

1. Css background:
I have learned that adapting background from another website requires a code conversion usually. The more common one is Sass to CSS. Even though there is a great similarity between these 2 codes, Sass is used due to its less of a hassle to use this language rather than CSS.

As brackets are ommitted in Sass. I have also edited the CSS code for the background which enables me to cover the entire webpage and a written script to change the direction at 45 degrees angle of the stars everytime the webpage got refreshed.

I have made use of math random and a list which state the 4 angle changes that math random could randomized from. The number of stars could be managed by the number of "div=stars" that is indicated in the webpage.

The maximum number of stars the background can cater is 50, as each stars is set to fall at a certain timing. For example:
    .star:nth-child(1) {
      --star-tail-length: 7.26em;
      --top-offset: 9.26vh;
      --fall-duration: 9.114s;
      --fall-delay: 7.099s; }
    .star:nth-child(2) {
      --star-tail-length: 5.28em;
      --top-offset: 5.24vh;
      --fall-duration: 8.295s;
      --fall-delay: 6.336s; }

Star-tail length: em-->Relative to the font-size of the element
top-offset: position of the stars
fall duration: how long does it takes to travel the page
fall-delay: duration before the animation starts.

So with the different star-tail-length, top-offset, fall duration and fall-delay, mulitple stars on the webpage mimics the real life action of shooting stars as the stars shoots down at different timings.


2. Homepage.html:
It features my profile picture and also 4 different buttons that has styling from bootstrap that navigate to all my other pages that I used the Card format from bootstrap. It is also centralized using the justify content-center function.


3. Introduction,WhatamIdoing,Hobby.html:
It features a write up of the content which is self explanatory by the title of the page. It has the same web design for all that consist of 4 buttons that has styling from bootstrap to navigate to other pages. Containers within containers were used to organize the web content. As for the paragraphing, I have used row instead of <p> as the styling was bad, which row enables me to adjust the gap between each paragraph.


4. Diary.html:
It features a table that self update itself whenever a new post got submitted through Writenew.html, which the table is linked to a database that is linked using forward loop from jinja2/python that enables the ID, Content and Time/Date  from the database using db.execute from CS50 library.


5. Writenew.html:
It features a form for me to write on what I feel for the day and get redirected after pressing the post button to Diary.html, as it is set as "post" method. The form design uses the boostrap Css styling which was able to increase in size when the user writes more.