#!/bin/sh /etc/rc.common
# OmegaLed script


START=10
STOP=15

start() {
        echo start

        omega2-ctrl gpiomux set pwm0 pwm

        #enable led chain
        rmmod p44-ledchain

        insmod /lib/modules/$(uname -r)/p44-ledchain.ko ledchain0=0,100,1

        if [ ! -f '/opt/OmegaLed/pid' ]; then
          python /opt/OmegaLed/remote.py &> /opt/OmegaLed/remote.log  &
          echo $! > /opt/OmegaLed/pid
        else
          echo "already running"
        fi
}

stop() {
        echo stop

        kill $(cat /opt/OmegaLed/pid)
        rm /opt/OmegaLed/pid

}

restart() {
        echo restart

        stop
        start
}

boot() {
        echo boot

        start
}
