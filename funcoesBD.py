from cmath import nan
from multiprocessing.dummy import JoinableQueue
from ModeloDB import Telefones,session



def consulta():
    try:
        telefones = Telefones.query.filter(Telefones.valido == None, Telefones.telefone_validando == None).first()
        id = telefones.id
        fone = f'{telefones.ddd}{telefones.fone}'
        valido = {telefones.valido}
        telefone = (fone)
    except:
        print('Tefones Validados. job Finalizado, Faça a exportacao')
    else:
        return telefone
    
def updateParaConsulta(telefone):
    telefones = Telefones.query.filter_by(ddd = telefone[0:2],fone = telefone[2:], valido=None).first()
    telefones.telefone_validando = 1
    telefones.save()

def insert(ddd,fone,data='00-00-0000' ,job=None):
    telefones = Telefones(ddd=ddd,fone=fone,dataentrada=data,numeroJob=job)
    telefones.save()
    print('Inserido os dados com sucesso')

def update(telefone,status):
    telefones = Telefones.query.filter_by(ddd = telefone[0:2],fone = telefone[2:], valido=None).first()
    telefones.valido = status
    telefones.save()
    print('Tefone Validado')

def consultatotal():
    telefones = Telefones.query.all()
    for t in telefones:
        print(t.id,t.ddd,t.fone,t.valido,t.data,t.numeroJob)



if __name__ == '__main__':
    #insert('11','979529488', data='03-08-2022',job='jobteste')
    #print(consulta())
    #update('14991326630',None)
    consultatotal()