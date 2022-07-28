![Alt text](/images/tratamento-agua.jpg?raw=true "Optional Title")

# Projeto de Data Science desenvolvida para apresentação na Universidade Federal do Sul e Sudeste do Pará
---

# Entendimento do negócio:
--
**CONTEXTO FICTÍCIO:** A CAASF (Centro de abastecimento de água de São Francisco) é uma empresa pública que abastece algumas cidades do nordeste por meio do Rio São Francisco. Ela está tendo problemas com a qualidade da água fornecida à população, foi verificado que as vezes é utilizado quantidade indevida de materiais para o tratamento. Essa verificação é tida com alguns testes como por exemplo PH, turbidez, TOC (Total Organic Carbon), Sulfato, TDS (Total Dissolved solids), condutividade, entre outros...

**DESAFIO**: Você foi contratado como cientista de dados para fornecer um modelo que **prediz quais as melhores condições que as variáveis envolvidas deve adotar para fornecer uma água pótavel dentro dos padrões estabelecidos por lei.** Tudo isso para que não haja consumação de material ou energia no processo de forma desnecessária. O seu diferencial como cientista de dados está no fato de você também ser engenheiro(a) químico(a), logo, também entenderá todo o processo de tratamento de ponta a ponta.

Vale ressaltar que os ganhos desse projeto, além da otimização do processo como um todo como redução do gasto em materiais e energia, também haverá uma melhora na saúde da população, evitando que postos fiquem sobrecarregados por causa de doenças advindas de água mal tratada.

## Entendimento dos dados

**Fonte:** [Kaggle](https://www.kaggle.com/datasets/adityakadiwal/water-potability)

**Atributos:**


1. **PH:** O pH é um parâmetro importante na avaliação do equilíbrio ácido-base da água. É também o indicador da condição ácida ou alcalina do estado da água. A OMS recomendou o limite máximo permitido de pH de 6,5 a 8,5. Os intervalos de investigação atuais foram de 6,52 a 6,83, que estão na faixa dos padrões da OMS.
2. **Dureza:** A dureza é causada principalmente por sais de cálcio e magnésio. Esses sais são dissolvidos a partir de depósitos geológicos através dos quais a água viaja. O período de tempo em que a água está em contato com o material produtor de dureza ajuda a determinar quanta dureza existe na água bruta. A dureza foi originalmente definida como a capacidade da água de precipitar sabão causada por cálcio e magnésio.
3. **TDS:** A água tem a capacidade de dissolver uma ampla gama de minerais ou sais inorgânicos e alguns orgânicos, como potássio, cálcio, sódio, bicarbonatos, cloretos, magnésio, sulfatos, etc. Esses minerais produziram sabor indesejado e cor diluída na aparência da água. Este é o parâmetro importante para o uso da água. A água com alto valor de TDS indica que a água é altamente mineralizada. O limite desejável para TDS é de 500 mg/le o limite máximo é de 1000 mg/l prescrito para beber.
4. **Cloramina:** Cloro e cloramina são os principais desinfetantes usados ​​em sistemas públicos de água. As cloraminas são mais comumente formadas quando a amônia é adicionada ao cloro para tratar a água potável. Níveis de cloro de até 4 miligramas por litro (mg/L ou 4 partes por milhão (ppm)) são considerados seguros na água potável.
5. **Sulfatos:** Os sulfatos são substâncias naturais encontradas em minerais, solo e rochas. Eles estão presentes no ar ambiente, águas subterrâneas, plantas e alimentos. O principal uso comercial do sulfato é na indústria química. A concentração de sulfato na água do mar é de cerca de 2.700 miligramas por litro (mg/L). Varia de 3 a 30 mg/L na maioria dos suprimentos de água doce, embora concentrações muito mais altas (1000 mg/L) sejam encontradas em algumas localizações geográficas.
6. **Condutividade:** A água pura não é um bom condutor de corrente elétrica, mas um bom isolante. O aumento da concentração de íons aumenta a condutividade elétrica da água. Geralmente, a quantidade de sólidos dissolvidos na água determina a condutividade elétrica. A condutividade elétrica (EC) realmente mede o processo iônico de uma solução que lhe permite transmitir corrente. De acordo com os padrões da OMS, o valor EC não deve exceder 400 μS/cm.
7. **TOC:** O Carbono Orgânico Total (COT) nas águas de nascente vem de matéria orgânica natural em decomposição (NOM), bem como de fontes sintéticas. TOC é uma medida da quantidade total de carbono em compostos orgânicos em água pura. De acordo com a US EPA < 2 mg/L como TOC em água tratada/potável, e < 4 mg/Lit em água de fonte que é usada para tratamento.
8. **Trialometanos:** THMs são produtos químicos que podem ser encontrados em água tratada com cloro. A concentração de THMs na água potável varia de acordo com o nível de matéria orgânica na água, a quantidade de cloro necessária para tratar a água e a temperatura da água que está sendo tratada. Níveis de THM de até 80 ppm são considerados seguros na água potável.
9. **Turbidez:** A turbidez da água depende da quantidade de matéria sólida presente no estado suspenso. É uma medida das propriedades de emissão de luz da água e o teste é usado para indicar a qualidade da descarga de resíduos em relação à matéria coloidal. O valor médio de turbidez obtido para o Wondo Genet Campus (0,98 NTU) é inferior ao valor recomendado pela OMS de 5,00 NTU.
10. **Potabilidade (Variável Target):** Indica se a água é segura para consumo humano onde 1 significa Potável e 0 significa Não potável.