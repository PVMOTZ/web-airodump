#!/bin/bash
#####################################################
#                                                   #
#    Monitoramento de Redes WiFi - MACTRIX          #
#                                                   #
# Uso:                                              #
# mactrix [Interface Wireless] [Channel]            #
#                                                   #                               
# -A interface wireless deve está em modo monitor   #
#                                                   #  
# -Se nenhum canal for especifico, o canal 11 será  #
#  utilizado                                        #
#####################################################


########################################
# Checando se os parametros do programa#
# foram passados corretamente          #
########################################
if [ -z $1 ]; then
  echo "ERRO: Interface Wireless não informada"
  exit
fi
IWIRELESS=$1

if [ -z $2 ]; then
  CHANNEL="1 6 11"
else
  CHANNEL=$2
fi
echo "Canais escolhidos: $CHANNEL - OK"


################################################
# Essa parte do codigo checa se a placa Wifi   #
# está presente e se está em modo monitor      #
################################################
function check_iw_name {
  # checa se a interface wireless existe
  local TMP=$( iwconfig 2> /dev/null | grep -i -o $1)
  if [ -z $TMP ]; then
    echo "ERRO: Interface $1 não existe!"
    exit
  else
    echo "Interface $1 - OK"
  fi
}

function check_iw_mode {
  # checa se a interface está em modo monitor
  local TMP=$( iwconfig $1 2> /dev/null | grep -i -o monitor )
  if [ -z $TMP ]; then
    echo "ERRO: A interface $1 não está em modo monitor"
    exit
  else
   echo "Interface $1 em modo monitor! - OK"
  fi 
}

check_iw_name $IWIRELESS
check_iw_mode $IWIRELESS


###########################
#     Setando o canal     #
###########################
iwconfig $IWIRELESS channel CHANNEL


#######################
# Iniciando o MACTRIX #
#######################
sudo python3 flaskapp.py $IWIRELESS
