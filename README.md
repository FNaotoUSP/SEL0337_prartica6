# SEL0337_prartica6

Nomes: 				
Fabio Naoto Massuda Hoçoya    11801115
João Pedro Tonet              12777076

Prática 6: 
Introdução às interfaces de visão computacional, sistemas de versionamento de arquivos e controle de acesso via Tags

Na prática 6 foram feitas duas montagens, uma utilizando a placa de RFID e a segunda utilizando o módulo de câmera. Para a utilização da RFID, foi realizada a montagem do circuito apresentado na Figura 1:

Figura 1:
<img src="/figuras/circuito_tag.jpg">

Para testar o funcionamento das TAGs foram utilizados os códigos “RFID_write.py” e “RFID_read.py” para realizar a leitura do “ID” e da “info” das tags e para modificá-las respectivamente.

Assim, a partir das informações da TAG recebidas pelo módulo, foi possível criar um script em python 3 para controle de acesso, em que todas as verificações subsequentes de identidade serão comparadas com os dados previamente cadastrados.

Para fins de verificação do correto funcionamento do código, foi inserido uma lógica de acionamento de um LED para indicar a liberação ou não do acesso. Caso a TAG aproximada ao leitor correspondesse aos dados na memória, um LED na cor verde seria acionado, caso contrário, seria ativado um da cor vermelha.

Figura 2:
<img src="/figuras/led_red_on.jpg">

Figura 3:
<img src="/figuras/tag_green_on.jpg">

A segunda parte do experimento não foi possível ser realizada devido a falta de câmeras funcionando. Foram testadas 6 módulos e 2 Raspberry Pi diferentes.
