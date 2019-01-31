
## intent:hello
- salut
- bonjour
- ça va
- hey
- hello
- coucou

## intent:search_dataset
- statistiques de [la ville de paris](organization)
- je cherche [les données](object) du [ministère de l'intérieur](organization)
- j'aimerai connaitre la [qualité de l'air](topic) à Paris
- Je voudrai avoir [les chiffres](object) de la [population française](topic)
- quel est [mon numéro](object) [RNA](topic) ?
- poule 2010
- je veux des données
- [vigicrue](topic) 2018
- base [SIRENE](topic)

## intent:thankyou
- merci
- c'est chouette
- cool !
- super !

## intent:bye
- au revoir
- à plus
- bye
- ciao
- bonne nuit

## lookup:organization
organisations.txt

## lookup:dataset
datasets.txt

## regex:year
- [0-9]{4}
