
bekeres = input("IP: ")
g = bekeres.split(".")


#________________________________elso________

e_128 = int(g[0]) // 128
e_m = int(g[0]) % 128

e_64 = e_m // 64
e_m2 = e_m % 64

e_32 = e_m2 // 32
e_m3 = e_m2 % 32

e_16 = e_m3 // 16
e_m4 = e_m3 % 16

e_8 = e_m4 // 8
e_m5 = e_m4 % 8

e_4 = e_m5 // 4
e_m6 = e_m5 % 4

e_2 = e_m6 // 2
e_m7 = e_m6 % 2

e_1 = e_m7 // 1
e_m8 = e_m7 % 1

elso_bin = []
elso_bin.append(e_128)
elso_bin.append(e_64)
elso_bin.append(e_32)
elso_bin.append(e_16)
elso_bin.append(e_8)
elso_bin.append(e_4)
elso_bin.append(e_2)
elso_bin.append(e_1)

#print(f" {g[0]} == {elso_bin}")
#________________________________masodik________

m_128 = int(g[1]) // 128
m_m = int(g[1]) % 128

m_64 = m_m // 64
m_m2 = m_m % 64

m_32 = m_m2 // 32
m_m3 = m_m2 % 32

m_16 = m_m3 // 16
m_m4 = m_m3 % 16

m_8 = m_m4 // 8
m_m5 = m_m4 % 8

m_4 = m_m5 // 4
m_m6 = m_m5 % 4

m_2 = m_m6 // 2
m_m7 = m_m6 % 2

m_1 = m_m7 // 1
m_m8 = m_m7 % 1

masodik_bin = []
masodik_bin.append(m_128)
masodik_bin.append(m_64)
masodik_bin.append(m_32)
masodik_bin.append(m_16)
masodik_bin.append(m_8)
masodik_bin.append(m_4)
masodik_bin.append(m_2)
masodik_bin.append(m_1)

#print(f" {g[1]} == {masodik_bin}")
#________________________________harmadik________

h_128 = int(g[2]) // 128
h_m = int(g[2]) % 128

h_64 = h_m // 64
h_m2 = h_m % 64

h_32 = h_m2 // 32
h_m3 = h_m2 % 32

h_16 = h_m3 // 16
h_m4 = h_m3 % 16

h_8 = h_m4 // 8
h_m5 = h_m4 % 8

h_4 = h_m5 // 4
h_m6 = h_m5 % 4

h_2 = h_m6 // 2
h_m7 = h_m6 % 2

h_1 = h_m7 // 1
h_m8 = h_m7 % 1

harmadik_bin = []
harmadik_bin.append(h_128)
harmadik_bin.append(h_64)
harmadik_bin.append(h_32)
harmadik_bin.append(h_16)
harmadik_bin.append(h_8)
harmadik_bin.append(h_4)
harmadik_bin.append(h_2)
harmadik_bin.append(h_1)

#print(f" {g[2]} == {harmadik_bin}")

#________________________________negyedik________

n_128 = int(g[3]) // 128
n_m = int(g[3]) % 128

n_64 = n_m // 64
n_m2 = n_m % 64

n_32 = n_m2 // 32
n_m3 = n_m2 % 32

n_16 = n_m3 // 16
n_m4 = n_m3 % 16

n_8 = n_m4 // 8
n_m5 = n_m4 % 8

n_4 = n_m5 // 4
n_m6 = n_m5 % 4

n_2 = n_m6 // 2
n_m7 = n_m6 % 2

n_1 = n_m7 // 1
n_m8 = n_m7 % 1

negyedik_bin = []
negyedik_bin.append(n_128)
negyedik_bin.append(n_64)
negyedik_bin.append(n_32)
negyedik_bin.append(n_16)
negyedik_bin.append(n_8)
negyedik_bin.append(n_4)
negyedik_bin.append(n_2)
negyedik_bin.append(n_1)

#print(f" {g[3]} == {negyedik_bin}")
elso_bin.extend(masodik_bin)
elso_bin.extend(harmadik_bin)
elso_bin.extend(negyedik_bin)


print(f"teljes bináris forma IP: {elso_bin}")


#______________________________________________________________maszk____________________________________________________




bekeres2 = input("netmaszk: ")
gg = bekeres2.split(".")


#________________________________elso________

n_e_128 = int(gg[0]) // 128
n_e_m = int(gg[0]) % 128

n_e_64 = n_e_m // 64
n_e_m2 = n_e_m % 64

n_e_32 = n_e_m2 // 32
n_e_m3 = n_e_m2 % 32

n_e_16 = n_e_m3 // 16
n_e_m4 = n_e_m3 % 16

n_e_8 = n_e_m4 // 8
n_e_m5 = n_e_m4 % 8

