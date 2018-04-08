
# Stenography Hacks

### stegchris1

The first approach I made was to simply store the encoded message in the red field. This was reliable and easy to implement, however it made it very obvious that the image was modified.

![Unmodified Image](https://cdn-images-1.medium.com/max/3600/1*VMqbhcWBDkwII0rVr7fDLQ.jpeg)
*Unmodified Image*

![Modified Image](https://cdn-images-1.medium.com/max/3600/1*4dKLhP7l4nN-bRRDOLdiaw.png)
*Modified Image*

Using [this script](https://github.com/chnakamura/cmsc389R-computer-vision-messaging/blob/master/stegchris.py), the image was encoded and decoded as follows (it worked with emojis too!)

    **$ python stegchris2.py -f bitcamp.png -m test.txt
    $ python stegchris2.py -f bitcamp.png**
    To be fair, you have to have a very high IQ to understand Rick and Morty. The humour is extremely subtle, andwithout a solid grasp of theoretical physics most of the jokes will go over a typical
    ...

### stegchris2

![Modified image](https://cdn-images-1.medium.com/max/2000/1*-qhliO8tcwYfGIbEbCwvhA.png)
*Modified image*

Next, I wanted to see if I could make it a little less obvious that the image had been modified. I decided that I could try only modifying transparent fields in the image, this way it would not be obvious when you simply looked at the image that it had been modified. This is done in [this script](https://github.com/chnakamura/cmsc389R-computer-vision-messaging/blob/master/stegchris2.py).

While this was is much less detectable, it requires that there are enough transparent pixels in order to fit the entire message you would like to encode.

### stegchris3

![Incrementing coordinates by 1](https://cdn-images-1.medium.com/max/2000/1*YByRVJroWR0eU7ZtPNzcUQ.png)
*Incrementing coordinates by 1*

![Incrementing coordinates by 4](https://cdn-images-1.medium.com/max/2000/1*YlxwDcuECPKZidhgDLeCrg.png)
*Incrementing coordinates by 4*

The script is [here](https://github.com/chnakamura/cmsc389R-computer-vision-messaging/blob/master/stegchris3.py).

In order to make the modification less obvious. I thought that instead of incrementing through each pixel, I could increment by a larger number. This would spread the modified pixels out, and perhaps it harder to notice that the image had been modified. Notice on the above image that incrementing every pixel produced a green stripe on the left side. This is not produced on the bottom image, where I instead modified every the first pixel in each 4x4 section.

This method does produce interesting artifacts in the image. While it is not quite as obvious as a large green stripe, if an hacker was looking for stenographic encoded messages this would be pretty obvious.

![The polka-dot pattern.](https://cdn-images-1.medium.com/max/2000/1*GjrydGYo8flmQQNdF6Ix7Q.png)*The polka-dot pattern.*

### stegchris4

I decided to try to make something a little bit more sophisticated. So I created the stegchris algorithm. Very advanced, made by an undergraduate with 5 hours of stenography experience! You can look at my final script [here](https://github.com/chnakamura/cmsc389R-computer-vision-messaging/blob/master/stegchris4.py), and an explication of how it works [here](https://github.com/chnakamura/cmsc389R-computer-vision-messaging/blob/master/writeup.pdf)!
