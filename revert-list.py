# coding=utf-8
"""
 * Nao tem como criar classes internas no Python,
 * entao infelizmente a classe Node fica publica
 *
 * Tambem nao existe modificador de acessibilidade,
 * entao tudo eh publico... varzea total! ihul \o/
 *
 * ¯\_(ツ)_/¯
 *
"""


class Node:
    # variaveis declaradas diretamente na classe (aqui) sao membros da classe e nao do objeto
    # normalmente em python nao se declara nada, eh tudo no pelo, go horse style (pensou, nao eh go horse)

    def __init__(self, content):
        # aqui no construtor eh que se "declara" a variavel ja atribuindo valor
        # e usando o self, que representa o objeto instanciado
        self.content = content
        self.next = None


class LinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def add(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.next is not None:
                n = n.next

            n.next = node

        self.count += 1

    def revert(self):
        prev = None
        curr = self.head

        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        self.head = prev

    # o padrao de nomes do python eh tudo minusculo (nao eh regra, eh padrao)
    # entao chamei a funcao de item() ao inves getItem()
    def item(self, index):
        p = self.head

        for i in xrange(0, index):
            p = p.next

        return p.content

    def size(self):
        return self.count

    def __str__(self):
        buf = ""
        for i in xrange(0, self.size()):
            buf += str(self.item(i)) + " "

        return buf


# Obs.: a implementacao do xrange eh usado por padrao no python3 dentro funcao range
# no python 2 voce tem as duas opcoes (range e xrange),
# diz a lenda que xrange consome menos memoria... coisas de python ¯\_(ツ)_/¯
# Obs2.: o segundo parametro da funcao range/xrange eh exclusivo (inicio -> fim-1)

# ----------- MAIN ---------- #

llist = LinkedList()

for i in xrange(1, 11):
    llist.add(i)

print(llist)
llist.revert()
print(llist)

str_list = LinkedList()
for i in xrange(1, 6):
    str_list.add("str" + str(i))

print(str_list)
str_list.revert()
print(str_list)

print("")