n_e_4 = n_e_m5 // 4
n_e_m6 = n_e_m5 % 4

n_e_2 = n_e_m6 // 2
n_e_m7 = n_e_m6 % 2

n_e_1 = n_e_m7 // 1
n_e_m8 = n_e_m7 % 1

n_elso_bin = []
n_elso_bin.append(n_e_128)
n_elso_bin.append(n_e_64)
n_elso_bin.append(n_e_32)
n_elso_bin.append(n_e_16)
n_elso_bin.append(n_e_8)
n_elso_bin.append(n_e_4)
n_elso_bin.append(n_e_2)
n_elso_bin.append(n_e_1)

#print(f" {gg[0]} == {n_elso_bin}")
#________________________________masodik________

n_m_128 = int(gg[1]) // 128
n_m_m = int(gg[1]) % 128

n_m_64 = n_m_m // 64
n_m_m2 = n_m_m % 64

n_m_32 = n_m_m2 // 32
n_m_m3 = n_m_m2 % 32

n_m_16 = n_m_m3 // 16
n_m_m4 = n_m_m3 % 16

n_m_8 = n_m_m4 // 8
n_m_m5 = n_m_m4 % 8

n_m_4 = n_m_m5 // 4
n_m_m6 = n_m_m5 % 4

n_m_2 = n_m_m6 // 2
n_m_m7 = n_m_m6 % 2

n_m_1 = n_m_m7 // 1
n_m_m8 = n_m_m7 % 1

n_masodik_bin = []
n_masodik_bin.append(n_m_128)
n_masodik_bin.append(n_m_64)
n_masodik_bin.append(n_m_32)
n_masodik_bin.append(n_m_16)
n_masodik_bin.append(n_m_8)
n_masodik_bin.append(n_m_4)
n_masodik_bin.append(n_m_2)
n_masodik_bin.append(n_m_1)

#print(f" {gg[1]} == {n_masodik_bin}")
#________________________________harmadik________

n_h_128 = int(gg[2]) // 128
n_h_m = int(gg[2]) % 128

n_h_64 = n_h_m // 64
n_h_m2 = n_h_m % 64

n_h_32 = n_h_m2 // 32
n_h_m3 = n_h_m2 % 32

n_h_16 = n_h_m3 // 16
n_h_m4 = n_h_m3 % 16

n_h_8 = n_h_m4 // 8
n_h_m5 = n_h_m4 % 8

n_h_4 = n_h_m5 // 4
n_h_m6 = n_h_m5 % 4

n_h_2 = n_h_m6 // 2
n_h_m7 = n_h_m6 % 2

n_h_1 = n_h_m7 // 1
n_h_m8 = n_h_m7 % 1

n_harmadik_bin = []
n_harmadik_bin.append(n_h_128)
n_harmadik_bin.append(n_h_64)
n_harmadik_bin.append(n_h_32)
n_harmadik_bin.append(n_h_16)
n_harmadik_bin.append(n_h_8)
n_harmadik_bin.append(n_h_4)
n_harmadik_bin.append(n_h_2)
n_harmadik_bin.append(n_h_1)

#print(f" {gg[2]} == {n_harmadik_bin}")

#________________________________negyedik________

n_n_128 = int(gg[3]) // 128
n_n_m = int(gg[3]) % 128

n_n_64 = n_n_m // 64
n_n_m2 = n_n_m % 64

n_n_32 = n_n_m2 // 32
n_n_m3 = n_n_m2 % 32

n_n_16 = n_n_m3 // 16
n_n_m4 = n_n_m3 % 16

n_n_8 = n_n_m4 // 8
n_n_m5 = n_n_m4 % 8

n_n_4 = n_n_m5 // 4
n_n_m6 = n_n_m5 % 4

n_n_2 = n_n_m6 // 2
n_n_m7 = n_n_m6 % 2

n_n_1 = n_n_m7 // 1
n_n_m8 = n_n_m7 % 1

n_negyedik_bin = []
n_negyedik_bin.append(n_n_128)
n_negyedik_bin.append(n_n_64)
n_negyedik_bin.append(n_n_32)
n_negyedik_bin.append(n_n_16)
n_negyedik_bin.append(n_n_8)
n_negyedik_bin.append(n_n_4)
n_negyedik_bin.append(n_n_2)
n_negyedik_bin.append(n_n_1)


n_elso_bin.extend(n_masodik_bin)
n_elso_bin.extend(n_harmadik_bin)
n_elso_bin.extend(n_negyedik_bin)

#print(f" {gg[3]} == {n_negyedik_bin}")

print(f"teljes bináris forma netmaszk: {n_elso_bin}")


#print(elso_bin)
#print(n_elso_bin)


