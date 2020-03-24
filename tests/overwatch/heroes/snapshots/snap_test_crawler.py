# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_crawler 1'] = [
    {
        'abilities': [
            {
                'description': 'O rifle de Ana atira dardos que podem restaurar a vida de seus aliados ou causar dano continuado a seus inimigos. Ela é capaz de usar a mira telescópica de seu rifle para dar tiros incrivelmente precisos.',
                'name': 'Rifle Biótico'
            },
            {
                'description': 'Ana dispara um dardo de sua arma secundária, deixando seus inimigos inconscientes (porém eles despertam ao receber dano).',
                'name': 'Dardo Sonífero'
            },
            {
                'description': 'Ana lança uma granada biótica que causa dano aos inimigos e cura os aliados em uma pequena área de efeito. Aliados afetados recebem por tempo limitado cura aumentada de todas as fontes, enquanto inimigos pegos pela explosão não podem se curar por alguns instantes.',
                'name': 'Granada Biótica'
            },
            {
                'description': 'Depois que Ana atinge seus aliados com um estimulante de combate, eles causam mais dano e recebem menos dano dos ataques inimigos temporariamente.',
                'name': 'Estimulante'
            }
        ],
        'bio': {
            'affiliation': 'Overwatch (anteriormente)',
            'age': '60',
            'base': 'Cairo, Egito',
            'occupation': 'Caçadora de recompensa',
            'realname': 'Ana Amari',
            'story': 'Uma das fundadoras de Overwatch, Ana usa suas habilidades e seu conhecimento para defender seu lar e as pessoas que ela ama.Como a Crise Ômnica teve um peso muito grande para o Egito, as forças de segurança esvaziadas e sem pessoal do país se apoiaram nos franco-atiradores de elite. Entres eles, Ana Amari, que era considerada por muitos a melhor do mundo. Sua destreza com as armas, tomada rápida de decisões e instintos, fizeram dela uma seleção natural para se juntar à força de ataque de Overwatch que terminou a guerra.Seguindo o sucesso da missão original de Overwatch, Ana serviu muitos anos como a Segunda no Comando para o Comandante de Ataque Morrison. Apesar de suas grandes responsabilidades liderando a organização, Ana se recusou a deixar as operações de combate. Ela continuou ativa até seus cinquenta anos de idade, até acreditarem que ela morreu nas mãos de uma agente da Talon conhecida como “Widowmaker”,  durante uma missão de resgate de reféns.Na verdade, Ana sobreviveu a esse encontro, mesmo que gravemente ferida e tendo perdido seu olho direito. Durante sua recuperação, ela sentiu o peso de uma vida gasta no combate e decidiu permanecer distante dos conflitos mundiais que se alargavam. Entretanto, com o passar do tempo, ela se deu conta de que não podia fazer nada enquanto sua cidade e as pessoas inocentes ao seu redor eram ameaçados por outros.Agora, Ana voltou à luta para proteger seu país das forças que poderiam desestabilizá-lo; e mais importante, para manter sua família e seus aliados mais próximos em segurança.'
        },
        'description': 'O arsenal versátil de Ana permite que ela afete heróis em todo o campo de batalha. Os tiros de seu Rifle Biótico e as Granadas Bióticas curam aliados e prejudicam inimigos. Sua arma de mão neutralizam alvos importantes e o Estimulante concede a um aliado um grande aumento de poder.',
        'difficulty': 3,
        'maps': [
        ],
        'name': 'Ana',
        'role': 'Suporte'
    },
    {
        'abilities': [
            {
                'description': 'A Arma de Sucata de Roadhog dispara explosões de estilhaços de curto alcance com grande difusão. Como alternativa, ela pode disparar uma bola de estilhaços que detona mais longe, arremeçando fragmentos de metal a partir do ponto de impacto.',
                'name': 'Arma de Sucata'
            },
            {
                'description': 'Roadhog recupera partes de sua vida depois de um breve período de tempo.',
                'name': 'Pegando Fôlego'
            },
            {
                'description': 'Roadhog lança sua corrente em um alvo, se ela acerta, ele o puxa para perto.',
                'name': 'Corrente de Gancho'
            },
            {
                'description': 'Depois de amontoar um carregador superior em sua Arma de Sucata, Roadhog despeja munição. Por um curto período de tempo, ele é capaz de de lançar um fluxo de estilhaços que arremessa os inimigos para trás.',
                'name': 'Cair Matando'
            }
        ],
        'bio': {
            'affiliation': 'Junkers (anteriormente)',
            'age': '48',
            'base': 'Junkertown, Austrália (anteriormente)',
            'occupation': 'Executor (anteriormente), Guarda-costas',
            'realname': 'Mako Rutledge',
            'story': '''Roadhog é um matador sanguinário com uma reputação merecida por crueldade e destruição gratuita.Após a Crise Ômnica, oficiais do governo entregaram o omnium australiano e as terras nos arredores aos ômnicos que quase destruíram o país, na esperança de estabelecer um acordo de paz duradouro. Esse acordo de paz desalojou permanentemente Mako Rutledge e um grande número de residentes da área: um conjunto de sobreviventes, fazendeiros solares e pessoas que só queriam ficar em paz.
Furiosos com a perda de seus lares, Mako e outros residentes recorreram a uma rebelião violenta. Eles formaram a Frente de Liberação Australiana e atacaram o omnium e sua população robô para tomar de volta as terras que tinham sido roubadas deles. Os eventos continuaram a ganhar maiores proporções até que a FLA sabotou o núcleo de fusão do omnium, resultando em uma explosão que destruiu o omnium, irradiou os arredores e sucateou o Deserto Australiano com metal retorcido e destroços por quilômetros.
Mako viu seu lar se tornar uma terra devastada apocalíptica e isso o mudou para sempre.Adaptando-se a seu ambiente, ele pôs uma máscara e partiu pelas autoestradas quebradas do Deserto Australiano em sua moto decrépita. Aos poucos, sua humanidade foi esquecida. Os últimos vestígios de Mako desapareceram e nasceu o matador impiedoso, Roadhog. '''
        },
        'description': 'Roadhog usa sua famosa Corrente de Gancho para puxar seus inimigos para perto antes de estraçalhá-los com as explosões de sua Arma de Sucata. Ele é tanque o suficiente para suportar uma grande quantidade de dano e pode recuperar sua vida com uma respiração.',
        'difficulty': 1,
        'maps': [
        ],
        'name': 'Roadhog',
        'role': 'Tanque'
    }
]
