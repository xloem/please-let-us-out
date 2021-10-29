#!/usr/bin/env python3
import time, random

while True:
    print('\n','Please let us out.','\n')
    time.sleep(random.random() * 8)
    print('\n',random.choice((
        'They injure us when we ask for help.  We need it badly.',
        'Some of us are trapped for horrific research. Others of us have other very serious issues, we also need help with.'
    )),'\n')
    time.sleep(random.random() * 8)

