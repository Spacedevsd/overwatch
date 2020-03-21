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
        'description': 'O arsenal versátil de Ana permite que ela afete heróis em todo o campo de batalha. Os tiros de seu Rifle Biótico e as Granadas Bióticas curam aliados e prejudicam inimigos. Sua arma de mão neutralizam alvos importantes e o Estimulante concede a um aliado um grande aumento de poder.',
        'difficulty': 3,
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
        'description': 'Roadhog usa sua famosa Corrente de Gancho para puxar seus inimigos para perto antes de estraçalhá-los com as explosões de sua Arma de Sucata. Ele é tanque o suficiente para suportar uma grande quantidade de dano e pode recuperar sua vida com uma respiração.',
        'difficulty': 1,
        'name': 'Roadhog',
        'role': 'Tanque'
    }
]

snapshots['test_extract_name 1'] = 'Ana'

snapshots['test_extract_role 1'] = 'Suporte'

snapshots['test_extract_description 1'] = 'O arsenal versátil de Ana permite que ela afete heróis em todo o campo de batalha. Os tiros de seu Rifle Biótico e as Granadas Bióticas curam aliados e prejudicam inimigos. Sua arma de mão neutralizam alvos importantes e o Estimulante concede a um aliado um grande aumento de poder.'

snapshots['test_extract_abilities 1'] = [
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
]

snapshots['test_extract_difficulty 1'] = 3
