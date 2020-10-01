/*
***********************************************
Nome do projeto:arduino_voltimetro.ino
Diretorio do projeto:/home/tavares/desenvolvimento2016/arduino_voltimetro
versao 1.0    31/08/2016

Este firmware implementa um voltimetro multicanal de seis canais.

Para diminuir o impacto da variacao  da tensao de alimentacao sobre o valor obtido no conversor AD, 
utiliza a tensao de referencia de 1.1V disponivel no arduino

Comandos recebidos via serial:
	1\n        	---> retorna a versão do firmware
	2,n\n		---> retorna a tensao no canal n (varia entre 0 e 5 volts)
	3\n  		---> retorna o valor de Vcc - utilizado para depuracao

Entrada: A0  a A5  (0-5 V)

obs: firmware projetado para cpus 328 /168 

codigo original da leitura da tensao de referencia:
    https://code.google.com/archive/p/tinkerit/wikis/SecretVoltmeter.wiki

Copyright 2016 Roberto Tavares, Licença: GNU GPL v3 http://www.gnu.org/licenses/gpl-3.0.html
www.cadernodelaboratorio.com.br

***********************************************
*/





/*
Defines 
*/


#define	LED_PLACA    13	//Pino led na placa

#define	MAX_LEN_ENTRADA     32	//tamanho do buffer de entrada
#define	NUMERO_MAXIMO_FUNCOES    4
#define	MAX_LEN_SAIDA     32	

/*
Globals variables 
*/
char chLido;	// contem o caracter lido
int cIndexEscrita;

char chParam[16];	// buffer para armazenamento do primeiro parametro
char chParam1[8];	// buffer para armazenamento do segundo parametro
char chCmd[4];		// buffer para o armazenamento do comando completo

char chSaida[MAX_LEN_SAIDA];
char chPDU[MAX_LEN_ENTRADA];

//vetor de funcoes que implementam os comandos
void (*func[NUMERO_MAXIMO_FUNCOES])();


static  float fVoltagesValues[6];	// contem os valores de tensao lidos


void setup()
{

pinMode (LED_PLACA,OUTPUT);	//porta com o led programda como saida
pinMode(12,OUTPUT);
digitalWrite(12,1);

Serial.begin(38400, SERIAL_8N1);




//inicializacao dos ponteiros de insecao e buffer de recepcao de comandos
cIndexEscrita=0;
chPDU[0]=0;

//inicializacao do vetor de chamada de funcoes
func[1]= reID;
func[2]= readValue;
func[3]= readVccValue;

//  Pisca o led 2x para dizer esta tudo OK
int  nLoop;	
for(nLoop=0; nLoop<2; ++nLoop)
	{
	digitalWrite (LED_PLACA,HIGH);	//acende o led
	delay (250);
	digitalWrite (LED_PLACA,LOW);
	delay (250);
	}
}

void loop()
{

/************************************************
le os caracteres vindos da serial e monta o comando
**************************************************/ 
chLido= Serial.read();

if(chLido != -1)
  {
  if(chLido != 0x0d)  //joga fora os 0x0d caso existam
    {  
    chPDU[cIndexEscrita]= chLido;
   
    if(chLido == 0x0A)  // delimitador de final de comando detectdo
      {
      chPDU[cIndexEscrita]=0;   
      processaCmd();  //ao final do comando chama a decodificacao
      cIndexEscrita=0;  //prepara para um novo comando
      }
    else
      {   
      ++cIndexEscrita;
      cIndexEscrita &= (MAX_LEN_ENTRADA -1);
      }
    }
  } 

}



// decodifica o comando e desvia para a rotina indicada no vetor de vetor de comandos
void processaCmd()
{
int nCmd;
//obtem o comando
strcpy(chCmd,strtok(chPDU,","));
nCmd= atoi(chCmd);
//obtem o primeiro paremtro
strcpy(chParam,strtok(NULL,","));
//obtem o segundo parametro
strcpy(chParam1,strtok(NULL,","));


if(nCmd > (NUMERO_MAXIMO_FUNCOES-1) ||  nCmd < 1)
  Serial.println("$255,Comando inexistente");
else  
//chama a rotina correspondente
	(*func[nCmd])();  
 
}




void reID()
{ 
Serial.println("$1,Voltmeter 1.0");
}

// valor enviado a serial  em milivolts
void readValue()
{
int nCanal;
char chMsg[20];
long lValue;
long lVcc;

nCanal= atoi(chParam);
lVcc= readVcc();

lValue= (long) analogRead(nCanal);

lValue= (lValue * lVcc)/1023L; 

sprintf(chMsg,"$2,%u\n", (unsigned int) lValue);

Serial.println(chMsg);

}


// valor enviado a serial em milivolts
void   readVccValue()
{
char chMsg[20];

long lVcc= readVcc();

sprintf(chMsg,"$3,%u\n", (unsigned int) lVcc);

Serial.print(chMsg);
}


// valor retornado em milivolts
long readVcc() 
{ 
long result; // Read 1.1V reference against AVcc 

ADMUX = _BV(REFS0) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1); 

delay(2); 		// Wait for Vref to settle 

ADCSRA |= _BV(ADSC);     // Convert 

while (bit_is_set(ADCSRA,ADSC)); 

result = ADCL; 

result |= ADCH<<8;
 
result = 1126400L / result;    // Back-calculate AVcc in mV 

return result; 
}



