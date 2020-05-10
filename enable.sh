#!/bin/sh

#opkg install --force-depends kmod-p44-ledchain_4.14.81\+2.0-7_mipsel_24kc.ipk

#rmmod p44-ledchain

omega2-ctrl gpiomux set pwm0 pwm

#insmod /lib/modules/4.4.61/p44-ledchain.ko ledchain0=0,100,1
insmod /lib/modules/$(uname -r)/p44-ledchain.ko ledchain0=0,100,1

 cat /dev/ledchain0
