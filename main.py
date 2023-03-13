import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.set('1', 'primeira chave usando r.set')
print(r.get('1'))

r.mset({"1030": "Analista", "1050":"Gerente", "1060": "Tester"})
print("Printando varios",r.mget("1030","1050","1060"))


print(r.exists("1020"))
print(r.delete("1030"))
print(r.type("1030"))
print(r.get("1050"))

r.set("Segundos", "Expirando em 60 segundos")
r.expire("Segundos", 60)
print(r.ttl("Segundos"))

r.set("Milisegundos", "Expirando em 10 milisegundos")
r.pexpire("Milisegundos",10)
print(r.pttl("Milisegundos"))

r.persist("Segundos")
print("Tirando a expiração", r.ttl("Segundos"))

r.set("100", "Engenheiro de Dados")
print("Printando apenas Engenheiro",r.getrange("100", 0,9))
print("Verificando o tamanho",r.strlen("100"))
print("Atualizando valor", r.getset("100", "Engenheiro de Produção"))
print("Verificando o tamanho",r.strlen("100"))
profissao = r.get("100")
print("printando", profissao.decode())

### HASHES ####

r.hmset("campos", {"Campo_um": "valor", "Campo_dois": "valor", "Campo_tres": "valor"})
print("Printando todos os campos",r.hgetall("campos"))
print("Printando quantas chaves há =", r.hlen("campos"))
print("Retorna as chaves sem os valores", r.hkeys("campos"))

### LISTS ###

# print("Adicionando items a uma lista", r.lpush("Nome_da_lista", "Campo_um", "Campo_dois"))
# print("Incluindo um item", r.lpush("Nome_da_lista", "Campo_tres"))
# print("Retornando pelo indice", r.lrange("Nome_da_lista", 0,10))
# print("Incluindo em determinanda posição da lista(antes de Campo Um)", r.linsert("Nome_da_lista", "after", "Campo_um", "Campo_zero"))
print("Retornando por posição", r.lrange("Nome_da_lista",0,9))
print("Comprimento da lista é=", r.llen("Nome_da_lista"))
print("Remover inicio", r.lpop("Nome_da_lista"))
print("Remover o final", r.rpop("Nome_da_lista"))


### SETS ###

print("Adicionando itens que caso repetidos, sao ignorados", r.sadd("13","primeiro","segundo"))
print("Adicionando o mesmo de proposito", r.sadd("13", "primeiro"))
print("Verificando se determinado componente é membro da lista =", r.sismember("13", "primeiro"))
print("Verificando o que há dentro do set", r.smembers("13"))
r.sadd("14", "primeiro", "segundo", "terceiro")
print("verificando a diferença dos dois conjuntos", r.sdiff("14","13"))
print("verificando  o que há em comum entre os dois conjuntos", r.sinter("14","13"))


#### SORTED SETS ####

r.zadd("Chave",{
    "key1": 1,
    "key2": 2
})
print("verificando  quantas keys há = ", r.zcard("Chave"))
print("verificando  em que posição esta a chave =", r.zrank("Chave","key2"))
print("conta quanto scores há dentro do range inserido =", r.zcount("Chave",0,3))
print("Retorna o score da chave =", r.zscore("Chave", "key1"))
print("Retornando os membros com ou sem score(true, false)", r.zrange("Chave", 0,3, False))
print("Removendo membro",r.zrem("Chave", "key1"))









