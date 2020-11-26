# Days 01-03 Dealing with Datetimes

Datetimes. The bane of our existence as coders (or at least for me anyway!).

## Day N: Learn the basics of datetime and date

A super basic day to get started. I will walk through the basics of datetime, starting with datetime and date then moving onto timedelta.

After learning, use your Python shell to play around with some timestamp calculations.

## Day N+1: Getting into The Python Standard Library

The [datetime](https://docs.python.org/3.2/library/datetime.html#module-datetime) module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation. For related functionality, see also the [time](https://docs.python.org/3.2/library/time.html#module-time) and [calender](https://docs.python.org/3.2/library/calendar.html#module-calendar) modules.


## Day N+2: My Turn!

I've got the basics down so now create something!

A fun project would be to create yourself a Pomodoro Timer that incorporates datetime rather than just the time module.

---

### Pomodoro Technique - [see](https://en.wikipedia.org/wiki/Pomodoro_Technique)

![plan](https://user-images.githubusercontent.com/12321741/72369481-459b5180-3711-11ea-9bb6-e6eed7a4a1e4.jpg)

### It is important:
**According to the principle of the Pomodoro technique - if you are
distracted while doing work, then you must interrupt the current time
and start a new Pomodoro. And this means that you need to write time in to
the database only after the specified time has passed and not earlier.**

**If you follow this principle, the Pomodoro Technique will be for you exactly 
the tool for which it was invented, namely, not to calculate the time of your 
work and breaks in work, but to make you concentrate on continuous and 
concentrated execution of works during one Pomodoro, i.e. within 25 minutes.**

---

I was originally hung up on trying to make the pomodoro class run asynchronous to allow input from a user (e.g. pause/restart the timer). Taking a step back, asynchronous functionality only increases the complexity of this problem. It didn’t need to be there. Keep things simple, stupid.

I have a tendency to want to build the perfect solution right out of the gate. It’s not sustainable and not reality . The aim should be to build a MVP (minimum viable product) and iterate as required.

I’m happy on where I landed with things.

Have fun!