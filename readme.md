# Introduction

I have a water level sensor positioned in the irrigation canal that I use to water my Acre. I have setup an Arduino controller with an XBee wireless interface in my pump shed. This controller senses the level of water in the ditch, and the level of water in the pump sump. 

The controller has the ability to turn on the two zones (North and South), as well as the 1.5HP pump. 

# ditchd

I run a ditch daemon that reads the controller status often (5 second intervals). This status is then logged to redis.

Commands to the ditchd can be sent via redis also. The ditchd checks the redis status 2 times a second, so pump and zone commands are executed quickly. 

## API
The Ditchd connects to the local wireless XBee via serial. So, this process much run at my house. I use a simple serial interface, which I should update to a binary interface for performance reasons..


# Ditch Celery

I worked on a version of this controller that uses Celery as the task queue. 

I had a celery server on my home machine, a celery server on an AWS web server, and I ran a celery beat process that updated the database and web site.

This system did not work reliably, mostly due to my limited understanding of Celery. The problem I faced was that the celery queue would fill up, and things would just hang up. I might re-visit that someday, just so that I can get more familiar with Celery.