"""
for sor in elso_bin:
    for sor1 in n_elso_bin:
        if sor == '1' or sor1 == '1':
            alhalozati.append(sor)
        if sor == '0' or sor1 == '0':
            host_cim.append(sor)


"""
bites_forma_ip = ""
bites_forma_netmaszk = ""
for szam in elso_bin:
    bites_forma_ip = str(szam) + bites_forma_ip
    
for szam in n_elso_bin:
    bites_forma_netmaszk = str(szam) + bites_forma_netmaszk

#print(f"hoszt cim: {host_cim}")
#print(f"alhálozati cim: {alhalozati_cim}")


#print(bites_forma_ip)
#print(bites_forma_netmaszk)

szamlalo_0 = 0
szamlalo_1 = 0
alhalozati_cim = ""
host_cim = ""
for szam in bites_forma_netmaszk:
    if szam == '0':
        szamlalo_0 = szamlalo_0 + 1
        host_cim = szam + host_cim
    else:
        szamlalo_1 = szamlalo_1 + 1
        alhalozati_cim = szam + alhalozati_cim

print(f"Host: ennyi 0: {szamlalo_0} db.\nHost: {host_cim}")
print(f"Alhálozati: ennyi 1: {szamlalo_1} db. \nAlhálózati: {alhalozati_cim}")
indem = 32 - len(host_cim)
harmincas = bites_forma_ip[:indem]
netmaszkos = harmincas + host_cim
print(f"eredmény: {netmaszkos}")



#________________________________binárisbol decimálisba________

szeletes0 = bites_forma_ip[-8:]

d_128 = int(szeletes0[-1]) * 128

d_64 = int(szeletes0[-2]) * 64


d_32 = int(szeletes0[-3]) * 32


d_16 = int(szeletes0[-4]) * 16


d_8 = int(szeletes0[-5]) * 8


d_4 = int(szeletes0[-6]) * 4


d_2 = int(szeletes0[-7]) * 2


d_1 = int(szeletes0[-8]) * 1

ossz0 = d_128 + d_64 + d_32 + d_16 + d_8 + d_4 + d_2 + d_1

#__________________________________________-masodik_________---decimálisba
szeletes1 = bites_forma_ip[15:24] # 23

d1_128 = int(szeletes1[-1]) * 128

d1_64 = int(szeletes1[-2]) * 64


d1_32 = int(szeletes1[-3]) * 32


d1_16 = int(szeletes1[-4]) * 16


d1_8 = int(szeletes1[-5]) * 8


d1_4 = int(szeletes1[-6]) * 4


d1_2 = int(szeletes1[-7]) * 2


d1_1 = int(szeletes1[-8]) * 1

ossz1 = d1_128 + d1_64 + d1_32 + d1_16 + d1_8 + d1_4 + d1_2 + d1_1


#__________________________________________-negyedik_________---decimálisba
szeletes3 = bites_forma_ip[0:8] # 15

d3_128 = int(szeletes3[-1]) * 128

d3_64 = int(szeletes3[-2]) * 64


d3_32 = int(szeletes3[-3]) * 32


d3_16 = int(szeletes3[-4]) * 16


d3_8 = int(szeletes3[-5]) * 8


d3_4 = int(szeletes3[-6]) * 4


d3_2 = int(szeletes3[-7]) * 2


d3_1 = int(szeletes3[-8]) * 1

ossz2 = d3_128 + d3_64 + d3_32 + d3_16 + d3_8 + d3_4 + d3_2 + d3_1

#__________________________________________-i_________---decimálisba
szeletes4 = bites_forma_ip[8:16] # 15 # 8

d4_128 = int(szeletes4[-1]) * 128

d4_64 = int(szeletes4[-2]) * 64


d4_32 = int(szeletes4[-3]) * 32


d4_16 = int(szeletes4[-4]) * 16


d4_8 = int(szeletes4[-5]) * 8


d4_4 = int(szeletes4[-6]) * 4


d4_2 = int(szeletes4[-7]) * 2


d4_1 = int(szeletes4[-8]) * 1

ossz3 = d4_128 + d4_64 + d4_32 + d4_16 + d4_8 + d4_4 + d4_2 + d4_1

print(f"binárisbol decimálisba {ossz0}.{ossz1}.{ossz3}.{ossz2}")

# vissza forditás


    

jo_bites_ip = ""
jo_bites_maszk = ""
for sor in elso_bin:
    jo_bites_ip = jo_bites_ip + str(sor)

for sor in n_elso_bin:
    jo_bites_maszk = jo_bites_maszk + str(sor)
    

alhalozati_cim11 = ""
host_cim11 = "" 
for maszk in jo_bites_maszk:
    for ip in jo_bites_ip:
        if maszk == '1':
            alhalozati_cim11 = alhalozati_cim11 + ip
        else:
            host_cim11 = host_cim11 + ip


