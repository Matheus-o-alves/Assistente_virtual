#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sinteseVoz1.py
#  Copyright 2017-08-22 tavares <tavares arroba  cadernodelaboratorio.com.br>
#  0.1
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#   
#  
import os

def main(args):
    os.system("espeak -s120 -vpt+m7 --stdout 'Olá, eu sou o Téslá, seu assistente virtual.' | aplay")

    #    os.system("espeak -vpt+f3 --stdout 'Ola, eu sou o Tesla seu assistente virtual.' | aplay" )
   #espeak -vpt+f3 –stdout “Bem vindo ao site do caderno de laboratorio.” | aplay
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
