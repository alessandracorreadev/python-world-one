first_20 = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo',
            'Grêmio', 'Red Bull Bragantino', 'Atlético-MG', 'Santos', 'Corinthians', 'Vasco', 'Vitória-BA',
            'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport')

print(f"Teams list: {first_20}")

print(f"The top 5 teams are: {first_20[:5]}")

print(f"The bottom 4 teams in the table are: {first_20[-4:]}")

print(f"The teams list in alphabetical order: \n{sorted(first_20)}")

print(f"São Paulo is in position {first_20.index('São Paulo')+1}.")