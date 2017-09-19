This program can monitor a Chinese A-stock. It alarms you when the tracked stock hits a record high, or drops below your tolerable price. It currently can support only one tracked stock. More features are still under development. To execute the program, type the following command:

**python monitor.py XXXXXX**

where XXXXXX is a 6-digit stock tick number. If you haven't tracked this stock before, it will ask you for a buy price. Then it will read data from the web and keep track of how price is changing compared to your buy price. If the price goes up, it will play a happy sound. If price drops below your preset tolerable loss price, it will play an alarm. This program is a handy gadget to have running in the background, so that you can work on other things while getting notified how your stock is behaving! The program will write the history into a text file inside the *data* folder named after the stock tick number. 
