#segmenter.py
import sys

text = str('''Hello. My name is Zack. I am doing well.
L'aragonés ("idioma aragonés" u "luenga aragonesa") ye un idioma romance, luenga propia d'Aragón, parlato por bellas 25.556 personas sobretot en as comarcas pirinencas y prepirinencas d'o norte d'Aragón. En as atras comarcas aragonesas a on que se charró l'idioma, hue o substrato y influencia de l'aragonés ye encara perceptible en o castellano que se i fabla, más que más en os aragonesismos lexicos.
Denominación.
A denominación formal mes común d'a luenga ye aragonés, nombre con que ye conoixita localment, historicament y internacional. A tradición filolochica fa uso igualment d'o compuesto navarro-aragonés u navarroaragonés ta referir-se, más que más, a lo estadio medieval d'o idioma, a consonant con l'uso d'atros compuestos lingüistico-cheograficos ta atros romances peninsulars como lo galaico-portugués u l'astur-leyonés. Popularment, a falta historica de claros referents lingüisticos y una diglosia multisecular con o castellano accentuoron as diferiencias dialectals de l'idioma, afavorindo una baixa conscienciación unitaria entre os parladors d'a luenga, y fendo que aquells que millor mantenioron o dialecto propio lo denominasen con un nombre local (ansotano, cheso, belsetán, chistabín, etc.) Fabla ye una altra denominación informal, considerata alternativa per beluns, popularizata en a segunda metat d'o s. XX. En realidat ye un alcurzamiento d'a expresión "fabla aragonesa", inspirata en a de "fabla chesa", usata en cheso.
Situación.
L'aragonés ye encara parlato como luenga materna en o suyo nuclio orichinal, as montanyas aragonesas d'os Pirineus, en as comarcas d'o Viello Aragón (Chacetania y Alto Galligo), Semontano, Sobrarbe y Ribagorza. As ciudatz y villas prencipals an encara puede trobar-se fabladors patrimonials de l'aragonés son: Uesca, Graus, Monzón, Balbastro, Fonz, Echo, Estadilla, Benás, Samianigo, Pandicosa, Chaca, Plan, Ansó, Ayerbe, Broto, Lo Grau. Altros aragoneses tamién aprenden aragonés como una segunda luenga en puestos como Uesca, Zaragoza, Exeya, y Teruel. Seguntes os datos d'o Censo de 1981, a on se incluyoron preguntas relativas a l'uso d'as luengas propias, a suma de fabladors no blincaba d'os 30.000, fendo que l'aragonés siga una d'as luengas europeas con más gran periglo d'extinción.
''')

print(text.replace('. ', '.\n'))

