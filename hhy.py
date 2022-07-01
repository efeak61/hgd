import random

x=None
y=0
z=0
kc=0
kn=0
cn=0
g=0
a=0
b=0
knt="bilinmiyor"
dd=0
yd=0
yy=0

#########################
# ___arasındaki sayı___
def sya(): 
	km=1
	while km==1:
		g=0
		a=input("1.arasında sayı :")
		b=input("2.arasında sayı :")
		if a.isdigit()==1 and b.isdigit()==1:
			a=int(a)
			b=int(b)
			g=1
		if g==1:
			if a<b:
				return a,b
				km=0
			else:
				g=0
				print("1.sayı 2.sayıdan büyük olacak")
		else:
			print("sayı giriniz")
#########################
#___kumar sayıları___
def syg(a,b):
	kl=1
	while kl==1:
		ku=0
		print("____________________")
		print("1.sayı - 2.sayı - 3.sayı")
		print("____________________")
		s1=input("1.sayı :")
		s2=input("2.sayı :")
		s3=input("3.sayı :")
		if s1.isdigit()==s2.isdigit()==s3.isdigit()==1:
			s1=int(s1)
			s2=int(s2)
			s3=int(s3)
			if a<s1<b and a<s2<b and a<s3<b:
				kl=0
				return s1,s2,s3
			else:
				print(a,"ve",b,"arasında olmalı")
		else:
			print("sayı giriniz")
#########################
#___kumar tekrarı___
def rn(s1,s2,s3,kn,yy,dd,a,b,kc):
	kk=1
	while  kk==1:
		x=input("tekrarlama sayısı :")
		if x.isdigit()==1:
			x=int(x)
			tkr=range(1,1+x)
			for tk in tkr :
				r1=random.randint(a,b)
				r2=random.randint(a,b)
				r3=random.randint(a,b)
				if((s1==r1)and(s2==r2)and(s3==r3)):
					kn=1
					knt="kumarı kazandınız"
					kc=kc+1
				elif kn==0:
					knt="kumarı kaybettiniz"
				if((s1==r1)and(s2==r2)and(s3==r3)):
					dr="doğru"
					dd=dd+1
				else:
					dr="yanlış"
					yy=yy+1
				if dr=="doğru" or dr=="yanlış" :
					print("random = |{}|{}|{}| girilen =|{}|{}|{}|sonuç ={}" .format(r1,r2,r3,s1,s2,s3,dr))
			kk=0
		else:
			print("sayı giriniz")
	return dd,yd,yy,len(tkr)
#########################
def kn():
	print()
#########################
while y==0:
	cn=input("konsol :")
	if cn=="kumar":
		s=sya()
		a,b=s[0],s[1]
		sg=syg(a,b)
		s1,s2,s3=sg[0],sg[1],sg[2]
		gr=rn(s1,s2,s3,kn,yy,dd,a,b,kc)
		dd,yd,yy,tt=gr[0],gr[1],gr[2],gr[3]
		print("işlem sayısı = {} \ndoğru işlem sayısı = {} \nyanlış işlem sayısı = {}" .format(tt,dd,yy))
	elif cn==".kpn":
		y=1
