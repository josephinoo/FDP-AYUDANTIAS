#!/usr/bin/env python
# coding: utf-8

# In[28]:


def academico(narchivos):
    notas=dict()
    for archivo in narchivos:
        semestre=archivo[6:-4]
        archivo=open(archivo)
        for linea in archivo:
            matricula,materia,notaP,notaF,notaM,estado=linea.strip().split(",")
            d_semestres=notas.setdefault(matricula,dict())
            listaMaterias=d_semestres.setdefault(semestre,[])
            listaMaterias.append((materia,notaP,notaF,notaM,estado))
    return notas


# In[29]:


notas=("notas-2013-II.csv","notas-2015-I.csv")
d_notas=academico(notas)
d_notas


# In[30]:


def semestres(notas, matricula):
    semestres_dict=notas[matricula]
    return tuple(semestres_dict.keys())
        


# In[31]:


sems=semestres(d_notas,"201321454")


# In[43]:


def nota_academico(notas,matricula,materia):
    d_sems=notas[matricula]
    for materias in d_sems.values():
        for m in materias:
            if m[0]==materia:
                n=m[1:-1]
                return sorted(n,reverse=True)[0:2]


# In[44]:


nota=nota_academico(d_notas,"201321454","Fundamentos de Programacion")


# In[71]:


def mas_aprobados(notas,semestre):
    d=dict()
    for matricula,semestres in notas.items():
        materias=semestres.get(semestre,0)
        if materias!=0:
            for materia in materias:
                print(materia[-1])
                if materia[-1]=="AP":
                    d.setdefault(materia[0],0)
                    d[materia[0]]+=1
    maximo=0
    for m,valor in d.items():
        if maximo<valor:
            maximo=valor
    return maximo


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




