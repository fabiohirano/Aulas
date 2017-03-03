import random

youtubers = ["pewdiepie", "jovemnerd", "rezendeevil", "felipeneto", "felipeneto pagodeiro", "felipeneto sem camisa", "nariz do castanhari", "kéfera", "Justin Bieber", "Donald Trump", "Léo Stronda", "Marcelo"]

adjetivo = ["cabeçudo", "gordo", "pegador"]

mortes = ["asfixiado com amoeba", "afogado em amoeba", "escorregando na nutella", "tropeçando no Eevee", "atropelado por um rinoceronte bêbado", "caindo do penhasco, quebrando a perna e caindo de novo", "bêbado e drogado", "pisoteado por um dragao branco de olhos azuis e rabo cor de rosa", "dormindo", "levando um coco na cabeça", "splashado por uma magicarpa", "de avc", "ouvindo Justin Biba", "intoxicado por Dolly Guaraná", "jogando CS por 87 horas seguidas", "levando um soco de Jooooooooooohn Ceeeeeeeeeeenaaaaaaaaa", "correndo para chegar no banheiro", "decapitado por el disco vuelador", "flagrado pela mãe vendo pornografia"]

tempo = random.randint(1, 60)

print random.choice(youtubers), random.choice(adjetivo), random.choice(adjetivo), "vai morrer em", str(tempo), "segundos", random.choice(mortes)
