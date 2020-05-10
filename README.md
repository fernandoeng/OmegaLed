# OmegaLed

OmegaLed Controller is a very small project of mine.

## Background

I have recently bough a computer case with some RGB leds in it, the [Hummer MC Pro](https://www.pcdiga.com/caixa-atx-nox-hummer-mc-pro-argb-branca) just like this one [Hummer MC](https://www.nox-xtreme.com/en/product/hummer-mc-zero-edition/146/) but with RGB lights, but the light effects are very limited with the stock controller, you have 7 colors to chose from, with 2 options each, static or breathing, a static and changing rainbow, and two more strange effects.
So, I have a couple of Onion Omega 2 laying around, and i've decided to use them to control the RGB strips in my computer case.


## Installation
I'll have to install the p44 ledchain driver for your current linux kernel
> opkg install --force-depends kmod-p44-ledchain_4.14.81\+2.0-7_mipsel_24kc.ipk

Enable the pwm one the Omega
>omega2-ctrl gpiomux set pwm0 pwm

Insert the module
> insmod /lib/modules/$(uname -r)/p44-ledchain.ko ledchain0=0,100,1

To see if everything is ok, run:
> cat /dev/ledchain0

##Use

Start the remote.py script
> python remote.py

Go to the address of your Omega with a browser using the port 8888, like http://omega-dead:8888/ and a very simple web page should load.
