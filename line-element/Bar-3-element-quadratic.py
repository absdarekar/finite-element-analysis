#program: Dispalcement, stresses and reactions in a compound, 3 step bar
#author: Atharv Darekar
import numpy;
E=[200,100,69]; # modulus of elasticity of element 1 to 3 GPa
A=[500,300,150]; # cross section area of element 1 to 3 mm^2
L=[50,50,50]; # length of element 1 to 3 mm
f7=float(input("Enter force on node 7 in kN \n")); # force on node 7 kN
k1=1/3*A[0]*E[0]/L[0]*1000; # stiffness of element 1 N.mm^-1
k2=1/3*A[1]*E[1]/L[1]*1000; # stiffness of element 2 N.mm^-1
k3=1/3*A[2]*E[2]/L[2]*1000; # stiffness of element 3 N.mm^-1
K_F=numpy.array([[7*k1,-8*k1,k1,0,0,0,0,0],[-8*k1,16*k1,-8*k1,0,0,0,0,0],[k1,-8*k1,7*k1+7*k2,-8*k2,k2,0,0,0],[0,0,-8*k2,16*k2,-8*k2,0,0,0],[0,0,k2,-8*k2,7*k2+7*k3,-8*k3,k3,0],[0,0,0,0,-8*k3,16*k3,-8*k3,0],[0,0,0,0,k3,-8*k3,7*k3,f7*1000]]); # augmented global stiffness and force matrix
d=numpy.linalg.solve(K_F[1:7,1:7],K_F[1:7,7]); #displacement of node 2-7 mm
d=numpy.hstack((numpy.zeros(1),d)); #displacement of node 1 to 7 mm
for i in range(0,7):
   print("\nDispalcement of node "+str(i+1)+" is "+str(d[i])+" mm \n");
f=numpy.dot(K_F[0:7,0:7],d.transpose()); #reaction at node 1 to 7 kN
print("\nReaction is "+str(f[0]/1000)+" kN \n");
l=numpy.zeros((1,3)); # initialisation of elongation vector
for i in range(2,-1,-1):
    l[0,i]=d[i*2+2]-d[i*2]; # elongation of element 1 to 3 mm
sigma=numpy.zeros((1,3)); # initialisation of stress vector
for i in range(0,3):
  sigma[0,i]=E[i]*l[0,i]/L[i]*1000; # stress of element 1 to 3 N.mm^-2
  print("\nStress of element "+str(i+1)+" is "+str(sigma[0,i])+" N.mm^-2\n");
