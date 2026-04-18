# Message in a Bottle Application 

## Project Description
This application allows users to get inspired by others by receiving a bottled message every 15 minutes that was sent by another random other user. 
It is built on the idea of real life bottled message practices. The goal is to get inspired or motivated by someone else's message. 
The application consists of 5 pages. One where users receive a bottled messaged sent by another user every 15 minutes (including a timer), 
a 'Send' page where one can type up and send a message through a form for other users to be received, a 'History' page listing the last 10 submitted messages as a record, an simple
'About' page detailing the goal and mission of the application, as well as a 'Contact' page where users are invited to send the creators any feedback.

## Features

#### Feature 1: Receive a message from another user
This feature allows users receive messages submitted earlier by other users.

#### Feature 2: Timer for next message
A timer feature has been built in on the landing page so that users know when they are to receive the next bottled message from the messages that are queued up.

#### Feature 3: Send a new bottled message 
The message that is submitted through the form on the 'Send' page end up being added to the messagebank.json file in the data folder.

#### Feature 4: Contact form 
A contact form has been implemented encouraging users to leave feedback for the betterment of the application. The email address needs to adhere to the
email address format or else it does not go through. Once it is submitted, a thank you message is displayed containing the name of the user who just
submitted feedback to make it more personal.

## Design choices

#### Colours
I chose these colors for the project due to the fact that at the very start I chose my own photograph as the background, so I based all my decisions re
colours so that it matches the hue of the background photo. I kept good accessibility, good balance, and of course user engagement in mind. Pastel
colours nicely seem to match the background. 

#### Fonts/Typography
I chose these this font as I did not want to overcomplicate and make the visuals overly crowded and overwhelming as I chose a background photo already. My idea was to go with a simple font to minimise visual noise. 

#### Images/Graphics
The background image is my own and I decided to base all my styling decision on the hue of the image. The only other image is the bottle image on the
landing page which I chose as it conveys playfulness.

## Development Process

#### Project planning
At the outset I was certain that I will need to pages: one for receiving and one for submitting bottled messages. The additional 3 pages were developed
at a later stage following best practices I came across in other applications and websites. Throughout the design stage I needed to find the best way to
store and queue messages that were submitted by users that will eventually be sent to other users. I ended up implementing that feature, the most 
essential feature of the app by using json. Please see messagebank.json for reference. 


#### Challenges Faced
The biggest challenge I faced was when I had to find the best way to store and queue messages that were submitted by users that will eventually be sent to other users. I ended up implementing that feature by using a json file that workes just perfectly for this purpose. At this stage I also came to realise that I would need presubmitted bottled messages queued up as well so I generated 96 of them using an AI chatbot to save hours of work.

#### Interactivity
I made the app interactive by using JavaScript to add dynamic visual effects and real-time updates. First, I used an event listener that waits for the
page to fully load before running the code. Once loaded, the message box fades smoothly into view by changing its opacity from 0 to 1 with a transition
effect, which creates a more engaging user experience.
I also added a countdown timer that updates every second using setInterval(). The timer starts at 900 seconds (15 minutes) and automatically converts
the time into minutes and seconds for display. It updates the text on the page in real time to show users when the next bottle will be available. When
the countdown reaches zero, it resets automatically to 3600 seconds (1 hour), allowing the timer to continue running without needing to refresh the page.
These JavaScript features make the app feel more interactive, responsive, and user-friendly by adding animation and live content updates.

#### Interactivity: Python specific description
I used Python with the Flask framework to make the page more advanced, functional, and interactive by adding backend features that go beyond what HTML,
CSS, and JavaScript can do alone. Flask allowed me to create multiple pages such as the homepage, submit page, about page, contact page, and history
page using routes. This gave the website a structured navigation system and made it feel like a complete web application.
I also used Python to handle user-submitted messages. When a visitor writes a message and submits the form, Python collects the input, stores it in a
list, and saves it permanently in a JSON file. This means messages are not lost when the page refreshes or the server restarts. It allows the app to
keep growing with new user content over time.
Another feature I built with Python was the time-slot message system. I divided the day into 15-minute intervals and assigned each message to a slot.
Depending on the current time, Python automatically selects which bottled message should appear on the homepage. This makes the website feel dynamic
because the displayed message changes throughout the day.
I also added a history feature where Python retrieves the last ten messages and displays them on a separate page. This gives users access to previous
content and encourages more engagement with the app.
Finally, I used Python to process the contact form, where the website accepts the user’s name and displays a personalised response. Overall, Python made the page smarter by handling data storage, user input, page routing, and time-based content updates, turning a simple webpage into a fully working
interactive application.

## Deployed site

This site has been deployed to GitHub Pages at the URL below:

ADD LINK HERE