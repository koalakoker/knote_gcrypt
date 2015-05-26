'''
Created on 24/mag/2015

@author: koala
'''

RandY = [
241	,
252	,
221	,
107	,
3	,
254	,
193	,
167	,
55	,
5	,
32	,
231	,
121	,
148	,
147	,
6	,
30	,
194	,
52	,
30	,
135	,
86	,
29	,
192	,
62	,
174	,
133	,
156	,
159	,
34	,
181	,
239	,
148	,
248	,
19	,
149	,
224	,
239	,
77	,
129	,
53	,
166	,
20	,
202	,
89	,
209	,
75	,
230	,
124	,
210	,
195	,
21	,
213	,
158	,
39	,
196	,
188	,
8	,
245	,
233	,
20	,
57	,
155	,
34	,
5	,
189	,
217	,
22	,
75	,
10	,
177	,
19	,
119	,
8	,
226	,
196	,
251	,
80	,
44	,
211	,
166	,
70	,
209	,
140	,
240	,
198	,
145	,
22	,
84	,
122	,
109	,
244	,
118	,
96	,
136	,
8	,
77	,
228	,
90	,
253	,
98	,
99	,
143	,
232	,
169	,
185	,
151	,
209	,
130	,
239	,
205	,
99	,
214	,
21	,
224	,
81	,
21	,
27	,
146	,
181	,
227	,
254	,
85	,
245	,
33	,
105	,
126	,
84	,
176	,
102	,
49	,
98	,
243	,
255	,
34	,
180	,
112	,
114	,
84	,
124	,
130	,
144	,
198	,
160	,
103	,
86	,
28	,
70	,
37	,
90	,
9	,
220	,
218	,
3	,
161	,
50	,
235	,
29	,
234	,
184	,
244	,
27	,
39	,
211	,
24	,
64	,
43	,
30	,
139	,
218	,
140	,
168	,
223	,
103	,
14	,
106	,
155	,
60	,
235	,
224	,
131	,
147	,
192	,
198	,
50	,
40	,
65	,
43	,
32	,
241	,
95	,
167	,
212	,
198	,
79	,
45	,
211	,
253	,
115	,
215	,
230	,
183	,
194	,
46	,
253	,
174	,
39	,
190	,
120	,
236	,
161	,
206	,
152	,
94	,
82	,
208	,
139	,
202	,
61	,
188	,
26	,
116	,
204	,
157	,
121	,
175	,
1	,
226	,
103	,
30	,
120	,
215	,
61	,
148	,
97	,
13	,
149	,
131	,
74	,
182	,
44	,
213	,
195	,
92	,
129	,
176	,
205	,
158	,
48	,
129	,
108	,
163	,
223	,
79	,
174	,
204	
]

baseKey = [
192	,
100	,
14	,
173	,
151	,
169	,
181	,
102	,
38	,
40	,
242	,
240	,
125	,
153	,
3	,
233	,
161	,
231	,
250	,
184	,
143	,
198	,
158	,
163	,
93	,
126	,
22	,
144	,
219	,
148	,
129	,
116	,
172	,
51	,
233	,
33	,
89	,
159	,
18	,
44	,
55	,
38	,
182	,
14	,
26	,
81	,
250	,
242	,
236	,
221
]

N = 50

PS = [0] * N
T = [0] * 256
IT = [0] * 256

def GCrypt_Key(keyValue, n):
	x = 0
	
	for i in range(N):
		x += PS[i] * ord(keyValue[i % n])

	return (x % 256)

def GCrypt_Initialize(keyValue, length):

	# Initialize PS "Key Vector"
	for i in range(N):
		PS[i] = baseKey[i]
	for i in range(N):
		PS[i] = GCrypt_Key(keyValue, length)
	
	# Initialize T and IT "Scramble Matrix and Inverse Scramble Matrix"
	for i in range(256):
		T[i] = i
	for k in range(125):
		for n in range(256):
			tmp = T[PS[n % N]]
			T[PS[n % N]] = T[n]
			T[n] = tmp
	for i in range(256):
		IT[i] = 0
		for j in range(256):
			if (T[j] == i):
				IT[i]=j


def GCrypt_encipher(PlainText, n):
	retVal = ""
	InitVal = PS[N-1]
	for i in range(n):
		x = (ord(PlainText[i]) ^ InitVal)
		x = T[x]
		retVal += chr(x)
		InitVal = x
	return retVal

def GCrypt_decipher(CriptText, n):
	retVal = ""
	InitVal = PS[N-1]
	for i in range(n):
		x = IT[ord(CriptText[i])] ^ InitVal
		InitVal = ord(CriptText[i])
		retVal += chr(x)
	return retVal

def GCrypt(command, testo, n):
	if (command[0] == 'c'):
		retVal = GCrypt_encipher (testo,n)
	if (command[0] == 'd'):
		retVal = GCrypt_decipher (testo,n)
	return retVal

"""
/////////////////////////////////////////////////////////
// Procedura di Hashing della password
/////////////////////////////////////////////////////////
"""

# Ritorna il Byte iesimo 3 2 1 0 del int
def GetByte(iVal, iPos):
	return (iVal>>(iPos * 8)) % 256

# Scrive il byte iesimo 3 2 1 0 del int
def SetByte(iVal, iPos, cValue):
	iTemp = cValue
	iMask = 0xFF
	iTemp = iTemp << (iPos * 8)
	iMask = iMask << (iPos * 8)
	iVal = iVal & (~iMask)
	iVal = iVal | (iTemp)
	return iVal

def GHashPass(pasw, n):
	pH = 0
	for i in range(n):
		pH += ord(pasw[i])
	pL = 0
	for i in range(n):
		pL += RandY[ord(pasw[i])]
	for i in range(n):
		for j in range(4):	
			pL = SetByte(pL,3-j,GetByte(pH,j) ^ ord(pasw[i]))
			pH = SetByte(pH,3-j,GetByte(pL,j) ^ RandY[ord(pasw[i])])
	return (pH << 32) + pL

def toHex(s):
	return (':'.join(x.encode('hex') for x in s))