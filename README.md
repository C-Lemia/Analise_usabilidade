# Analise_usabilidade
Foi gerado dados fictícios de participantes de uma analise de usabilidade de um shampooo, antes de coloca-lo a venda no mercado nacional. Foram "selecionados" 30 participantes, de idade entre 25 a 65 anos, de ambos os generos, masculino e feminino e tipos de cabelo (Liso, Ondulado, Cacheado, Crespo). Foi coletado os dados de porosidade, oleosidade e hidratação, do cabelo de cada participantes, no intervalo de D0, D14 e D28 ( D0 seria o cabelo antes do começo do uso do produto, D14 seria 14 dias depois do uso e D28 seria 28 dias após o uso do produto).
É realizada uma análise estatística comparativa dos dados de oleosidade, porosidade e hidratação de participantes em dois pontos temporais (D0 e D28). O teste usado é o teste t pareado:

- Realiza um teste t pareado (ttest_rel) para comparar as medições de D0 e D28 para cada métrica (oleosidade, porosidade e hidratação) para verificar se há uma diferença estatisticamente significativa entre os dois tempos.

- Obtém a estatística t e o p-valor para cada teste.

- Caso os dados nao atenderem a suposições de normalidade, então é rodado o teste de Wilcoxon, sendo útil quando se suspeita que a distribuição dos dados possa ser assimétrica ou quando há outliers.

- A combinação dos dois testes permite uma análise mais robusta, já que fornece insights sobre os dados sob diferentes suposições. Se ambos os testes indicam resultados semelhantes, isso fortalece a conclusão sobre a diferença entre os grupos. Se os resultados forem conflitantes, isso pode indicar a necessidade de investigar mais a fundo a distribuição e as características dos dados.

- É gerado arquivo excel tanto para os dados demograficos dos participantes, quanto para os estatisticos.
![image](https://github.com/user-attachments/assets/a0bfdb83-6824-4e3a-a13d-ad9dbaa82bb4)
![image](https://github.com/user-attachments/assets/d3be1b2a-7875-460d-9f15-3530dd056162)
![image](https://github.com/user-attachments/assets/2001ce1b-6a08-45ac-af4a-6d497bee1a07)
![image](https://github.com/user-attachments/assets/ad76e10d-5d3a-412b-90b8-c351bc1c1d01)
![image](https://github.com/user-attachments/assets/0313a846-df11-4640-995e-c709eef38ee4)
![image](https://github.com/user-attachments/assets/1a4147c7-46a0-4294-ace4-9089a1c9b809)
![image](https://github.com/user-attachments/assets/ddeff255-efa5-41ca-b71b-ecb4c0cc1a4b)
![image](https://github.com/user-attachments/assets/68a4054d-482b-4d23-a61f-250bfa6bfb81)
![image](https://github.com/user-attachments/assets/95c8458e-b7cd-411f-93f6-6247463ca2ef)
