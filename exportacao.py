import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    'sqlite:///basetelefones.db',echo=True
        
        )

conexao_sa = engine.connect()

telefones = pd.read_sql_table('telefones',conexao_sa,index_col='id')
telefones = telefones.query('data=="9-3-2023"')
#telefones.to_excel(f'Bases_Validadas/base_71902.xlsx')
telefones.to_excel(f'Bases_Validadas/base_{str(telefones.iloc[1,4])}.xlsx')