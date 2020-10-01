#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sinteseVoz3.py
#  Copyright 2017-08-22 tavares <tavares arroba  cadernodelaboratorio.com.br>
#  0.1
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#   
#  
import os
import num2words
import serial



def leSerial():
    if self.portaSerial.isOpen():
        while self.portaSerial.inWaiting() > 0:
            caracLido = self.portaSerial.read(1)
            
      



def main(args):
    inicio_cmd= 'espeak -vpt+f4 -g10 --stdout  '
    fim_cmd= ' | aplay' 
    total_leituras= 10
    
    idPorta= "/dev/ttyACM0"
    
    try:
        portaSerial = serial.Serial(idPorta,38400,timeout=10)   
  
    except serial.SerialException as e:
        msg = " Impossivel_abrir_porta__Vou_fechar_o_programa"
        os.system(inicio_cmd + msg + fim_cmd)
        sys.exit(1)     
         
    msg = "Operando_na_porta_" + idPorta
    os.system(inicio_cmd + msg + fim_cmd)
    
    comando = "1\n".encode()
    portaSerial.write(comando)
    stringLida= portaSerial.read(15).decode()

    
    if stringLida == "$1,Voltmeter 1.":
        strId= "Voltimetro_caderno_1.0"
    else:
        strId= "Hardware_não_identificado"
    os.system(inicio_cmd + strId + fim_cmd)
    
   
    for nIndice in range(total_leituras,-1,-1): 
        comando = "2,0\n".encode()
        portaSerial.write(comando)
        stringLida= portaSerial.read(10).decode()
        valor = stringLida.split(',')[-1]
        valor_atual = num2words.num2words(int(valor),lang='pt_BR') 
        os.system(inicio_cmd + valor_atual.replace(' ','_') + fim_cmd)
    
    
    os.system("espeak -vpt --stdout 'Fim de demostração' | aplay" )
    
    
   
    if portaSerial.isOpen():
        portaSerial.close()
   
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
