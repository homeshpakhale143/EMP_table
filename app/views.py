from django.shortcuts import render
from app.models import *
from django.db.models import Q
from django.db.models import *
from django.http import HttpResponse

# Create your views here.
def display_dept(request):
     QLDO=Dept.objects.all()
     d={'QLDO': QLDO}
     return render(request,'display_dept.html',d)


def display_emp(request):
     QLEO=Emp.objects.all()
     d={'QLEO': QLEO}
     return render(request,'display_emp.html',d)

     
def display_salgrade(request):
     QLSG=Salgrade.objects.all()
     d={'QLSG': QLSG}
     return render(request,'display_salgrade.html',context= d)




def display_equijoins(request):
     JDED=Emp.objects.select_related('DEPTNO').all()
     JDED=Emp.objects.select_related('DEPTNO').filter(ENAME='SMITH')
     JDED=Emp.objects.select_related('DEPTNO').filter(SAL__lte='3000')
     JDED=Emp.objects.select_related('DEPTNO').filter(SAL__gte='2000')
     JDED=Emp.objects.select_related('DEPTNO').filter(ENAME__startswith='A')
     JDED=Emp.objects.select_related('DEPTNO').filter(JOB__contains='MAN')
     JDED=Emp.objects.select_related('DEPTNO').filter(COMM__gte='500')
     JDED=Emp.objects.select_related('DEPTNO').filter(Q(DEPTNO=10) | Q(DEPTNO=30))
     JDED=Emp.objects.select_related('DEPTNO').filter(EMPNO__startswith='75')
     JDED=Emp.objects.select_related('DEPTNO').filter(Q(ENAME='ALLEN') | Q(ENAME='SCOTT'))
     JDED=Emp.objects.select_related('DEPTNO').filter(JOB='CLERK')
     JDED=Emp.objects.select_related('DEPTNO').filter(SAL__lte=3500)
     JDED=Emp.objects.select_related('DEPTNO').filter(HIREDATE='1981-06-09')
     JDED=Emp.objects.select_related('DEPTNO').filter(Q(HIREDATE='1981-06-09'))
     JDED=Emp.objects.select_related('DEPTNO').all()


     #---Displaying the details of Employees whose sal is avg salary---#

     AVGSAL=Emp.objects.aggregate(avg_sal=Avg('SAL'))['avg_sal']
     MAXSAL=Emp.objects.aggregate(max_sal=Max('SAL'))['max_sal']
     SUMSAL=Emp.objects.aggregate(sum_sal=Sum('SAL'))['sum_sal']
     JDED=Emp.objects.select_related('DEPTNO').filter(SAL__gte=AVGSAL)
     JDED=Emp.objects.select_related('DEPTNO').filter(SAL__lte=AVGSAL)

     EGD=Emp.objects.select_related('DEPTNO').annotate(g_a_s=Avg('SAL'))
     EGD=Emp.objects.select_related('DEPTNO').annotate(g_s_s=Sum('SAL'))
     EGD=Emp.objects.values('DEPTNO').annotate(g_a_s=Avg('SAL')).filter(g_a_s__lte=AVGSAL)
     EGD=Emp.objects.values('DEPTNO').annotate(g_a_s=Max('SAL')).filter(g_a_s__lte=MAXSAL)
     # EGD=Emp.objects.values('DEPTNO').annotate(g_a_s=Avg('SAL')).filter(g_a_s__lte=SUMSAL)
     print(EGD)
     # print(JDED)
     # print(JDED)



     d={'JDED':JDED}
     return render(request,'display_equijoins.html',d)


def display_selfjoins(request):
     ESJO=Emp.objects.select_related('MGR').all()
     ESJO=Emp.objects.select_related('MGR').filter(ENAME__startswith='A')
     ESJO=Emp.objects.select_related('MGR').filter(ENAME__endswith='S')
     ESJO=Emp.objects.select_related('MGR').filter(ENAME__contains='k')
     ESJO=Emp.objects.select_related('MGR').filter(ENAME__contains='R')
     ESJO=Emp.objects.select_related('MGR').filter(DEPTNO=10)
     ESJO=Emp.objects.select_related('MGR').filter(DEPTNO=30)
     ESJO=Emp.objects.select_related('MGR').filter(Q(DEPTNO=10) | Q(DEPTNO=50))
     ESJO=Emp.objects.select_related('MGR').filter(JOB='SALESMAN')
     ESJO=Emp.objects.select_related('MGR').filter(JOB='MANAGER')
     ESJO=Emp.objects.select_related('MGR').filter(SAL__gt=1000)
     ESJO=Emp.objects.select_related('MGR').filter(SAL__gt=3000)
     ESJO=Emp.objects.select_related('MGR').filter(SAL__lt=5000)
     ESJO=Emp.objects.select_related('MGR').filter(SAL__lte=3500)
     ESJO=Emp.objects.select_related('MGR').filter(SAL__gte=3000)
     ESJO=Emp.objects.select_related('MGR').filter(EMPNO=7902)
     ESJO=Emp.objects.select_related('MGR').filter(EMPNO__isnull=True)
     ESJO=Emp.objects.select_related('MGR').filter(EMPNO__isnull=False)
     ESJO=Emp.objects.select_related('MGR').filter(MGR__isnull=True)
     ESJO=Emp.objects.select_related('MGR').filter(MGR__isnull=False)
     ESJO=Emp.objects.select_related('MGR').filter(Q(SAL__gt=2000) | Q(SAL__lt=3000))
     ESJO=Emp.objects.select_related('MGR').filter(ENAME='Achuth')
     # ESJO=Emp.objects.select_related('MGR').all()
     d={'ESJO':ESJO}
     return render(request,'display_selfjoins.html',d)

