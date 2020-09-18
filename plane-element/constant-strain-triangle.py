#program: Shape function
#author: Atharv Darekar
import numpy;
coordinates=numpy.zeros((3,2));
alpha=numpy.zeros(3);
beta=numpy.zeros(3);
gamma=numpy.zeros(3);
N=numpy.zeros(3);
sigma_N=0;
for i in range(0,3):
    coordinates[i,0]=float(input("Enter x"+str(i+1)+"\n"));
    coordinates[i,1]=float(input("Enter y"+str(i+1)+"\n"));
x=float(input("Enter x\n"));
y=float(input("Enter y\n"));
alpha[0]=coordinates[1,0]*coordinates[2,1]-coordinates[2,0]*coordinates[1,1];
alpha[1]=coordinates[2,0]*coordinates[0,1]-coordinates[0,0]*coordinates[2,1];
alpha[2]=coordinates[0,0]*coordinates[1,1]-coordinates[1,0]*coordinates[0,1];
beta[0]=coordinates[1,1]-coordinates[2,1];
beta[1]=coordinates[2,1]-coordinates[0,1];
beta[2]=coordinates[0,1]-coordinates[1,1];
gamma[0]=coordinates[2,0]-coordinates[1,0];
gamma[1]=coordinates[0,0]-coordinates[2,0];
gamma[2]=coordinates[1,0]-coordinates[0,0];
D=numpy.delete(numpy.hstack((numpy.ones((3,2)),coordinates)),0,1);
A=0.5*numpy.linalg.det(D);
for i in range(0,3):
    N[i]=(alpha[i]+beta[i]*x+gamma[i]*y)/(2*A);
for i in range(0,3):
    sigma_N+=N[i];
