# Plant soil moisture meter with automated notifications

I've created an app that would read moisture metrics from a moisture sensor inserted into a plant's pot.

Since i don't have any hardware connected yet, this app currently only simulates readings from a moisture sensor. 

The moisture units here are taken from a [moisture sensor tutorial](https://www.youtube.com/watch?v=M3RuHX6jEXI&ab_channel=Data36-OnlineDataScienceCourses)

The units are unknown but they [relate to resistance of the soil](https://arduino.stackexchange.com/questions/74679/what-are-the-units-of-output-of-soil-moisture-sensor)


This seonsor also measure soil temperature, so i created this in a way that it would also record the temperature.


My initial idea was to run the function that reads the soil metrics every hour and records the metrics into a file 'plat_history.csv'
If the metrics from a sensor are not optimal for the plant it sends an email and plays a song to notify the user. The song is only played if it's daytime.
you can also see plant's moisture history in a pdf line chart, change the song that plays when something is wrong with soil enviroment, change the email address that notifications are being sent to, add or remove a plant to read the soil environment of. 



## In order for this to work you'll need to:

- **install these libs**

```
pip install pygame
```
```
pip install reportlab
```

- **to change the sender's email and password** in **inform_user/send_email.py send_email** function