def display_EmpMgrDept(request):
     EMDJ=Emp.objects.select_related('DEPTNO','MGR').all()
     print(EMDJ[0])
     EMDJ=Emp.objects.select_related('DEPTNO','MGR').filter(ENAME__startswith='A')
     EMDJ=Emp.objects.select_related('DEPTNO','MGR').filter(SAL__gt=5000)
     EMDJ=Emp.objects.select_related('DEPTNO','MGR').filter(DEPTNO__in=(10,20,50))
     EMDJ=Emp.objects.select_related('DEPTNO','MGR').filter(ENAME='KING')
     EMDJ=Emp.objects.select_related('MGR').filter(Q(DEPTNO=30) | Q(DEPTNO=50))
     EMDJ=Emp.objects.select_related('MGR').filter(Q(DEPTNO=10) | Q(DEPTNO=40))


     EMDJ=Emp.objects.values('SAL','ENAME').filter(ENAME='ALLEN')
     # EMDJ=Emp.objects.select_related('DEPTNO','MGR').all()
     EMDJ=Emp.objects.extra(where=["LENGTH(ENAME) = 5"])
     EMDJ=Emp.objects.extra(where=["ENAME LIKE '%T_' "])
     # EMDJ=Emp.objects.extra(where=["LENGTH(SAL) = 3"])
     EMDJ=Emp.objects.extra(where=["ENAME LIKE 'S%' "])

     d={'EMDJ':EMDJ}
     return render(request,'display_EmpMgrDept.html',d)

def display_update(request):
     # Emp.objects.filter(ENAME='Achuth').update(JOB='Web Developer')
     # Emp.objects.filter(ENAME='ALLEN').update(JOB='MANAGER')
     # Emp.objects.filter(ENAME='SCOTT').update(DEPTNO=10)
     # Emp.objects.update_or_create(ENAME='SMITH',defaults={'SAL':25000})
     # Emp.objects.update_or_create(ENAME='ALLEN',defaults={'SAL':36000})
     # DO=Dept.objects.get(DEPTNO=50)
     # Emp.objects.update_or_create(ENAME='SMITH',defaults={'DEPTNO':DO})
     # Emp.objects.update_or_create(ENAME='SMITH',SAL=18000,JOB='COOKING',HIREDATE='2023-5-06',COMM=500,defaults={'DEPTNO':DO})
     # Emp.objects.filter(ENAME='SMITH').update(COMM=750)
     
     EDO=Emp.objects.all()
     d={'EDO':EDO}
     return render(request,'display_update.html',d)


def display_delete(request):
     # Emp.objects.filter(ENAME='SCOTT').delete()
     # Emp.objects.filter(JOB='CLERK').delete()
     # Emp.objects.filter(SAL=18000).delete()
     # Emp.objects.filter(ENAME='ALLEN').delete()
     Emp.objects.filter(EMPNO=7844).delete()

     DEO=Emp.objects.all()
     d={'DEO':DEO}
     return render(request,'display_delete.html',d)


def display_aggregate(request):
     # EAO=Emp.objects.aggregate(avg_salary=Avg('SAL'))['avg_salary']
     # EAO=Emp.objects.aggregate(min_salary=Min('SAL'))['min_salary']
     # EAO=Emp.objects.aggregate(max_salary=Max('SAL'))['max_salary']
     # EAO=Emp.objects.aggregate(count_salary=Count('SAL'))['count_salary']
     # EAO=Emp.objects.aggregate(sum_salary=Sum('SAL'))['sum_salary']
     # EAO=Emp.objects.aggregate(min_hiredate=Min('HIREDATE'))['min_hiredate']
     AEAS=Emp.objects.aggregate(A_E_A_S=Avg('SAL'))['A_E_A_S']
     
     # print(EAO)
     print(AEAS)
     return HttpResponse("<center><h1>First We check CMD</h1></center>")